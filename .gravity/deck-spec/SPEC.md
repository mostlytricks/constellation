# DECK-SPEC — the seam (v0, provisional)

The intermediate representation between the four skills. `ideate` produces the
brief above it, `templatize` produces the parts it references, `compose` writes
one and `build.py` renders it. **v0 is fixed by synthetic evidence only**
(orion-sample) — real-deck analysis may revise every shape here; that's expected,
bump `spec_version` when it happens.

Three JSON shapes, one directory convention each:

| Shape | Lives at | Written by |
|---|---|---|
| deck-spec | `library/decks/<slug>/deck-spec.json` | `compose` (agent) |
| template | `library/templates/<slug>.template.json` | `templatize` (agent) |
| theme | `library/themes/<name>.theme.json` | `templatize` (agent) |

## deck-spec

```json
{
  "spec_version": 0,
  "deck": {
    "title": "<deck title>",
    "aspect": 1.333,
    "theme": "orion",
    "language": "en"
  },
  "slides": [
    {
      "n": 1,
      "role": "title",
      "template": "title-bookend",
      "fill": { "title": "…", "subtitle": "…" }
    },
    {
      "n": 2,
      "role": "content",
      "template": "accent-headline-content",
      "stretch": false,
      "fill": { "title": "…", "body": ["bullet 1", "bullet 2"] }
    }
  ]
}
```

- `role` comes verbatim from the IDEA.md outline row (ideate's role vocabulary).
- `template` names a file in `library/templates/` (without `.template.json`).
- `stretch: true` marks a slide whose role is **not** in the template's `roles`
  list — an honest stretch the composing agent chose, never silent.
- `fill` keys must be box names in the template that accept text. A string for
  single-line boxes, an array of strings for `"content": "bullets"` boxes.
- Unresolved material renders as a literal visible `OPEN: …` line on the slide —
  never silently dropped, never plausibly filled.

## template

Geometry + role bindings from one analyzed archetype, **all source text
stripped** (the privacy wall — templates are committable, analysis is not).

```json
{
  "template": "accent-headline-content",
  "version": 0,
  "source": "orion-sample, archetype A (slides 3-5)",
  "roles": ["content"],
  "aspect": 1.333,
  "boxes": [
    { "box": "title", "x_pct": 5.0, "y_pct": 5.3, "w_pct": 90.0, "h_pct": 12.0,
      "text_style": "heading" },
    { "box": "body", "x_pct": 8.0, "y_pct": 21.3, "w_pct": 84.0, "h_pct": 60.0,
      "text_style": "body", "content": "bullets" },
    { "box": "accent-bar", "x_pct": 5.0, "y_pct": 92.0, "w_pct": 90.0, "h_pct": 2.0,
      "fill": "accent" }
  ],
  "open": []
}
```

- Geometry is `%` of slide (extract.py's convention) — templates survive
  aspect/size changes.
- A box with `text_style` accepts text; add `"content": "bullets"` when it takes
  an array. `"align": "center"` optional (default left).
- Style and fill values are **theme token names, never literals** — the
  template owns geometry, the theme owns appearance.
- `roles` lists only roles the *evidence* showed this archetype serving.
- `open` carries unresolved facts (e.g. theme-inherited styling).

## theme

The design guide as tokens. One per visual identity.

```json
{
  "theme": "orion",
  "version": 0,
  "source": "orion-sample visual grammar",
  "tokens": {
    "colors": { "accent": "2E5CFF", "text": "333333" },
    "text_styles": {
      "heading": { "size_pt": 32, "bold": true, "color": "accent" },
      "body":    { "size_pt": 18, "bold": false, "color": "text" }
    }
  },
  "open": []
}
```

- `colors` are 6-hex strings, no `#`. `text_styles[].color` names a color token.
- Optional per-style `"font": "<name>"`; omit to inherit the renderer default.

## Enforcement

**Gate:** `.venv/Scripts/python .claude/skills/compose/build.py library/decks/constellation-intro/deck-spec.json` — exits non-zero on any violation.

`build.py` (the compose skill's renderer) is the validator: it refuses a spec
whose template/theme/box/token references don't resolve, an unmarked role
stretch, and a text-accepting box with no fill — every error listed at once.
There is no separate schema checker — if `build.py` builds it, it's a valid
v0 spec. (The wall here is the Gate itself — no lint/test-tag walls exist
yet, there is no test framework; see root CLAUDE.md **Test**.)

## OPEN

- OPEN: v0 schema derives from one synthetic deck; real-deck evidence
  (multi-master decks, pictures, tables, charts) will force new box kinds.
- OPEN: bullets **render** as literal `• ` prefixes (python-pptx has no direct
  bullet API) — writing real `buChar`/`buAutoNum` XML in `build.py` is a later
  fidelity pass. The **read** side is closed: `extract.py` dumps per-paragraph
  bullet facts and per-master theme facts, so real-deck analysis can now state
  what bullets/inherited styles a template should reproduce.
