# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import scoretools
from abjad.tools import selectortools


persisted_selector = selectortools.Selector(
    callbacks=(
        selectortools.PrototypeSelectorCallback(
            prototype=scoretools.Leaf,
            flatten=True,
            ),
        selectortools.LogicalTieSelectorCallback(
            flatten=True,
            pitched=True,
            trivial=True,
            ),
        selectortools.DurationSelectorCallback(
            duration=selectortools.DurationInequality(
                operator_string='>',
                duration=durationtools.Duration(1, 4),
                ),
            ),
        selectortools.ItemSelectorCallback(
            item=0,
            apply_to_each=True,
            ),
        selectortools.FlattenSelectorCallback(
            depth=-1,
            ),
        ),
    )