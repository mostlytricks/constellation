# Constellation Studio — Design language

This is the canonical visual and interaction contract for the Studio
application. Deck previews retain their own template and theme styling; these
rules govern the workbench around them.

The shared-model architecture invariant is owned by `.gravity/MISSION.html` §04. This document applies it to the UI without redefining the presentation seam.

## Design thesis

Constellation Studio is an **observatory workbench, not a space-themed
dashboard**. The metaphor appears through structure—nodes, paths, evidence,
and alignment—not decorative stars or science-fiction effects.

The interface should feel like a professional development environment for
presentations: calm, precise, information-dense, keyboard-friendly, and honest
about what the system knows.

## Principles

1. **Workbench, not dashboard.** Prefer persistent tools, inspectors, source views, and resizable panes over card grids and page-sized forms.
2. **Evidence stays visible.** Validation, provenance, privacy, unsupported constructs, `OPEN:` items, and template stretches never disappear behind a success message.
3. **One artifact, many lenses.** Guided forms, raw source, diffs, preview, and structure views operate on the same selected artifact and draft state.
4. **Preview before consequence.** Build, export, and template promotion follow an explicit preview and approval gate.
5. **Human authority is explicit.** Agent suggestions create reviewable drafts; they do not silently overwrite files or promote templates.
6. **Calm density.** Compact spacing and strong hierarchy are welcome; visual noise is not. The deck canvas receives the strongest emphasis.
7. **Files remain legible.** UI concepts map clearly to briefs, analyses, templates, themes, deck specs, builds, and diagnostics.

## Application structure

The default wide-screen workbench has five persistent zones:

```text
┌──────────── Project · breadcrumb · command · mode · run state ────────────┐
│ Orbit rail       │ Storyboard + stage                │ Context inspector  │
│ Pipeline         │ Strip, preview, source, diff      │ Props, diagnostics │
│ Artifacts        │                                   │ Provenance         │
├──────────────────┴───────────────────────────────────┴────────────────────┤
│ Evidence drawer · validation · run log · privacy · outputs · timing       │
└───────────────────────────────────────────────────────────────────────────┘
```

- **Top bar — 48 px.** Project, artifact breadcrumb, command palette, Guided/Developer mode, theme, and run state.
- **Orbit rail — 248–280 px.** Workflow stages and artifact tree; collapses to a 48 px activity rail.
- **Stage — flexible.** Storyboard strip plus preview, editor, comparison, or structure view.
- **Inspector — 336–384 px.** Contextual properties, diagnostics, and provenance.
- **Evidence drawer — 180–300 px.** Resizable events, validation, privacy findings, and outputs.
- Panel headers are 40 px. Pane sizes persist locally.
- Shared pane borders express hierarchy; routine sections are not floating cards.

Primary product surfaces are **Workbench**, **Library**, and **Runs**. Template
Lab is a focused workflow inside the Workbench, not another visual system.

## Workflow grammar

The Orbit rail exposes a reviewable sequence:

`Source → Evidence → Draft → Preview → Approval → Build`

Each node carries one textual state: `ready`, `running`, `review`, `blocked`,
`passed`, `failed`, or `stale`. Color reinforces the label but never replaces
it.

Template Lab follows:

`Analyze → Draft template/theme → Preview against evidence → Approve diff → Commit`

A committed template must be visually distinct from a draft. Promotion always
shows the file diff, privacy result, validation result, and affected dependents.

## Guided and Developer modes

Guided and Developer are synchronized lenses over the same artifact,
selection, draft buffer, undo history, and validation model. Changing modes
preserves the selected slide and field.

### Guided

- Storyboard-first authoring with plain-language labels.
- Structured controls for roles, templates, fills, theme tokens, and content.
- Progressive disclosure for geometry, identifiers, and raw values.
- Errors identify the problem, artifact, and correction path.
- Suggested fixes remain previews until accepted.

### Developer

