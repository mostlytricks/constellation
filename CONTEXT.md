# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- **`ideate` skill built** (earlier today): pure elicitation, strawman-first, per-slide roles; worked example `library/ideas/constellation-intro/IDEA.md`.
- **`.gravity/` adopted (v1.8):** protocol card embedded, `DECK-SPEC.md` → `.gravity/deck-spec/SPEC.md` via `git mv` (Gate line added; references in both SKILL.mds + build.py fixed), root CLAUDE.md now carries the Doc Map + router table. `check.py consistency` 0 fails (MISSION/PLAN absent by choice), `check.py spec` OK, smoke loop still green. **Uncommitted — staged for review.**
- **Pipeline completed — all 4 skills exist.** `templatize` (patterns → text-free template JSONs + theme tokens; orion worked example) and `compose` (agent writes deck-spec, `build.py` renders + verifies) shipped. The **deck-spec seam is defined v0** at `.claude/skills/DECK-SPEC.md`, enforced by `build.py` (refuses unmarked stretches, unfilled text boxes, dead references — negative-tested). Worked example: **constellation-intro composes itself** from its own brief (9 slides, round-read green; full circle proven by re-running `extract.py` on the output — geometry/censuses match the templates exactly).

## Current State
- Machine complete, evidence synthetic. All templates/theme derive from the orion-sample fixture; deck-spec v0 is explicitly provisional (`spec_version` bumps when real evidence revises it). Both smoke loops in CLAUDE.md **Test** green.
- Known fidelity gaps (OPEN in DECK-SPEC/theme): theme-inherited fonts/colors unread (master XML), bullets are literal `• ` prefixes, no picture/table/chart box kinds yet.
- Privacy wall extended: rendered `.pptx` under `library/decks/` git-ignored; deck-spec.json committed as source.

## Next Step
- Run `analyze` on a **real deck** (drop into `fixtures/` — git-ignored; they live on the work machine). Real evidence fixes the archetype schema, revises deck-spec v0→v1, and replaces the synthetic templates with earned ones.

---
