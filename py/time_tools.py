# -*- encoding: utf-8 -*-
from abjad import Duration
from abjad import Offset
from abjad import Voice
from abjad import iterate
from abjad.tools import mathtools
from abjad.tools import metertools
from abjad.tools import rhythmmakertools
from abjad.tools import scoretools
from abjad.tools import timespantools


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
    music = rhythm_maker(durations, seeds=seed)
    for i, x in enumerate(music):
        if len(x) == 1 and isinstance(x[0], scoretools.Tuplet):
            music[i] = x[0]
        else:
            music[i] = scoretools.Container(x)
    music = scoretools.Container(music)
    return music


def make_silence_music(start_offset, stop_offset, meter_boundaries):
    silence_timespan = timespantools.Timespan(start_offset, stop_offset)
    shards = silence_timespan.split_at_offsets(meter_boundaries)
    durations = [_.duration for _ in shards if _.duration]
    mask = rhythmmakertools.mask_all()
    rhythm_maker = rhythmmakertools.NoteRhythmMaker(output_masks=[mask])
    music = make_music(rhythm_maker, durations)
    return music


def make_performed_music(rhythm_maker, timespans, meter_boundaries, seed=0):
    split_timespans = timespantools.TimespanInventory()
    for shard in timespans.split_at_offsets(meter_boundaries):
        split_timespans.extend(shard)
    durations = [_.duration for _ in split_timespans if _.duration]
    music = make_music(rhythm_maker, durations, seed=seed)
    return music


def add_time_signature_context(score, meters):
    time_signatures = [_.implied_time_signature for _ in meters]
    measures = scoretools.make_spacer_skip_measures(time_signatures)
    time_signature_context = scoretools.Context(
        [measures],
        context_name='TimeSignatureContext',
        name='TimeSignatureContext',
        )
    score.insert(0, time_signature_context)


def get_all_voicewise_timespans(timespan_inventory):
    voicewise_timespans = {}
    for timespan in timespan_inventory:
        voice_name = timespan.voice_name
        if voice_name not in voicewise_timespans:
            voicewise_timespans[voice_name] = timespantools.TimespanInventory()
        voicewise_timespans[voice_name].append(timespan)
    return voicewise_timespans


def build_score(
    performed_rhythm_maker,
    permitted_meters,
    score_template,
    timespan_inventory,
    ):
    score = score_template()
    fitted_meters, meter_boundaries = get_meters_and_meter_boundaries(
        timespan_inventory, permitted_meters)
    all_voicewise_timespans = get_all_voicewise_timespans(timespan_inventory)
    seed = 0
    for voice in iterate(score).by_class(Voice):
        voice_timespans = all_voicewise_timespans[voice.name]
        previous_stop_offset = Offset(0)
        for shard in voice_timespans.partition(include_tangent_timespans=True):
            if shard.start_offset != previous_stop_offset:
                silence_music = make_silence_music(
                    meter_boundaries=meter_boundaries,
                    start_offset=previous_stop_offset,
                    stop_offset=shard.start_offset,
                    )
                voice.append(silence_music)
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
            silence_music = make_silence_music(
                meter_boundaries=meter_boundaries,
                start_offset=previous_stop_offset,
                stop_offset=meter_boundaries[-1],
                )
            voice.append(silence_music)
    add_time_signature_context(score, fitted_meters)
    return score