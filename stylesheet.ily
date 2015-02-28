\version "2.19.0"

#(set-global-staff-size 12)

\header {
    tagline = \markup { }
}

\layout {
    \accidentalStyle forget
    indent = 0\mm
    ragged-right = ##t
    \context {
        \Voice
        \remove Forbid_line_break_engraver
    }
    \context {
        \Voice
        \name AnnotatedDivisionsVoice
        \type Engraver_group
        \alias Voice
        \override Accidental.stencil = ##f
        \override Dots.stencil = ##f
        \override Flag.stencil = ##f
        \override NoteColumn.ignore-collision = ##t
        \override NoteHead.no-ledgers = ##t
        \override NoteHead.transparent = ##t
        \override Stem.stencil = ##f
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 999
        \override TupletNumber.stencil = ##f
        \override TupletBracket.direction = #down
        \override TupletBracket.thickness = 3
    }
    \context {
        \Voice
        \name AnnotatedPhrasesVoice
        \type Engraver_group
        \alias Voice
        \override Accidental.stencil = ##f
        \override Dots.stencil = ##f
        \override Flag.stencil = ##f
        \override NoteHead.no-ledgers = ##t
        \override NoteHead.transparent = ##t
        \override Stem.stencil = ##f
        \override TupletNumber.stencil = ##f
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 1000
        \override NoteColumn.ignore-collision = ##t
        \override TupletBracket.direction = #down
        \override TupletBracket.thickness = 3
    }
    \context {
        \Staff
        \accepts AnnotatedDivisionsVoice
        \accepts AnnotatedPhrasesVoice
    }
    \context {
        \RhythmicStaff
        \accepts AnnotatedDivisionsVoice
        \accepts AnnotatedPhrasesVoice
    }
    \context {
        \Score
        \remove Bar_number_engraver
        \override Beam.positions = #'(4 . 4)
        %\override SpacingSpanner.strict-grace-spacing = ##t
        %\override SpacingSpanner.strict-note-spacing = ##t
        \override SpacingSpanner.uniform-stretching = ##t
        \override Stem.length = 8.25
        \override TextScript.outside-staff-padding = 1
        \override TimeSignature.style = #'numbered
        \override TupletBracket.bracket-visibility = ##t
        \override TupletBracket.minimum-length = 3
        \override TupletBracket.outside-staff-padding = 1.5
        \override TupletBracket.padding = 1.5
        \override TupletBracket.breakable = ##t
        \override TupletBracket.springs-and-rods = #ly:spanner::set-spacing-rods
        \override TupletBracket.staff-padding = 2.25
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
        proportionalNotationDuration = #(ly:make-moment 1 24)
        tupletFullLength = ##t
    }
}

\paper {
    left-margin = 1\in
}