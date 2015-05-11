
%# Composing in text
%
%-   Allography
%-   Version control
%-   If the input is versioned text, not graphic, there is always a clear,
%    retrievable history of the thought process behind the work
%
%# Maquettes and unfolding processes
%
%-   Timespans allow for large scale phrasing and density structures.
%-   They simply model attack points and durations, making attack and overlap
%    density easy to play with.
%-   Timespan annotations allow for maquette-like composition techniques, or
%    working in a way that conceptually mirrors working with a DAW, even though
%    there is no real graphic output except for notation itself.
%-   Annotations can act as a description of what sort of material should appear
%    in what locations -- both horizontally in time and vertically in the score
%    hierarchy.
%-   Timespans also allow for overlap, and have affordances for masking.
%-   This allows timespans to be created by a factories in layers, and those
%    layers resolved down to a single non-overlapping layer via masking.
%
%# Patterns and randomness
%
%-   All of the maker tools described here (and in the next chapter) emphasize
%    working with patterns.
%-   Sufficiently complex patterns of discrete numbers (and combinations of
%    patterns) are perceptually indistinguishable from randomness. It doesn't
%    take much.
%-   Likewise, randomness -- no matter how it is arrived at, windowed, weighted
%    and so forth -- is a kind of maintenance burden. How can you know that
%    your compositional machinery is behaving correctly when the results are
%    always different by design?
%-   Why the extensive use of patterns rather than anything else?
%-   Patterns are sufficient
%-   They are also testable
%
%# Architecture and extensibility
%
%-   Only a few recipes for timespan and rhythm creation have been outlined
%    here. Obviously, many more are possible, with other paradigms. The models
%    described here generally rely on patterns. Other work could create
%    rhythm-makers which take pitches as input, or which follow breakpoints, or
%    mimic some other external structure. Likewise with timespan-makers. More
%    work could be done to create stronger intentional interrelations between
%    timespans.
%-   One of the strengths in the overall design philosophy described throughout
%    this chapter is extensibility. Just because I *haven't* yet created a
%    derived-from-bird-song rhythm-maker doesn't mean I can't. Such a maker
%    could be created and follow the same interface as all other rhythm-makers,
%    benefiting from their foundation of shared notational logics.
%-   More factories are possible
%-   Those outlined here are neither the *only* nor the *best* possible
%    factories one could design
%-   New factories can make use of the interfaces implemented by these
%    factory families (timespan- and rhythm-makers)
%-   New factories can also propose entirely new ways of working
%    (such as...)
%-   Extensibility is afforded because the basic building blocks --
%    timespans, timespan inventories, meter and Abjad's model of score --
%    are rock solid
%-   This way of working also has implications about composing algorithms vs
%    composing *with* algorithms
%-   The segment-maker (and friends) are designed as black boxes, but also - for
%    me, anyways - aren't actually
%-   Could someone else even use this system? Maybe, maybe not. I'm more
%    concerned with teaching people design principles so that they can construct
%    their own compositional models on top of systems such as Abjad.
%
%# Score as evaluable expression, expressivity
%
%-   People always think machines are in control. Hardly.
%-   Still, this is about working within formal constraints
%-   Avoid fractal act
%-   Where to position messiness
%
%# Future work
%
%In no way do I consider this project finished. Nor do I think a project like
%this can ever be complete. There is, in my opinion, no single universal
%methodology to composition, nor should there ever be. There is still quite a
%lot of work to do to solve an entire array of practical problems, let alone
%aesthetic ones. Having devoted so much effort to large- and small-scale time
%structures, I need to turn my attention toward harmony and orchestra as
%constraints and coordinating forces.
%
%In no way do I consider this project finished. Nor do I think a project like
%this can ever be complete. There is, in my opinion, no single universal
%methodology to composition, nor should there ever be. There is still quite a
%lot of work to do to solve an entire array of practical problems, let alone
%aesthetic ones.
%
%Having devoted so much effort to large- and small-scale time structures, I need
%to turn my attention toward harmony and orchestra as constraints and
%coordinating forces.
%
%-   multi-staff writing, piano music pedaling, staff-change-writing
%-   more flexible pitch structuring
%    -   shared sonorities between parts
%    -   fix problems of pitch handler hashing
%    -   separate pitch-handler into pitch-class, registration- and chord-
%    -   new pitch handlers
%    -   modeling of counterpoint rules and dissonance
%        - obviously is there is a tremendous amount of research into this
%          the question is not of finding something new, but of studying the 
%          available research and evaluating various implementations
%-   idiomatic writing and awareness
%    -   improve string writing based on fingerings and string numbers
%    -   provide models of wind multiphonics
%    -   test and warn for difficult or impossible wind trills and breathing
%    -   improve instrument-specific dynamic handling
%-   explicit modeling of variation / transformation between parts in a
%    polyphonic texture
%
%There is, I think, always a negotiation between making the "truest" model and
%simply getting the job done.
%
%# Parting words
%
%My intention with providing the complete sources to both my scores and working
%methods is not that others copy me, although they certainly can if they like. I
%would not be offended, but maybe a little disappointed that someone who managed
%to put together the tools and knowledge was also so strangely lazy that they
%didn't take the time to place some personal stamp on their duplication by
%turning the knobs or mixing the potions differently. But that seems incredibly
%unlikely to me.
%
%Rather, I want this shared knowledge to be something like a lifeboat to those
%who come after me, rather than hiding it away to collect dust.
%
%I imagine myself, a composer ten years younger, searching for answers to many
%of the questions I've now made good progress on solving, questions which rarely
%even concern making art because there is still too much groundwork to lay. Had
%I a clear path then to follow, change, or even wholly react against,
%maybe I would have produced more music by now. Or maybe not. I no longer have
%the same misgivings as I did when younger about splitting my creative energies
%between composition and engineering. If anything, they are now the same
%activity.
%
%While the code presented here may become dusty, as most code does, the
%concepts and techniques -- as separate from their concrete implementations --
%most likely won't. While everything has been presented in Python, this work
%could, and should, be implemented in many other programming languages.