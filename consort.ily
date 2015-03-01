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
        \override TupletBracket.direction = #up
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
        \override TupletBracket.staff-padding = 3
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 999
        \override TupletNumber.stencil = ##f
        \override TupletBracket.direction = #down
        \override TupletBracket.thickness = 2
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
        \override TupletBracket.staff-padding = 3
        \override TupletBracket.outside-staff-padding = 1
        \override TupletBracket.outside-staff-priority = 1000
        \override NoteColumn.ignore-collision = ##t
        \override TupletBracket.direction = #down
        \override TupletBracket.thickness = 2
    }
    \context {
        \Staff
        \remove Time_signature_engraver
        \accepts AnnotatedDivisionsVoice
        \accepts AnnotatedPhrasesVoice
    }
    \context {
        \RhythmicStaff
        \consists Clef_engraver
        \remove Time_signature_engraver
        \accepts AnnotatedDivisionsVoice
        \accepts AnnotatedPhrasesVoice
    }
    \context {
        \name TimeSignatureContext
        \type Engraver_group
        \consists Axis_group_engraver
        %\consists Bar_number_engraver
        \consists Mark_engraver
        \consists Metronome_mark_engraver
        \consists Script_engraver
        \consists Text_engraver
        \consists Text_spanner_engraver
        \consists Time_signature_engraver
        \override BarNumber.extra-offset = #'(-6 . -4)
        \override BarNumber.font-name = "Didot Italic"
        \override BarNumber.font-size = 1
        \override BarNumber.padding = 4
        \override BarNumber.stencil = #(make-stencil-circler 0.1 0.7 ly:text-interface::print)
        \override Beam.direction = #up
        \override MetronomeMark.X-extent = #'(0 . 0)
        \override MetronomeMark.Y-extent = #'(0 . 0)
        \override MetronomeMark.break-align-symbols = #'(left-edge)
        \override MetronomeMark.extra-offset = #'(4 . -6)
        \override MetronomeMark.font-size = 3
        \override RehearsalMark.X-extent = #'(0 . 0)
        \override RehearsalMark.X-offset = 6
        \override RehearsalMark.Y-offset = -2.25
        \override RehearsalMark.break-align-symbols = #'(time-signature)
        \override RehearsalMark.break-visibility = #end-of-line-invisible
        \override RehearsalMark.font-name = "Didot"
        \override RehearsalMark.font-size = 8
        \override RehearsalMark.outside-staff-priority = 500
        \override Rest.direction = #up
        \override Rest.staff-position = -100
        \override RehearsalMark.self-alignment-X = #center
        \override Script.extra-offset = #'(4 . -9)
        \override Script.font-size = 6
        \override Stem.direction = #up
        \override TextScript.font-size = 3
        \override TextScript.outside-staff-priority = 600
        \override TextScript.padding = 6
        \override TextSpanner.bound-details.right.attach-dir = #left
        \override TextSpanner.padding = 6.75
        \override TimeSignature.X-extent = #'(0 . 0)
        \override TimeSignature.break-align-symbol = #'left-edge
        \override TimeSignature.break-visibility = #end-of-line-invisible
        \override TimeSignature.font-size = 3
        \override TimeSignature.space-alist.clef = #'(extra-space . 0.5)
        \override TimeSignature.style = #'numbered
        \override VerticalAxisGroup.default-staff-staff-spacing = #'(
            (basic-distance . 0)
            (minimum-distance . 14)
            (padding . 0)
            (stretchability . 0)
        )
        \override VerticalAxisGroup.minimum-Y-extent = #'(-20 . 20)
    }
    \context {
        \Score
        \accepts TimeSignatureContext
        \remove Bar_number_engraver
        \remove Mark_engraver
        \remove Metronome_mark_engraver
        \override BarLine.bar-extent = #'(-2 . 2)
        \override BarLine.hair-thickness = 0.5
        \override BarLine.space-alist = #'(
            (time-signature extra-space . 0.0)
            (custos minimum-space . 0.0) 
            (clef minimum-space . 0.0) 
            (key-signature extra-space . 0.0) 
            (key-cancellation extra-space . 0.0) 
            (first-note fixed-space . 0.0) 
            (next-note semi-fixed-space . 0.0) 
            (right-edge extra-space . 0.0)
            )
        \override Beam.beam-thickness = 0.75
        \override Beam.breakable = ##t
        \override Beam.length-fraction = 1.5
        \override DynamicLineSpanner.add-stem-support = ##t
        \override DynamicLineSpanner.outside-staff-padding = 1
        \override Glissando.after-line-breaking = ##t
        \override Glissando.breakable = ##t
        \override Glissando.thickness = 3
        \override GraceSpacing.common-shortest-duration = #(ly:make-moment 1 8)
        \override NoteCollision.merge-differently-dotted = ##t
        \override NoteCollision.merge-differently-headed = ##t
        \override NoteColumn.ignore-collision = ##t
        \override OttavaBracket.add-stem-support = ##t
        \override OttavaBracket.padding = 2
        %\override SpacingSpanner.base-shortest-duration = #(ly:make-moment 1 64)
        %\override SpacingSpanner.strict-grace-spacing = ##f
        %\override SpacingSpanner.strict-note-spacing = ##f
        \override SpacingSpanner.uniform-stretching = ##t
        \override Beam.direction = #up
        \override Beam.positions = #'(5 . 5)
        \override Stem.details.beamed-lengths = #'(6)
        \override Stem.details.lengths = #'(6)
        \override Stem.stemlet-length = 1.5
        \override StemTremolo.beam-width = 1.5
        \override StemTremolo.flag-count = 4
        \override StemTremolo.slope = 0.5
        \override StemTremolo.style = #'default
        \override SustainPedal.self-alignment-X = #CENTER
        \override SustainPedalLineSpanner.padding = 2
        \override SustainPedalLineSpanner.to-barline = ##t
        \override TextScript.add-stem-support = ##t
        \override TextScript.outside-staff-padding = 1
        \override TextScript.padding = 1
        \override TextScript.staff-padding = 1
        \override TextSpanner.bound-details.right.padding = 2.5
        \override TrillPitchAccidental.avoid-slur = #'ignore
        \override TrillPitchAccidental.layer = 1000
        \override TrillPitchAccidental.whiteout = ##t
        \override TrillPitchHead.layer = 1000
        \override TrillPitchHead.whiteout = ##t
        \override TrillSpanner.bound-details.right.padding = 1
        \override TrillSpanner.outside-staff-padding = 1
        \override TrillSpanner.padding = 1
        \override TupletBracket.avoid-scripts = ##t
        \override TupletBracket.direction = #down
        \override TupletBracket.full-length-to-extent = ##t
        \override TupletBracket.outside-staff-padding = 2
        \override TupletBracket.padding = 2
        \override TupletNumber.font-size = 1
        \override TupletNumber.text = #tuplet-number::calc-fraction-text
        \override VerticalAxisGroup.staff-staff-spacing = #'(
            (basic-distance . 8)
            (minimum-distance . 14)
            (padding . 4)
            (stretchability . 0)
            )
        autoBeaming = ##f
        proportionalNotationDuration = #(ly:make-moment 1 24)
        tupletFullLength = ##t
    }
}

\paper {
    left-margin = 1\in
}