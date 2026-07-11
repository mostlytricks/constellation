# PATTERNS — meridian-pitch.pptx

> Second worked example of the `analyze` skill — a synthetic **consultant-mood
> financial pitch** (`fixtures/make_meridian_fixture.py`, all content fictional),
> built to exercise theme extraction, real bullet XML, and graphic frames.
> Every claim cites slide numbers from `structure.json` alongside this file.

Deck: 11 slides, 16:9 (aspect 1.778), single master, theme **"Meridian"**
(custom — not Office defaults; see the dump's `themes` section).

## Slide archetypes

| Archetype | Slides | Signature |
|---|---|---|
| **A — kicker-headline-content** | 2, 4, 5 (variant: 10) | `Blank` · 7 shapes: kicker (x 4.5, y 6.0, 90.8×4%) + action headline (y 10.7, h 12%) + gold rule (x 4.5, y 23.3, 9×0.4%, solid `C9A227`) + bullet body (y 28.0, h 57.3%) + source line (y 88.7) + footer pair (y 94.7: confidential string w 45% left, page number x 92.3 right). Slide 10 adds a `F2F4F7` panel (y 66.7, h 17.3%) over a shortened body — 8 shapes. |
| **B — exhibit** | 7, 8 | Archetype A's scaffold with a **graphic frame** in the body zone instead of bullets: a 4×6 table (slide 7, y 29.3, 90.8×32%) / a COLUMN_CLUSTERED chart (slide 8, y 28.0, 86.3×57.3%). |
| **C — numbered divider** | 3, 6, 9 | `Blank` · 4 shapes: full-bleed navy bg (`0B2340`) + section number (x 4.5, y 32.0, 60pt) + gold rule (y 47.3) + section title (y 50.0, 32pt). |
| *(singletons)* | 1 (cover), 11 (closing) | Cover: navy full-bleed + rule + title stack. Closing: `Title Slide` layout placeholders, styling theme-inherited. |

Geometry within each archetype is **identical across its slides** — the same
hard-grid property orion-sample had, now at consulting-deck complexity.

## Visual grammar

From the deck-wide censuses:

- **Kicker:** 11 pt bold gold `C9A227`, ALL CAPS — 6 runs, one per A/B slide (2, 4, 5, 7, 8, 10).
- **Action headline:** 24 pt bold **Georgia** navy `0B2340` — 6 runs, same slides. Full-sentence "so-what" titles, consultant style.
- **Body:** 14 pt Arial ink `3B4652` — 11 runs (slides 4, 5, 10); the exec summary (slide 2) runs 15 pt.
- **Meta text:** 9 pt italic mute `8A94A0` sources (6×) + 8 pt mute footers (12×) — `8A94A0` totals 19 runs, all wayfinding/citation, never content.
- **Divider voice:** 60 pt Georgia gold number + 32 pt Georgia white title (slides 3, 6, 9).
- **Gold does three jobs:** kicker text (6×), rule fills (10×: under every headline, on every divider, on the cover), divider numbers (3×) — one accent, used as punctuation, never decoration.
- **Two-font system:** Georgia = display (13 runs: headlines, divider numbers/titles, cover), Arial = everything else (43 runs). Matches the theme's font scheme exactly (major = Georgia, minor = Arial).
- **Theme-inherited:** 2 runs `(inherit)` — the closing placeholders (slide 11). The `themes` section resolves the chain: title → `titleStyle` lvl1 = 44 pt, `+mj-lt` → **Georgia**, `scheme:tx1` → `dk1` `000000`.

## Bullets (first deck with real bullet XML)

- `char:▪` — 11 paragraphs (slides 4, 5, 10): true `buChar` with hanging indent.
- `autonum:arabicPeriod` — 4 paragraphs (slide 2): the exec summary is *numbered*, signaling sequence.
- `none` — 12 paragraphs: kickers and headlines explicitly suppress bullets.
- `(inherit)` — 45: table cells, sources, footers, dividers, cover — prose boxes that never state a bullet.

## Grid

The A/B scaffold (exact across slides 2, 4, 5, 7, 8, 10):

- Left rail: **4.5%** (everything aligns to it; no second indent level)
- Kicker band: y **6.0%** · headline band: y **10.7%**, h 12% · rule: y **23.3%**
- Body zone: y **28.0%**, h 57.3% (exhibits sit inside it)
- Source: y **88.7%** · footer: y **94.7%**
- Divider stack: number y 32.0% · rule y 47.3% · title y 50.0%

## Template candidates

1. **kicker-headline-content** (archetype A, 3× + variant) — the workhorse; generalize first.
2. **numbered-divider** (archetype C, 3×) — small, exact, high reuse.
3. **exhibit** (archetype B, 2×) — recurs, but its body is a graphic frame: **deck-spec v0 has no table/chart box kind**, so it cannot be a buildable template yet. This is the concrete evidence the SPEC's box-kind OPEN predicted.

## OPEN

- ~~OPEN: archetype B blocked on v1 box kinds; right-align/caps/italic inexpressible~~ — closed by **deck-spec v1** (`.gravity/deck-spec/PLAN.v1.md`): `exhibit-table` + `exhibit-chart` templates now exist, and `right` align / `caps` / `italic` / `bullet_char` are theme/template facts.
- OPEN: the numbered exec summary (slide 2, `buAutoNum`) still has no deck-spec content kind — bullets-only in v1.
- OPEN: slide 11's subtitle placeholder chain stops at the master (`bodyStyle` lvl1 = 32 pt) — the `Title Slide` *layout* may override it, and the dump doesn't walk layout-level styles.
