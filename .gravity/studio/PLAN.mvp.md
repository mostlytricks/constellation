# studio — PLAN.mvp

Status: ○ planned

## Goal

After deck-spec v1 and the typed core are evidence-backed, deliver one
professional local workflow:

`import → extract → inspect → edit spec → validate → preview → build/export`

The MVP proves Guided and Developer views over the same state. Template Lab,
agent autonomy, cloud sync, and desktop packaging are outside this slice.

## Scenario

- given an approved local deck, when a user imports it → an isolated run shows extraction progress, artifacts, provenance, privacy state, and diagnostics
- given a draft deck-spec, when a user edits it in Guided or Developer view → both surfaces show the same typed state and validation results
- given an invalid spec, when validation runs → exact diagnostics appear and build remains unavailable
- given a valid spec, when preview and build run → both consume the same `SlideScene`, and the exported PPTX passes round-read verification
- given a keyboard user at desktop width, when they navigate the workbench → pipeline, storyboard, inspector, diagnostics, command palette, and source/diff views remain usable without modal churn

## Slice

- **[NEW]** `.gravity/integration/` via `/new-domain` + `/new-spec` — mint and wire the third domain immediately before frontend/backend work; its SPEC owns the OpenAPI boundary and change order.
- **[NEW]** `src/constellation/api/` — thin FastAPI/Pydantic adapter over the typed engine, with isolated run lifecycle, validation, preview, and build operations.
- **[NEW]** `studio/` — React/TypeScript/Vite workbench with resizable Pipeline, Storyboard/Preview, and Inspector panes plus an Evidence drawer.
- **[NEW]** `studio/src/features/developer/` — lazy-loaded source editor, structured diagnostics, diffs, provenance, and build log.
- **[NEW]** `studio/src/features/guided/` — schema-driven deck, slide, template, fill, and theme controls over the same draft.
- **[NEW]** Python integration tests and Studio component/E2E tests — one complete synthetic-fixture workflow and one invalid-spec path.
- **[MODIFY]** `.gitignore` — ignore `.constellation/` run state and generated Studio artifacts.

## Verification

1. Run the core/deck-spec gate; v1 must already be green.
2. Run Python API tests and Studio unit, type, and production-build checks.
3. Start Studio, import the synthetic fixture, and confirm the pipeline reaches inspect with artifacts and provenance visible.
4. Introduce a dead template reference in Developer view; expect an inline structured diagnostic and disabled build.
5. Correct it in Guided view; expect Developer source to update, preview to render, and export to pass round-read verification.
6. Assert preview and PPTX resolve identical slide order, box identity, geometry, and text from the same `SlideScene`.
7. `[review]` At 1440×900, verify dense resizable panes, dark/light themes, keyboard navigation, command palette, and visible privacy/stretch/`OPEN:`/validation badges.

## Open questions

- OPEN: which v1 fields are safe for schema-driven Guided editing?
- OPEN: should preview use client SVG or server-rendered imagery while retaining `SlideScene` as the sole input?
- OPEN: which job events belong in MVP versus a later resumable-run slice?
- OPEN: should the source editor ship in the initial bundle or lazy-load with Developer view?

## Next

Do not scaffold Studio yet. Complete
`.gravity/deck-spec/PLAN.real-deck-evidence.md`, then deck-spec v1 and the typed
core, before this slice becomes active.
