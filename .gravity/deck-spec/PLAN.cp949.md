# deck-spec — PLAN.cp949

Status: ✓ shipped

## Goal

Scripts must never crash on a cp949 (Korean Windows) console. File IO already
declares UTF-8 everywhere; **console** output doesn't — Python inherits the
console's legacy codepage, and any printed character outside cp949 (em-dashes,
`▪`, deck symbols) raises `UnicodeEncodeError`. Same bug the workspace fixed
in `patch_slice.py`/`check.py` (gravity v2.3); same fix applied project-wide.

## Scenario (bug intake — currently false)

- given a cp949 console (`PYTHONIOENCODING=cp949` simulates it), when `extract.py fixtures/meridian-pitch.pptx` prints its dump to stdout → **exits 0 with UTF-8 output** (today: `UnicodeEncodeError` on `—`, exit 1 — the repro).
- given the same console, when any script prints an error interpolating deck data (Hangul fills, `▪` census keys) → the message renders, never a second crash masking the first.

## Slice

- **[MODIFY]** `.claude/skills/analyze/extract.py`, `.claude/skills/compose/build.py`, `fixtures/verify_roundtrip.py`, `fixtures/make_fixture.py`, `fixtures/make_meridian_fixture.py` — reconfigure stdout/stderr to UTF-8 at entry (check.py's exact pattern: `reconfigure(encoding="utf-8", errors="replace")` guarded for non-reconfigurable streams).
- **[MODIFY]** `.gravity/IMPLEMENTATION_PLAN.md` gate — add the cp949 regression line so the scenario keeps a named wall.

## Verification

1. Red first: `PYTHONIOENCODING=cp949 .venv/Scripts/python .claude/skills/analyze/extract.py fixtures/meridian-pitch.pptx > /dev/null` — exits 1 pre-fix (proven 2026-07-12), exits 0 post-fix.
2. Full gate (all loops + full-circle verifier) — green, byte-identical outputs.
3. `check.py consistency` + `spec` — 0 fails.

## Open questions

- OPEN: machine-level belt: setting `PYTHONUTF8=1` (Python UTF-8 mode) on the Windows machines makes *all* Python tools default to UTF-8 — recommended, but scripts must not rely on it (this slice makes them self-sufficient).

## Next

Shipped — repro red pre-fix (`UnicodeEncodeError` on `—`, exit 1), green
post-fix; full gate + checkers 0 fails; the cp949 gate line is the named
regression wall. Machine-side belt (user's option): `setx PYTHONUTF8 1`.
