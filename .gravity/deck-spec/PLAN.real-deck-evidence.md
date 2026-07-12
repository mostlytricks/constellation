# deck-spec — PLAN.real-deck-evidence

Status: ◑ building

## Goal

Analyze representative private decks and create an evidence-backed change plan
for deck-spec v1. Every construct encountered must be supported, preserved as
an explicit unsupported fact, or deliberately deferred—never silently lost.

## Scenario

- given a real deck with layouts and rich objects, when `analyze` runs → the structural dump and slide-cited report expose every observed construct and every extractor gap
- given the evidence reports, when v1 is planned → each schema change cites observed slides and includes a v0→v1 migration decision
- given private source material, when a pattern is promoted → tracked templates retain reusable geometry and design knowledge without source text

## Evidence intake

- [x] Evidence-first sequencing was approved on 2026-07-12.
- [ ] Supply or approve at least one branded business deck and one professional technical deck; Korean content is preferred in one.
- [x] Private decks and their analyses remain git-ignored; only sanitized, generalized artifacts may graduate.

## Slice

- **[NEW]** `fixtures/<private-deck>.pptx` — approved, git-ignored source evidence.
- **[NEW]** `library/analysis/<slug>/structure.json` and `PATTERNS.md` — private structural facts and slide-cited interpretation.
- **[MODIFY]** `.claude/skills/analyze/extract.py` — represent facts the real fixtures prove are currently missing.
- **[NEW]** `.gravity/deck-spec/PLAN.v1.md` — evidence citations, support/defer decisions, migration shape, and named verification work.
- **[MODIFY]** `.gravity/deck-spec/SPEC.md` and renderer code only after the v1 plan is reviewed.

## Verification

1. Run `analyze` on every approved deck.
2. `[review]` Compare each deck with its dump: masters/layouts, shapes, geometry, text, pictures, tables, charts, groups, and inherited styling. Record every mismatch as `OPEN:`.
3. Confirm every encountered construct is classified in `PLAN.v1.md` as supported, explicit-unsupported, or deferred.
4. Run `git check-ignore` for every private deck and analysis artifact; confirm no source text enters tracked templates or themes.
5. Run the project gate in `.gravity/IMPLEMENTATION_PLAN.md`. Studio runtime code must still be absent.

## Open questions

- OPEN: the approved real-deck evidence set is not present on this machine.
- OPEN: whether the first v1 slice must cover every observed rich object or preserve some as explicit unsupported nodes depends on those fixtures.

## Next

Place the first approved real `.pptx` under `fixtures/` and run the `analyze`
skill; do not infer v1 fields from the synthetic fixture.

