# CONTEXT — constellation

Last touched: 2026-07-12

## Completed
- **cp949 console crash fixed** (this session; `.gravity/deck-spec/PLAN.cp949.md` ✓): the bug you hit on the other machine — Python inherits the Korean-Windows console codepage, and printed deck data (`—`, `▪`, Hangul) crashed the scripts. All five scripts now reconfigure stdout/stderr to UTF-8 at entry; repro proven red→green; cp949 regression line added to the gate. Optional machine belt: `setx PYTHONUTF8 1`.
- **`v0.2.1` cut and pushed.** Consolidated the two parallel work streams onto `main` (github v0.2.0 line — five skills, seam v1, KR write-half, `storyline`, title-grammar census — plus the local codex four-doc/Studio work), resolved the four-doc-pipeline doc collision, and released it as `v0.2.1`. Also backfilled the missing `v0.2.0` tag at `f6416db`. `main` + tags `v0.2.0`/`v0.2.1` pushed to origin; safety branch `codex-local-wip` deleted.
- **Studio adopted as a *planned* future domain.** constellation stays a Claude Code skill set now, with a professional local Studio as a later shape behind the evidence gate. `.gravity/studio/PLAN.mvp.md` + `.gravity/DESIGN.md` in place, `studio ○` wired into MISSION §04 / the IMPLEMENTATION_PLAN spine / the Doc Map; deck-spec real-deck-evidence intake plan and the full-circle `fixtures/verify_roundtrip.py` added to the gate.

## Current State
- Five skills, seam v1, two theme families, machine green (all gate loops + full-circle verifier + `check.py` 0 fails **0 warnings** — `/sync-gravity` ran: card re-copied + stamp v2.4, judgment checklist clean, nothing to retrofit). The roadmap lives in `.gravity/IMPLEMENTATION_PLAN.md`. `deck-spec` is still on synthetic evidence; `studio` is intent-only, no runtime.
- Known doc drift, user's call (reported, not fixed): CHANGELOG footer links not updated at the v0.2.1 cut (no `[0.2.1]` line, `[Unreleased]` compares from v0.2.0); `PLAN.real-deck-evidence.md` still says "v1" where the queue says real evidence mints v2. PROJECTS.md adoption row (local-only) still shows the old stamp.

## Next Step
- Take the `now` slice: drop a real deck into `fixtures/` (office machine) and run `analyze` to begin earning deck-spec v2 evidence.

---
