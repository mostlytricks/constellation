# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- Project scaffolded, identity docs written, repo `mostlytricks/constellation` created (public) + pushed.
- **`analyze` skill built end-to-end:** `extract.py` (deterministic facts → JSON) + SKILL.md (agent interprets → PATTERNS.md), venv + python-pptx, synthetic fixture (`fixtures/make_fixture.py`, 6 slides with a deliberate 3× archetype + Korean UTF-8 check), smoke loop green, worked example committed at `library/analysis/orion-sample/`.

## Current State
- Runs locally: smoke loop in CLAUDE.md **Test** passes; Korean text survives the dump (UTF-8, verified in-file).
- Privacy wall in `.gitignore`: real decks + their analysis never committed; only the synthetic orion-sample output is whitelisted.
- Skills remaining: `ideate`, `templatize`, `compose` — all unbuilt. Deck-spec seam still undefined (OPEN in CLAUDE.md).
- Known extractor gap: theme-inherited fonts/colors reported as `(inherit)` — master/theme XML not read yet (OPEN in orion-sample PATTERNS.md).

## Next Step
- Run `analyze` on a **real deck** (user supplies 1–2 `.pptx` fixtures) — the real test of stage-2 interpretation, and the evidence that defines the deck-spec schema before `templatize` is built.

---
