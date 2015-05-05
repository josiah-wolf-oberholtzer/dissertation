# -*- coding: utf-8 -*-
"""
    pygments.styles.dissertation
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    A colorful style, inspired by the terminal highlighting style.

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
     Number, Operator, Generic, Whitespace


class DissertationStyle(Style):
    """
    A colorful style, inspired by the terminal highlighting style.
    """

    default_style = ""

    crimson =    '#a51c30'

    ink =        '#1e1e1e'
    mortar =     '#8c8179'
    parchment =  '#f3f3f1'
    slate =      '#8996a0'
    shade =      '#bac5c6'

    indigo =     '#293352'
    bluebonnet = '#4e84c4'
    ivy =        '#52854c'
    pear =       '#c3d7a4'
    saffron =    '#d16103'
    creme =      '#f4edca'
    gold =       '#c4961a'
    lemon =      '#ffdb6d'

    styles = {
        Whitespace:                 '#bbbbbb',

        Comment:                    'italic #aaaaaa',
        Comment.Preproc:            'noitalic #4c8317',
        Comment.Special:            'italic #0000aa',

        Keyword:                    indigo,
        Keyword.Type:               '#00aaaa',

        Operator.Word:              '#0000aa',

        Name.Builtin:               mortar,
        Name.Function:              crimson,
        Name.Class:                 'underline {}'.format(crimson),
        Name.Namespace:             'underline #00aaaa',
        Name.Variable:              '#aa0000',
        Name.Constant:              '#aa0000',
        Name.Entity:                'bold #800',
        Name.Attribute:             '#1e90ff',
        Name.Tag:                   'bold #1e90ff',
        Name.Decorator:             '#888888',

        String:                     crimson,
        String.Symbol:              '#0000aa',
        String.Regex:               '#009999',

        Number:                     '#009999',

        Generic.Heading:            'bold #000080',
        Generic.Subheading:         'bold #800080',
        Generic.Deleted:            '#aa0000',
        Generic.Inserted:           '#00aa00',
        Generic.Error:              '#aa0000',
        Generic.Emph:               'italic',
        Generic.Strong:             'bold',
        Generic.Prompt:             slate,
        Generic.Output:             slate,
        Generic.Traceback:          '#aa0000',

        Error:                      '#F00 bg:#FAA'
    }