- Dense split editor and preview.
- JSON and Markdown with schema completion, pointer-aware diagnostics, formatting, go-to-definition, and diffs.
- Structure tree for slides, boxes, tokens, references, and unsupported source objects.
- Build log, resolved values, timings, provenance, and generated metadata.
- Invalid source may remain in a draft buffer, but cannot build or commit.
- Applying raw edits shows a staged diff; files are not rewritten on every keystroke.

Developer mode is a first-class lens, not a hidden “advanced” disclosure.

## Visual grammar

- Base spacing unit: **4 px**; common steps are 4, 8, 12, 16, 24, and 32 px.
- Control radius: **4 px**; menu/panel: **6 px**; dialog: **8 px**.
- Shadows are reserved for menus, dialogs, and dragged items. Panes use borders and surface color.
- Icons use one 16 px outline family at approximately 1.5 px stroke. Emoji are not interface icons.
- Headings use sentence case. Uppercase is limited to short machine-state labels.
- No glass effects, ambient gradients, glowing borders, or starfield backgrounds.
- The constellation motif appears only in the Orbit rail, dependency paths, and product mark.

## Typography

| Role | Font | Notes |
|---|---|---|
| Interface | **Geist Sans** | Bundle for the application; `Pretendard Variable` is the Korean fallback |
| Code and identifiers | **Geist Mono** | Paths, JSON, geometry, timings, and tabular numbers |
| Deck preview | **Deck theme** | Studio fonts must never leak into presentation content |

```css
--font-interface: 'Geist Sans', 'Pretendard Variable', sans-serif;
--font-mono: 'Geist Mono', ui-monospace, monospace;
```

- Base UI text: **13/20 px**.
- Supporting text: **12/18 px**.
- Compact metadata: **11/16 px**.
- Section title: **14/20 px**, weight 600.
- Workspace title: **18–20 px**, weight 600.
- Monospace is for source, paths, identifiers, geometry, and timings—not ordinary labels.

## Semantic color tokens

Dark is the initial presentation; light is a complete theme rather than a
mechanical inversion. The preview matte is independent of application theme.
Components consume semantic tokens only—literal color values belong in the
theme definitions below, not component styles.

| Token | Dark | Light | Purpose |
|---|---:|---:|---|
| `--canvas` | `#0B0D12` | `#F3F5F8` | Application background |
| `--surface-1` | `#11151C` | `#FFFFFF` | Primary panes |
| `--surface-2` | `#171C25` | `#F8F9FB` | Editors and raised regions |
| `--surface-active` | `#202735` | `#E9EDF3` | Selected rows and active tools |
| `--border-subtle` | `#2B3442` | `#D8DEE8` | Pane and row separators |
| `--border-strong` | `#445064` | `#ABB6C6` | Emphasized boundaries |
| `--text-primary` | `#F3F6FA` | `#151922` | Primary content |
| `--text-secondary` | `#B1BAC7` | `#4B5565` | Supporting content |
| `--text-muted` | `#7E899A` | `#6E7888` | Metadata |
| `--action-fill` | `#4E5CCB` | `#4B57C8` | Primary action |
| `--action-hover` | `#5D6CDE` | `#3945AE` | Primary action hover |
| `--on-action` | `#FFFFFF` | `#FFFFFF` | Text on primary action |
| `--link` | `#9BA9FF` | `#3444B8` | References and links |
| `--focus-ring` | `#B4A5FF` | `#6855D9` | Keyboard focus |
| `--info` | `#73C7E8` | `#136B8A` | Information |
| `--success` | `#56D49B` | `#157A55` | Passed gate |
| `--warning` | `#F0C36A` | `#8A5B00` | Warning or `OPEN:` |
| `--danger` | `#FF7A83` | `#B42332` | Failure or destructive action |
| `--stretch` | `#C4A7FF` | `#6D42B8` | Intentional template stretch |
| `--privacy` | `#FF8AC6` | `#A52669` | Privacy-sensitive evidence |
| `--selection` | `#253154` | `#E5E9FF` | Selected source or scene object |

Status always combines label, icon, and color. A status hue is never reused as
a generic decorative accent.

