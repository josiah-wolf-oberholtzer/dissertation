Consort: laying out time
========================

## timespans and timespan inventories

- offsets and duration
- wellformedness
- time relations: intersection, congruency etc.
- unioning, differencing and splitting
- multiplexing and demultiplexing
- resolution
- partitioning
- timespan collection vs timespan inventory

## rhythm makers

- divisions
- rhythm maker
- specifiers: tie, duration spelling, beam
- specific rhythm makers
    - NoteRhythmMaker
    - IncisedRhythmMaker
    - EvenDivisionsRhythmMaker
    - TaleaRhythmMaker
- composite rhythm maker

## meter finding and rewriting

- meters vs time signatures
    - rhythm trees
- finding meters
    - metric accent kernels
    - offset counters
    - discard final silence
- rewriting meters
    - specific iteration techniques
    - boundary depth
    - dot count

## performed and silent timespans

- payloaded timespans:
    - layer
    - voice name
- performed timespans:
    - forbid fusing
    - forbid splitting
    - minimum duration
    - (additionally, music specifier: minimum phrase duration)
    - divisions
    - music
    - music specifier

## timespan makers

- timespan specifier
- target timespans
- talea
- padding
- flooded timespan maker
- dependent timespan maker
- talea timespan maker
    - taleas: playing, silence and initial silence
    - groupings
    - synchronization
    - repeat and reflect
- aside: looms in aurora

## the time manager pipeline
 
- populate independent timespans
    - populate multiplexed timespans
    - find meters
    - demultiplex timespans
        - resolve timespan inventories
        - subtract timespan inventories
    - split demultiplexed timespans
    - prune malformed timespans
    - consolidate demultiplexed timespans
    - inscribe demultiplexed timespans
        - get rhythm maker
        - make simple music
        - consolidate rests
        - group nonsilent divisions
    - multiplex timespans
    - prune short timespans
    - prune meters
- populate dependent timespans
    - populate multiplexed timespans
    - demultiplex timespans
    - split demultiplexed timespans
    - prune short timespans
    - prune malformed timespans
    - consolidate demultiplexed timespans
    - inscribe demultiplexed timespans
- populate silent timespans
- validate timespans
- rewrite meters
- collect attack points
- populate score