# constellation — Implementation plan & resume sheet

> Working scenario: real-deck evidence turns the synthetic machine into an earned pattern library — and, later, a professional local Studio over the same seam.
> Branch `main` · last updated 2026-07-12.

## Status right now

v0.2.0 is cut and merged: five skills, deck-spec seam at v1, two theme families
(orion 4:3, meridian 16:9), all gates green. Everything below the `now` lane is
blocked on the same thing — real decks, which live on the office machine. The
tag `v0.2.0` still needs a local push (see CONTEXT.md).

## How to resume in a fresh session

1. Open the repo at its project dir.
2. Read this file + `CONTEXT.md` (now) + `.gravity/MISSION.html` (why, if anything feels unmoored).
3. Run the gate (below) to verify green.
4. Take the `now` slice; before touching the seam, load `.gravity/deck-spec/SPEC.md`.

## Domain status spine

The skills are the machine, not domains. Two subjects have earned a folder
(root CLAUDE.md, *Adding a domain*): `deck-spec` (shipped) and `studio`
(planned — intent fixed, no runtime yet). `○ planned · ◑ building · ✓ shipped`.

| Domain | Status | Where it stands |
|---|---|---|
| `deck-spec` | ✓ v1 shipped | `.gravity/deck-spec/SPEC.md` (v1, provisional — synthetic evidence); last slice `.gravity/deck-spec/PLAN.v1.md` ✓; v2 awaits real-deck evidence |
| `studio` | ○ planned | product + design intent fixed (`.gravity/studio/PLAN.mvp.md`, `.gravity/DESIGN.md`); a *consumer* of the seam — implementation waits behind real-deck evidence and the typed v1 core |

## Slice queue

| Lane | Slice | Domain PLAN | Status |
|---|---|---|---|
| now | **Real-deck evidence intake** — drop real decks into `fixtures/` (office machine), run `analyze`, earn templates/themes; **blocked: decks are on the office machine** | mints `.gravity/deck-spec/PLAN.v2.md` | ○ |
| next | deck-spec v2 — decided by that evidence: `picture` box kind, numbered lists (`buAutoNum`), layout-level style walking, multi-master (SPEC OPEN list) | `.gravity/deck-spec/PLAN.v2.md` (future) | ○ |
| next | Dogfood — first real pitch end-to-end: `ideate` + `storyline` → compose from earned templates | — | ○ |
| later | KR fidelity, legacy half — cp949 files need a real legacy deck (write half shipped: `PLAN.kr.md` ✓ — `font_ea` key + `fonts_ea` census + `byeoljari-demo` KR worked example) | `.gravity/deck-spec/PLAN.kr.md` | ◑ |
| later | Title-grammar wall — graduate the analyze census from `[review]` judgment to a checkable rule, if it proves useful | — | ○ |
| later | **Studio MVP** — local Guided + Developer workbench over the resolved scene; **gated: needs the typed v1 core first**, then mint `integration` as a third domain before the browser/Python boundary | `.gravity/studio/PLAN.mvp.md` | ○ |

## Locked decisions

- **Evidence over invention** — no schema change without a deck that demands it; unknowns are `OPEN:` lines (MISSION §03).
- **`build.py` is the seam's only validator** — no separate schema checker; if it builds, it's valid (SPEC *Enforcement*).
- **Breaking seam changes bump `spec_version` and old specs are refused by name** — never silent compat (v1 precedent).
- **Templates prove by building** — a template that can't pass the gate isn't minted (templatize step 5).
- **Skills ≠ domains** — `.claude/skills/` is the product; `.gravity/` folders are minted only by the is-it-a-domain gate.
- **One authoritative engine** — the planned Studio never duplicates composition or validation; it consumes the same resolved scene and defers to `build.py` (MISSION §04).
- **Studio waits for evidence** — no Studio runtime code before real-deck evidence and the typed v1 core; product/design intent may be authored now (`studio/PLAN.mvp.md`, `DESIGN.md`), implementation may not.
- **Human-reviewed consequences** — promotion, writes, and exports stay explicit; no silent autopilot in either the skills or the future Studio.

## Open questions

- OPEN: should `templatize` bake theme-resolved values into templates, or keep "inherit from theme" as a token? (orion PATTERNS OPEN — real evidence will decide.)
- OPEN: numbered lists — a `"content": "numbered"` box kind vs a per-item marker inside `bullets`? Wait for a real deck's shape.
- OPEN: does the storyline mood curve need more than one word per act once real pitches use it?

## The gate

```bash
.venv/Scripts/python fixtures/make_fixture.py
.venv/Scripts/python .claude/skills/analyze/extract.py fixtures/orion-sample.pptx -o library/analysis/orion-sample/structure.json
.venv/Scripts/python fixtures/make_meridian_fixture.py
.venv/Scripts/python .claude/skills/analyze/extract.py fixtures/meridian-pitch.pptx -o library/analysis/meridian-pitch/structure.json
.venv/Scripts/python .claude/skills/compose/build.py library/decks/constellation-intro/deck-spec.json -o library/decks/constellation-intro/constellation-intro.pptx
.venv/Scripts/python .claude/skills/compose/build.py library/decks/meridian-demo/deck-spec.json -o library/decks/meridian-demo/meridian-demo.pptx
# full-circle: re-extract a generated deck and refuse geometry/theme-token drift
.venv/Scripts/python .claude/skills/analyze/extract.py library/decks/constellation-intro/constellation-intro.pptx -o library/analysis/constellation-intro-roundtrip/structure.json
.venv/Scripts/python fixtures/verify_roundtrip.py
# gravity index + spec honesty
python ../../.claude/scenarios/check.py consistency --project .
python ../../.claude/scenarios/check.py spec --project .
```

Last green: 2026-07-12 (consolidation — all loops + full-circle verifier + `check.py consistency`/`spec` 0 fails).
