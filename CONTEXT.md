# CONTEXT — constellation

Last touched: 2026-07-12

## Completed
- **Two parallel work streams consolidated onto `main`.** The github line (v0.2.0: five skills, deck-spec seam v1, KR write-half, `storyline`, title-grammar census) plus the local codex work merged into one coherent tree. Resolved the doc collision — both sessions had independently adopted the four-doc pipeline. Pre-consolidation local snapshot preserved on branch `codex-local-wip`.
- **Studio adopted as a *planned* future domain.** Per decision, constellation stays a Claude Code skill set now, with a professional local Studio as a later shape behind the evidence gate. Folded in `.gravity/studio/PLAN.mvp.md` + `.gravity/DESIGN.md`, wired `studio ○` into MISSION §04 / the IMPLEMENTATION_PLAN spine / the Doc Map. Added the deck-spec real-deck-evidence intake plan and the full-circle `fixtures/verify_roundtrip.py` (now in the gate).

## Current State
- Five skills, seam v1, two theme families, machine green (all gate loops + full-circle verifier + `check.py` 0 fails). The roadmap lives in `.gravity/IMPLEMENTATION_PLAN.md` — read it for what's next beyond the immediate step. `deck-spec` is still on synthetic evidence; `studio` is intent-only, no runtime.
- ⚠ The `v0.2.0` git tag still needs a local push: `git tag -a v0.2.0 -m "v0.2.0" f6416db && git push origin v0.2.0`.
- ⚠ Gravity protocol card is still stamped `v1.8` (matches the actual card content). A real `/sync-gravity constellation` to the current workspace version is a separate follow-up — not folded in, because codex had only bumped the stamp line without re-copying the card.

## Next Step
- Push the consolidated `main` + the pending `v0.2.0` tag, then take the `now` slice: drop a real deck into `fixtures/` (office machine) and run `analyze` to begin earning deck-spec v2 evidence.

---
