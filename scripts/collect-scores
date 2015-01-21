#! /usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import print_function
import os
import shutil
import dissertation
import aurora
import armilla
import ersilia
import plague_water
import zaira
from abjad.tools import stringtools

if __name__ == '__main__':
    target_directory = os.path.join(
        dissertation.__path__[0],
        'scores',
        )
    score_packages = (
        aurora,
        armilla,
        ersilia,
        plague_water,
        zaira,
        )
    for score_package in score_packages:
        score_name = score_package.__name__
        score_name = stringtools.to_dash_case(score_name)
        source_path = os.path.join(
            score_package.__path__[0],
            'build',
            'score.pdf',
            )
        if not os.path.exists(source_path):
            continue
        target_path = os.path.join(
            target_directory,
            '{}-score.pdf'.format(score_name),
            )
        print('Copying...')
        print('\tfrom:', source_path)
        print('\tto:  ', target_path)
        shutil.copy(source_path, target_path)