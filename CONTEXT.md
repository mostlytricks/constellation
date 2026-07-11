# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- **v0.2.0 cut and merged** (PR #1 → `main`). ⚠ Tag `v0.2.0` still needs a local push — the remote session token can't push tag refs: `git tag -a v0.2.0 -m "v0.2.0" f6416db && git push origin v0.2.0`.
- **Four-doc pipeline adopted** (this session): `.gravity/MISSION.html` + `.gravity/IMPLEMENTATION_PLAN.md` authored and wired; checkers 0 fails, 0 warnings. Plus the **title-grammar census** in `analyze` stage 2.
- **KR write-half shipped** (this session; `.gravity/deck-spec/PLAN.kr.md` ✓): `font_ea` style key (additive to v1) writes `a:ea` typefaces, `fonts_ea` census reads them; meridian carries Malgun Gothic; Korean worked example `library/decks/byeoljari-demo/` — Hangul round-trips intact, geometry 4/4, all 24 runs `Malgun Gothic`.

## Current State
- Five skills, seam v1, two theme families, machine green. The roadmap now lives in `.gravity/IMPLEMENTATION_PLAN.md` (slice queue + locked decisions) — read it, not this file, for what's next beyond the immediate step.
- Branch restarted from merged `main`; new work rides `claude/constellation-gravity-release-i64nqq` again.

## Next Step
- On the office machine: push the `v0.2.0` tag (command above), then take the `now` slice from the slice queue — drop a **real deck** into `fixtures/` and run `analyze`.

---
