# deck-spec — PLAN.v1

Status: ✓ shipped

## Goal

Bump the seam v0→v1 on the **write side**, closing every OPEN the meridian
evidence made concrete: `table`/`chart` box kinds, `right` align and
`caps`/`italic` style keys, and real `buChar` bullet XML in `build.py` — so
the exhibit archetype becomes templatable and composers stop approximating.
(Real-deck evidence is blocked on the office machine; this is the area that
doesn't need it.)

## Scenario

- given the meridian exhibit archetype (table/chart, 2×, `library/analysis/meridian-pitch/PATTERNS.md`), when templatize generalizes it → the template builds green instead of being refused for an inexpressible box kind.
- given a theme style with `"caps": true` / `"italic": true`, when build.py renders a box bound to it → the output text is uppercased / italic without the composer editing fills by hand.
- given a `"content": "bullets"` box, when the built deck is re-extracted → `bullet_census` reports `char:` bullets, not `(inherit)` literal-prefix paragraphs.
- given a v0 spec (`"spec_version": 0`), when build.py runs → it is refused with a message naming the bump (no silent compat).

## Slice

- **[MODIFY]** `.claude/skills/compose/build.py` — accept `spec_version: 1`; render `content: "table"` (header style/fill + banding tokens) and `content: "chart"` (categories × series, `series_fill` token) boxes; `align: "right"`; `caps`/`italic` style keys; write real `buChar` bullets (`tokens.bullet_char`, default `•`) with hanging indent; extend round-read verify to graphic frames.
- **[MODIFY]** `.gravity/deck-spec/SPEC.md` — v1 shapes + shrunk OPEN list.
- **[NEW]** `library/templates/exhibit-table.template.json`, `exhibit-chart.template.json` — the meridian archetype B, now expressible.
- **[MODIFY]** `library/themes/meridian.theme.json` — `table-header`/`table-body` styles, `bullet_char: "▪"`, `caps` on kicker, `italic` on source; drop closed `open` entries. Other templates/specs: bump `spec_version`, drop closed OPENs.
- **[MODIFY]** `library/decks/meridian-demo/deck-spec.json` — add one table + one chart slide exercising the new kinds.

## Verification

1. Both smoke loops (root CLAUDE.md **Test**) — green; build.py exits non-zero on a v0 spec.
2. Full circle: `extract.py` on the rebuilt meridian-demo — geometry matches all templates exactly; `bullet_census` shows `char:▪`; table/chart shapes present.
3. `check.py consistency` + `check.py spec` — 0 fails.

## Open questions

- OPEN: numbered lists (`buAutoNum`, seen in meridian slide 2) still have no deck-spec content kind — bullets-only for v1; revisit with real-deck evidence.
- OPEN: `picture` box kind deferred until a deck provides evidence.

## Next

Shipped — verification 1–3 all green (v0/ragged-table/short-series specs
refused; full circle geometry-exact with `char:▪` bullets and both graphic
frames round-tripping; checkers 0 fails). Next slice needs real-deck evidence.
