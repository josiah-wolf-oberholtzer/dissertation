# Introduction

Score as extension. The score extends the composition model. The composition
model extends the notation model. The notation model extends computation.

Scores made of segments. Segments constructed by segment-makers. Segment-makers
coordinating multiple compositional processes in a maquette, a collage.

Why not do everything in one huge pass? I've done. A lot. Monoliths are
difficult to work with, both poetically and practically. The process doesn't
allow entry. The swath is too big - it's a cognitive burden. Smaller chunks
allow for more decision points.

No randomness. Repeatable.

Fully automated typesetting. The gives tremendous freedom, but also
hinders certain types of typography. Murat's slurs. Instant notation, though,
regardless of the degree of change.

The only things that can exist are exactly what can be described and
implemented.

-   Formalized score control
-   Research into same
-   This is a treatise

Tools discussion:
Python: Python packages and modules, classes, functions and instances, imports,
LilyPond, LaTeX: Automated typesetting, include statements.

Intended audience? Mainly composers who wish to work more closely with
computation. Computer scientists might enjoy this document, but the topics are
not necessarily discussed rigorously. This is a practical discussion. A kind of
lengthy tutorial on issues surrounding the creation of large-scale musical
works in an entirely formalized way.

My hope is that after reading the following chapters, a student of this
document could proceed to read through the material and segment definitions for
each of the three Invisible Cities score included in the appendices and
understand their contents.

## Personal background

-   khml
    -   An early example of maquette
-   nptl_b
    -   Max to spreadsheets, then by hand
    -   Notion of parametric specification
-   mbrsi
    -   Max to spreadsheets, then by hand
    -   Notion of timespans already established
    -   Incredibly labor intensive
    -   Attempted to automate via Illustrator, failed
    -   One single fabric, unfolding
    -   Impossible to maquette different textures together
-   aurora
    -   Revived the project, years later
    -   Implemented entirely in Python with Abjad
    -   Rendered by LilyPond
    -   Finally possible to maquette textures
    -   No time-signature changes possible: as though on flat grid
-   plague water
    -   Time signatures!
-   invisible cities
    -   Modernized the work done in plague water

## Historical background

-   Patchwork
-   OpenMusic
-   PWGL
-   Bach
-   SuperCollider
-   Score
-   Rhinoceros and Grasshopper
-   Why didn't I use any of these?
    -   I realized text-based work was the right way to go
    -   Rapid prototyping, legibility, visualization all important
    -   Need a well-maintained language

## About the text

-   Who is this for?
-   Why am I writing this?
-   What is this really about?