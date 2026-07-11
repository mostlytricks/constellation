# deck-spec — PLAN.kr

Status: ✓ shipped (write half; cp949 legacy half stays in the queue's `later` lane)

## Goal

Prove the pipeline round-trips Korean end to end and give the seam an
East-Asian font channel: today `build.py` writes only the latin typeface
(`a:latin`), so Hangul runs render on fallback fonts — a KR deck loses its
typography. Pulled forward from the `later` lane: it's the one slice that
needs no real deck (MISSION first wedge is EN/KR).

## Scenario

- given a deck-spec with Korean fills, when `build.py` renders and the output is re-extracted → text round-trips intact and geometry matches templates (UTF-8 path proven, not assumed).
- given a theme style with `"font_ea": "Malgun Gothic"`, when a run renders → its `a:ea` typeface is set, and `extract.py`'s new `fonts_ea` census reports it (the wall that shows fallback vs. specified).
- given a v1 spec without `font_ea`, when it builds → unchanged output (the key is additive; `spec_version` stays 1).

## Slice

- **[MODIFY]** `.claude/skills/analyze/extract.py` — `font_census` gains a `fonts_ea` count (per-run `a:ea` typeface, `(inherit)` when unset) + deck aggregate: the evidence side.
- **[MODIFY]** `.claude/skills/compose/build.py` — `apply_style` writes `a:ea` when the style carries `font_ea`.
- **[MODIFY]** `library/themes/meridian.theme.json` — `font_ea: "Malgun Gothic"` on the text styles (bilingual default for the family).
- **[MODIFY]** `.gravity/deck-spec/SPEC.md` — document the optional `font_ea` style key.
- **[NEW]** `library/decks/byeoljari-demo/deck-spec.json` — a small all-Korean deck on the meridian family: the KR worked example.

## Verification

1. Build the KR demo — green, round-read verified.
2. Re-extract it: Hangul previews intact, geometry matches templates exactly, `fonts_ea` census shows `Malgun Gothic` on styled runs.
3. Rebuild the EN decks — byte-path unchanged for specs without `font_ea` styles… (meridian gains the key, so EN decks now carry `a:ea` too — harmless; constellation-intro/orion unaffected). Gates + checkers green.

## Open questions

- OPEN: cp949 *legacy files* (the other half of the CLAUDE.md gotcha) still need a real legacy deck — extraction-side; stays in the `later` lane.

## Next

Shipped — KR demo builds green; re-extraction: geometry 4/4 exact, Hangul
previews intact, `fonts_ea` = `Malgun Gothic` on all 24 runs. cp949 legacy
half waits for a real legacy deck (queue `later`).
