# PATTERNS — orion-sample.pptx

> Worked example of the `analyze` skill's stage-2 output. Source: the synthetic
> fixture (`fixtures/make_fixture.py`), extracted to `structure.json` alongside
> this file. Every claim cites slide numbers from that dump.

Deck: 6 slides, 4:3 (aspect 1.333), single master.

## Slide archetypes

| Archetype | Slides | Signature |
|---|---|---|
| **A — accent-headline content** | 3, 4, 5 | `Blank` layout · 3 shapes: title textbox (x 5.0, y 5.3, 90×12%) + body textbox (x 8.0, y 21.3, 84×60%) + full-width accent bar (x 5.0, y 92.0, 90×2%, solid `2E5CFF`) |
| **B — title/closing bookend** | 1, 6 | `Title Slide` layout · 2 placeholders (CENTER_TITLE + SUBTITLE), all styling theme-inherited |
| *(singleton)* | 2 | `Title and Content` layout · agenda bullets — recurs only once, not a template candidate |

Geometry within archetype A is **identical across all three slides** — this is a
hard grid, not a loose family.

## Visual grammar

From the deck-wide censuses:

- **Heading:** 32 pt, bold, accent `2E5CFF` — exactly 3 runs, one per archetype-A slide (slides 3–5).
- **Body:** 18 pt, `333333` — 9 runs, three bullets per archetype-A slide.
- **Accent color role:** `2E5CFF` appears as heading text (3×) *and* as the footer bar fill (slides 3–5) — one color, two jobs: emphasis + wayfinding.
- **Theme-inherited:** 8 runs `(inherit)` — all on the placeholder slides (1, 2, 6). The dump's `themes` section resolves them: titles inherit `titleStyle` lvl1 (44 pt, `scheme:tx1` → `dk1` `000000`, `+mj-lt` → Calibri), body placeholders inherit `bodyStyle` (32/28/24 pt by level, same color/font chain).

## Title grammar

Content-bearing slides (2–5): **0 claims, 4 labels** ("Agenda", "Pillar One:
Extraction", …) — teaching-deck grammar: titles name topics, the bullets carry
the content. Contrast with meridian-pitch (6/6 claims): the census separates
lecture decks from pitch decks at a glance.

## Grid

Recurring positions (archetype A, exact across slides 3–5):

- Left margin: **5.0%** (title, bar) / **8.0%** (body — indented one step)
- Title band: y **5.3%**, height 12%
- Body block: y **21.3%**, height 60%
- Footer bar: y **92.0%**, height 2%

## Template candidates

1. **accent-headline content** (archetype A, 3×) — the deck's workhorse; generalize first.
2. **title/closing bookend** (archetype B, 2×) — thin: it's just the theme's own Title Slide layout; the template is the theme, not the deck.

## OPEN

- ~~OPEN: theme-resolved fonts/colors invisible to the extractor~~ — closed: `extract.py` now dumps the per-master `themes` section (color/font scheme, color map, master text styles), so `(inherit)` runs resolve from the dump (see Visual grammar above). Still open for `templatize`: whether templates should bake resolved values or keep "inherit from theme" as a token.
- OPEN: all 23 paragraphs report bullet `(inherit)` because the fixture writes literal `• ` prefixes (no `buChar`) — matching the compose-side bullet gap in `.gravity/deck-spec/SPEC.md` OPEN. A real deck with true bullet XML is the first interesting test of `bullet_census`.
