# CONTEXT — constellation

Last touched: 2026-07-12

## Completed
- **`v0.2.1` cut and pushed.** Consolidated the two parallel work streams onto `main` (github v0.2.0 line — five skills, seam v1, KR write-half, `storyline`, title-grammar census — plus the local codex four-doc/Studio work), resolved the four-doc-pipeline doc collision, and released it as `v0.2.1`. Also backfilled the missing `v0.2.0` tag at `f6416db`. `main` + tags `v0.2.0`/`v0.2.1` pushed to origin; safety branch `codex-local-wip` deleted.
- **Studio adopted as a *planned* future domain.** constellation stays a Claude Code skill set now, with a professional local Studio as a later shape behind the evidence gate. `.gravity/studio/PLAN.mvp.md` + `.gravity/DESIGN.md` in place, `studio ○` wired into MISSION §04 / the IMPLEMENTATION_PLAN spine / the Doc Map; deck-spec real-deck-evidence intake plan and the full-circle `fixtures/verify_roundtrip.py` added to the gate.

## Current State
- Five skills, seam v1, two theme families, machine green (all gate loops + full-circle verifier + `check.py` 0 fails). The roadmap lives in `.gravity/IMPLEMENTATION_PLAN.md` — read it for what's next beyond the immediate step. `deck-spec` is still on synthetic evidence; `studio` is intent-only, no runtime.
- ⚠ Gravity protocol card is stamped `v1.8` but the workspace is now `v2.4` (`check.py` WARNs `PROTOCOL_STALE`). A real `/sync-gravity constellation` — which re-copies the card, not just the stamp — is an open follow-up.

## Next Step
- Take the `now` slice: drop a real deck into `fixtures/` (office machine) and run `analyze` to begin earning deck-spec v2 evidence. (Or clear the `PROTOCOL_STALE` warning first with `/sync-gravity constellation`.)

---
