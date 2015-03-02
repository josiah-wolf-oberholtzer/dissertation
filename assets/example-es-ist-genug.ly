\version "2.19.5"

\language "english"

\header {
    composer = "J. S. Bach"
    title = "Es ist genug"
    tagline = \markup { }
}

\new StaffGroup <<
    \new Staff <<
        \key af \major
        \new Voice = "Soprano" {
            \voiceOne
            af'2 bf'4 c'' |
            d''2 ^\fermata r4 d'' | 
            ef'' bf' bf' df'' | 
            c''2. ^\fermata
        }
        \new Voice = "Alto" {
            \voiceTwo
            ef'2 ef'4 df'8 c'8 | 
            g'2 _\fermata r4 g' |
            g'4. af'8 g' f' g' ef' | 
            af'2. _\fermata
        }
    >>
    \new Staff <<
        \clef bass
        \key af \major
        \new Voice = "Tenor" {
            \voiceOne
            c'2 bf4 f' | 
            f'2 ^\fermata r4 b |
            c'8 df' ef'4 ef' ef' | 
            ef'2. ^\fermata
        }
        \new Voice = "Bass" {
            \voiceTwo
            af2 g4 a4 | 
            b2 _\fermata r4 g |
            c'8 bf16 af16 g8 f ef df c bf, | 
            af,2. _\fermata
        }
    >>
>>