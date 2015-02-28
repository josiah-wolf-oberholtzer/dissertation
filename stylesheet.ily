\version "2.19.15"

#(set-global-staff-size 12)

\layout {
    indent = 0\mm
    ragged-right = ##t
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