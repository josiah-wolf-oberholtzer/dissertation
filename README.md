dissertation
============

A theory of composition
-----------------------

## motivations

- specification
- interpretation
- different timescales

## actors

- makers
    - configure and call
- handlers
    - configure and call
- selectors
    - configure and call
- specifiers
    - aggregate makers, handlers
- materials
    - something out of time
- segments
    - something in time

## before rhythm, after rhythm

## dramatis personae

- segment maker
- music setting
- timespan maker
    - independent, dependent
- timespan identifier
    - ratio parts expression
- context names
- music specifier
    - composite music specifier
- rhythm maker
    - composite rhythm maker
- handler
    - grace
    - pitch
    - attachment
- score post processing

Laying out time
---------------

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
- independent vs dependent
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

Consort's time manager
----------------------

## the time manager pipeline

## populating independent timespans

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

## populating dependent timespans

- populate multiplexed timespans
- demultiplex timespans
- split demultiplexed timespans
- prune short timespans
- prune malformed timespans
- consolidate demultiplexed timespans
- inscribe demultiplexed timespans

## post processing

- populate silent timespans
- validate timespans
- rewrite meters
- collect attack points
- populate score

Consort's handlers
------------------

## score iteration

- phrase-wise
- time-wise
- seeds

## grace handler

- quirks of LilyPond's grace handling

## pitch handler

- pitch specifier
- pitch operation
- pitch operation specifier
- register specifier

## attachment handler

- attachment expressions
- selectors