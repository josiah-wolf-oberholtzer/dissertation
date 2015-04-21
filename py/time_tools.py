# -*- encoding: utf-8 -*-
import collections
import consort
from abjad import Duration
from abjad import Offset
from abjad import Voice
from abjad import inspect_
from abjad import iterate
from abjad import mutate
from abjad.tools import mathtools
from abjad.tools import metertools
from abjad.tools import rhythmmakertools
from abjad.tools import scoretools
from abjad.tools import templatetools
from abjad.tools import timespantools


def add_time_signature_context(score, meters):
    time_signatures = [_.implied_time_signature for _ in meters]
    measures = scoretools.make_spacer_skip_measures(time_signatures)
    time_signature_context = scoretools.Context(
        [measures],
        context_name='TimeSignatureContext',
        name='TimeSignatureContext',
        )
    score.insert(0, time_signature_context)


def build_score(
    performed_rhythm_maker,
    permitted_meters,
    score_template,
    timespan_inventory,
    ):
    fitted_meters, meter_boundaries = get_meters_and_meter_boundaries(
        timespan_inventory, permitted_meters)
    all_voicewise_timespans = get_all_voicewise_timespans(timespan_inventory)
    seed = 0
    score = score_template()
    for voice in iterate(score).by_class(Voice):
        if voice.name not in all_voicewise_timespans:
            all_voicewise_timespans[voice.name] = \
                timespantools.TimespanInventory()
        voice_timespans = all_voicewise_timespans[voice.name]
        previous_stop_offset = Offset(0)
        for shard in voice_timespans.partition(include_tangent_timespans=True):
            if shard.start_offset != previous_stop_offset:
                silent_music = make_silent_music(
                    meter_boundaries=meter_boundaries,
                    start_offset=previous_stop_offset,
                    stop_offset=shard.start_offset,
                    )
                voice.append(silent_music)
            performed_music = make_performed_music(
                meter_boundaries=meter_boundaries,
                rhythm_maker=performed_rhythm_maker,
                seed=seed,
                timespans=shard,
                )
            voice.append(performed_music)
            seed += 1
            previous_stop_offset = shard.stop_offset
        if previous_stop_offset != meter_boundaries[-1]:
            silent_music = make_silent_music(
                meter_boundaries=meter_boundaries,
                start_offset=previous_stop_offset,
                stop_offset=meter_boundaries[-1],
                )
            voice.append(silent_music)
        for phrase in voice:
            rewrite_meters(phrase, fitted_meters, meter_boundaries)
    add_time_signature_context(score, fitted_meters)
    return score


def get_all_voicewise_timespans(timespan_inventory):
    voicewise_timespans = {}
    for timespan in timespan_inventory:
        voice_name = timespan.voice_name
        if voice_name not in voicewise_timespans:
            voicewise_timespans[voice_name] = timespantools.TimespanInventory()
        voicewise_timespans[voice_name].append(timespan)
    return voicewise_timespans


def get_meters_and_meter_boundaries(timespan_inventory, permitted_meters):
    offset_counter = metertools.OffsetCounter(timespan_inventory)
    fitted_meters = metertools.Meter.fit_meters_to_expr(
        expr=offset_counter,
        maximum_run_length=1,
        meters=permitted_meters,
        )
    meter_durations = [Duration(_) for _ in fitted_meters]
    meter_boundaries = mathtools.cumulative_sums(
        meter_durations,
        start=Offset(0),
        )
    return fitted_meters, meter_boundaries


def make_music(rhythm_maker, durations, seed=0):
    music = rhythm_maker(durations, rotation=seed)
    for i, division in enumerate(music):
        if len(division) == 1 and isinstance(division[0], scoretools.Tuplet):
            music[i] = division[0]
        else:
            music[i] = scoretools.Container(division)
    music = scoretools.Container(music)
    return music


def make_performed_music(rhythm_maker, timespans, meter_boundaries, seed=0):
    split_timespans = timespantools.TimespanInventory()
    for shard in timespans.split_at_offsets(meter_boundaries):
        split_timespans.extend(shard)
    durations = [_.duration for _ in split_timespans if _.duration]
    music = make_music(rhythm_maker, durations, seed=seed)
    return music


def make_silent_music(start_offset, stop_offset, meter_boundaries):
    silence_timespan = timespantools.Timespan(start_offset, stop_offset)
    shards = silence_timespan.split_at_offsets(meter_boundaries)
    durations = [_.duration for _ in shards if _.duration]
    mask = rhythmmakertools.silence_all()
    rhythm_maker = rhythmmakertools.NoteRhythmMaker(output_masks=[mask])
    music = make_music(rhythm_maker, durations)
    return music


def rewrite_meters(phrase, meters, meter_boundaries):
    pairs = list(zip(meters, meter_boundaries))
    for division in phrase:
        division_offset = inspect_(division).get_timespan().start_offset
        while 1 < len(pairs) and pairs[1][1] <= division_offset:
            pairs.pop(0)
        if isinstance(division, scoretools.Tuplet):
            contents_duration = division._contents_duration
            meter = metertools.Meter(contents_duration)
            mutate(division).rewrite_meter(
                meter,
                boundary_depth=1,
                )
        else:
            meter, meter_boundary = pairs[0]
            initial_offset = division_offset - meter_boundary
            mutate(division).rewrite_meter(
                meter,
                boundary_depth=1,
                initial_offset=initial_offset,
                )

if __name__ == '__main__':
    performed_rhythm_maker = rhythmmakertools.TaleaRhythmMaker(
        beam_specifier=rhythmmakertools.BeamSpecifier(
            beam_each_division=True,
            beam_divisions_together=True,
            ),
        extra_counts_per_division=(0, 1),
        talea=rhythmmakertools.Talea([1, 2, 3], 16),
        )
    permitted_meters = metertools.MeterInventory([
        (2, 4), (4, 8), (3, 4), (6, 8), (7, 8), (4, 4),
        ])
    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(
        staff_count=4, with_clefs=True,
        )
    music_specifiers = collections.OrderedDict([
        ('Voice 1', None),
        ('Voice 2', None),
        ('Voice 3', None),
        ('Voice 4', None),
        ])
    target_timespan = timespantools.Timespan(0, (19, 4))
    timespan_maker = consort.TaleaTimespanMaker(
        initial_silence_talea=rhythmmakertools.Talea(
            counts=(0, 1, 3),
            denominator=8,
            ),
        playing_talea=rhythmmakertools.Talea(
            counts=(1, 2, 3, 4),
            denominator=4,
            ),
        playing_groupings=(1, 2),
        reflect=True,
        repeat=True,
        silence_talea=rhythmmakertools.Talea(
            counts=(3, 1, 1),
            denominator=8,
            ),
        step_anchor=Right,
        synchronize_groupings=False,
        synchronize_step=False,
        )
    timespan_inventory = timespan_maker(
        music_specifiers=music_specifiers,
        target_timespan=target_timespan,
        )

    score = build_score(
        performed_rhythm_maker=performed_rhythm_maker,
        permitted_meters=permitted_meters,
        score_template=score_template,
        timespan_inventory=timespan_inventory,
        )

    multiplier = Duration(24, 4) / Duration(19, 4)
    timespan_inventory = timespan_inventory.reflect()
    timespan_inventory = timespan_inventory.stretch(multiplier)
    timespan_inventory = timespan_inventory.round_offsets(Duration(1, 8))

    score = build_score(
        performed_rhythm_maker=performed_rhythm_maker,
        permitted_meters=permitted_meters,
        score_template=score_template,
        timespan_inventory=timespan_inventory,
        )