# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- **`analyze` skill built end-to-end:** `extract.py` (deterministic facts → JSON) + SKILL.md (agent interprets → PATTERNS.md); smoke loop green on the synthetic orion-sample fixture (3× archetype found, Korean UTF-8 verified); worked example committed.
- **`ideate` skill built:** pure elicitation skill (strawman-first, five themes, named arcs, per-slide **roles** — the upstream half of the deck-spec seam); worked example `library/ideas/constellation-intro/IDEA.md` (doubles as the future demo deck's brief).

## Current State
- 2 of 4 skills exist (`analyze`, `ideate`); `templatize` + `compose` unbuilt. Deck-spec seam half-defined: idea-side roles named in ideate's SKILL.md; pattern-side archetype schema waits on real-deck evidence.
- Smoke loop in CLAUDE.md **Test** passes. Privacy wall: real decks + their analysis git-ignored; only synthetic orion-sample output whitelisted.
- Extractor gap: theme-inherited fonts/colors show as `(inherit)` — master/theme XML unread (OPEN in orion-sample PATTERNS.md).
- No real `.pptx` on this machine (checked fixtures/Downloads/Desktop/Documents) — real decks presumably live on the work machine.

## Next Step
- Run `analyze` on a **real deck** the user supplies (drop into `fixtures/` — git-ignored). That evidence fixes the archetype schema and unblocks `templatize`.

---
