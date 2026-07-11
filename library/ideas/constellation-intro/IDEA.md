# IDEA — Constellation: decks from patterns, not from scratch

> Worked example of the `ideate` skill's output — and a live brief: this deck
> will be constellation's own demo when `compose` exists.

Audience: developers who use AI agents and still hand-build every slide; they believe deck-making is unavoidable manual labor
Occasion: 10-minute demo talk (meetup / internal sharing), EN with KR-ready structure
Core message: **Your past decks already contain your future ones — extract the patterns once, compose forever.**
Arc: before → after → bridge
Tone: confident-but-playful (one spoon of humor)

## Outline
| # | role | message (one line) | material |
|---|------|--------------------|----------|
| 1 | title | Constellation — decks from patterns, not from scratch | — |
| 2 | content | *Before:* every deck starts at slide zero, again | the 11pm-before-the-demo feeling |
| 3 | content | Your old decks are a pattern library nobody reads | orion-sample PATTERNS.md excerpt |
| 4 | section | *After:* the pipeline | — |
| 5 | content | analyze — a script extracts facts, an agent finds the archetypes | structure.json snippet |
| 6 | content | templatize — archetypes become reusable templates + a design guide | library/templates/ + orion.theme.json |
| 7 | content | compose — idea × pattern × theme → final .pptx | build.py green run output |
| 8 | demo | *Bridge:* watch a deck assemble itself | this deck: library/decks/constellation-intro/ builds from its own brief |
| 9 | closing | Stop drawing stars one by one — name the constellation | repo link |

## OPEN
- OPEN: slide 8's live demo works (the deck composes itself) but the orion templates are synthetic — patterns from a real deck would make the visual payoff land harder.

> Composed: `library/decks/constellation-intro/deck-spec.json` (the `compose`
> skill's worked example — slides 4 and 8 are marked stretches; `section` and
> `demo` have no evidence-backed template yet).
