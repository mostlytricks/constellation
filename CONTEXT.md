# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- **v0.1.0 released** — the full four-skill pipeline + `.gravity/` adoption, tagged `v0.1.0` and merged to `main` (see `CHANGELOG.md [0.1.0]` for the contents; the tag is the anchor).
- **Read-side fidelity pass shipped** (this session): `extract.py` now parses master/theme OOXML — per-master `themes` section (color/font scheme, color map, master text styles) resolving the `(inherit)` censuses, plus per-paragraph `bullet_census`. SKILL rule updated (resolve inherits against the dump, cite the chain), worked example regenerated, SPEC/CLAUDE OPEN lines narrowed to the *write* side. Both smoke loops + full circle green (9/9 slides geometry-exact vs templates).

## Current State
- Machine complete and now **theme-sighted**, evidence still synthetic. Real-deck analysis is no longer blind to inherited styling — the two extraction blockers named against it are closed.
- Remaining fidelity gaps (OPEN in SPEC): `build.py` writes bullets as literal `• ` prefixes (no `buChar` authoring); no picture/table/chart box kinds; extractor doesn't walk layout-level overrides (masters/themes only).
- Privacy wall unchanged: `fixtures/*.pptx` + `library/analysis/` git-ignored except the orion worked example; rendered decks git-ignored, deck-spec.json committed.

## Next Step
- Run `analyze` on a **real deck** (drop into `fixtures/` on the work machine — git-ignored). Real evidence fixes the archetype schema, revises deck-spec v0→v1, and replaces the synthetic templates with earned ones. The `themes` + `bullet_census` sections now make that evidence readable.

---
