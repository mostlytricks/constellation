# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- **Read-side fidelity pass shipped**: `extract.py` parses master/theme OOXML (per-master `themes` section + `bullet_census`), SKILL rule updated, OPEN lines narrowed to the write side. Both smoke loops + full circle green. (v0.1.0 itself is tagged and on `main`; see `CHANGELOG.md`.)
- **Second evidence base: the consultant pitch** (this session): `fixtures/make_meridian_fixture.py` — synthetic 11-slide, 16:9 financial pitch with a rewritten theme (custom colors, Georgia/Arial), real `buChar`/`buAutoNum` bullets, a table, a chart. Ran the full pipeline on it: analyze (second worked example, `library/analysis/meridian-pitch/`) → templatize (`kicker-headline-content` + `numbered-divider` + `meridian` theme) → verification build (`library/decks/meridian-demo/`, zero stretches, full-circle geometry-exact). Privacy grep clean.

## Current State
- Two template families (orion 4:3, meridian 16:9), two themes, machine green end-to-end. The new extraction features are all exercised: theme census shows the custom "Meridian" scheme, bullet census caught all four kinds, `(inherit)` runs resolve via the dump.
- **deck-spec v1 pressure is now concrete** (SPEC OPEN, cited): the meridian exhibit archetype (table/chart, 2×) is a real template candidate v0 cannot express — `table`/`chart` box kinds are v1's first candidates, plus right-`align`/`caps`/`italic` style keys and `buChar` writing in `build.py`.
- Evidence still synthetic — meridian is consultant-*shaped*, not consultant-*sourced*. It sharpens the schema questions; only a real deck answers them.

## Next Step
- Run `analyze` on a **real deck** (drop into `fixtures/` on the work machine — git-ignored). Decide deck-spec v0→v1 (box kinds + style keys) from that evidence *plus* the meridian OPEN list, bumping `spec_version`.

---
