# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- **Second evidence base + meridian family**: consultant-pitch fixture (`fixtures/make_meridian_fixture.py`) run through the full pipeline — second analyze worked example, `kicker-headline-content` + `numbered-divider` templates, `meridian` theme, verification deck.
- **deck-spec v0→v1 shipped** (this session; slice: `.gravity/deck-spec/PLAN.v1.md`): `build.py` renders `table` + `chart` box kinds, `right` align, `caps`/`italic` style keys, and real `buChar` bullets (`tokens.bullet_char`); v0 specs refused with a naming error. The meridian exhibit archetype is now templated (`exhibit-table`, `exhibit-chart`) and exercised by two new meridian-demo slides. Negative tests (v0 spec, ragged table, short chart series) all refused; full circle geometry-exact with `char:▪` bullets and both graphic frames round-tripping.

- **`storyline` skill shipped** (this session): the mood-and-flow interviewer for single pitches — stakes, skeptic's seat, action-title pass, mood curve, ghost-deck read-back; upgrades IDEA.md in place. ideate/compose wired (handoff + honor-the-mood rule, new `summary`/`exhibit`/`ask` roles); worked example `library/ideas/meridian-pitch/IDEA.md`.

## Current State
- **Five skills** (ideate · storyline · analyze · templatize · compose); seam at **v1** (still provisional — synthetic evidence only: orion + meridian). Three template families, two themes, all committed deck-specs on v1, machine green end-to-end.
- Every fidelity gap the synthetic evidence could close is closed. Remaining OPENs (SPEC): numbered-list content kind (`buAutoNum`, meridian slide 2), `picture` box kind, layout-level style walking in `extract.py` — all waiting on real-deck evidence.
- Real decks are on the **office machine** — blocked until the user is there.

## Next Step
- Run `analyze` on a **real deck** (drop into `fixtures/` on the office machine — git-ignored). That evidence decides v1→v2 (pictures, numbered lists, multi-master) and replaces synthetic templates with earned ones.

---