## Signature components

### Orbit rail

A compact pipeline and artifact navigator. Nodes expose state, elapsed time,
inputs, outputs, and blockers. Connecting lines communicate dependency only.

### Storyboard strip

Slide thumbnails show slide number, role, template, and validation state.
Keyboard reordering, multi-select, and comparison cannot obscure the canvas.

### Scene stage

The canonical preview surface. It can overlay box IDs, safe margins, overflow,
unsupported objects, and source evidence. The Stage consumes the resolved scene owned by the core and must not introduce a parallel preview model.

### Spec lens

One synchronized inspector for Guided fields, source, resolved values, and
diffs. Selecting a diagnostic focuses the exact slide, box, field, or pointer.

### Gate bar

A persistent summary above build/export: validation, stretches, `OPEN:` items,
privacy, stale preview state, and approval. A blocked action explains why next
to the disabled control.

### Evidence drawer

A structured event stream rather than a terminal imitation. Events filter by
stage and severity and link to the responsible artifact. Raw logs remain
available in Developer mode.

## Motion

| Use | Duration |
|---|---:|
| Micro-feedback | 80 ms |
| Selection and panel transition | 140 ms |
| Drawer and dialog transition | 220 ms |

Use `cubic-bezier(.2, .8, .2, 1)`. Active runs may use one restrained opacity
pulse on the active Orbit node. Errors appear immediately. Reduced-motion mode
removes transforms, animated paths, and pulses.

## Accessibility

- Target WCAG 2.2 AA.
- Every operation is keyboard reachable; focus remains visible across pane boundaries.
- Resizers expose separator semantics and keyboard adjustment.
- Job updates use polite live announcements; only unrecoverable failures interrupt.
- Slide thumbnails have meaningful accessible names.
- Scene Stage has a parallel structure outline so content is inspectable without reading pixels.
- Support editor screen-reader mode, 200% zoom, forced colors, Korean IME composition, and CJK fallback without clipped controls.
- Dialogs restore focus to their invoking control.

## Responsive behavior

- **≥1440 px:** all five workbench zones may stay visible.
- **1100–1439 px:** Orbit rail collapses; inspector or Evidence drawer may be pinned, not both by default.
- **768–1099 px:** storyboard and inspector become edge drawers; Stage remains primary.
- **<768 px:** review, approval, diagnostics, and run monitoring remain supported; geometry editing opens full-screen.
- Pointer targets are at least 32 px in dense desktop mode and 44 px for touch layouts.

## Safe to change versus identity

**Safe to change:** minor palette tuning inside semantic roles, radii within the
defined scale, exact glyphs inside the selected icon family, and timings within
the motion scale.

**Identity:** evidence-first workbench structure, synchronized Guided/Developer
lenses, restrained graphite atmosphere, compact typography, semantic status
language, visible Gate bar, and one Scene Stage shared with export semantics.

## Adding UI checklist

1. Use semantic variables, not color or font literals in components.
2. Confirm Guided and Developer views change the same draft state.
3. Keep provenance, privacy, unsupported constructs, and validation reachable.
4. Verify dark/light themes, keyboard operation, 200% zoom, reduced motion, and Korean IME.
5. Do not enable build, export, commit, or promotion without the relevant Gate state.
6. Read the copy aloud; replace vague “magic,” “generate,” or “optimize” language with domain terms.

## Anti-patterns

- Generic premium glass cards, neon gradients, excessive rounding, or starfield decoration.
- A metrics-card homepage when the user needs an artifact workbench.
- Separate renderers or state models for preview and export.
- Silent autopilot, automatic promotion, or implicit file writes.
- Success toasts that hide warnings, stretches, or `OPEN:` material.
- Raw JSON as the only authoring path, or Guided mode that cannot reveal source.
- Color-only status, unlabeled icons, emoji controls, or spinner-only waits.
- Modal workflows for routine inspection.
- Global output paths or assumptions that only one run exists.
- Hiding diagnostics because a build technically completed.
