# DECK-SPEC — the seam (v1, provisional)

The intermediate representation between the four skills. `ideate` produces the
brief above it, `templatize` produces the parts it references, `compose` writes
one and `build.py` renders it. **v1 is still fixed by synthetic evidence only**
(orion-sample + meridian-pitch) — real-deck analysis may revise every shape
here; that's expected, bump `spec_version` when it happens.

v0→v1 (evidence: `library/analysis/meridian-pitch/PATTERNS.md`): `table` and
`chart` box kinds, `right` align, `caps`/`italic` style keys, theme
`bullet_char`, real `buChar` bullet rendering. Change intent:
`PLAN.v1.md` alongside this file.

Three JSON shapes, one directory convention each:

| Shape | Lives at | Written by |
|---|---|---|
| deck-spec | `library/decks/<slug>/deck-spec.json` | `compose` (agent) |
| template | `library/templates/<slug>.template.json` | `templatize` (agent) |
| theme | `library/themes/<name>.theme.json` | `templatize` (agent) |

## deck-spec

```json
{
  "spec_version": 1,
  "deck": {
    "title": "<deck title>",
    "aspect": 1.778,
    "theme": "meridian",
    "language": "en"
  },
  "slides": [
    {
      "n": 1,
      "role": "content",
      "template": "kicker-headline-content",
      "stretch": false,
      "fill": { "kicker": "…", "headline": "…", "body": ["bullet 1", "bullet 2"],
                "source": "…", "footer": "…", "page-no": "1" }
    },
    {
      "n": 2,
      "role": "exhibit",
      "template": "exhibit-table",
      "fill": {
        "kicker": "…", "headline": "…", "source": "…", "footer": "…", "page-no": "2",
        "exhibit": [["$M", "FY24"], ["Revenue", "18.2"]]
      }
    }
  ]
}
```

- `role` comes verbatim from the IDEA.md outline row (ideate's role vocabulary).
- `template` names a file in `library/templates/` (without `.template.json`).
- `stretch: true` marks a slide whose role is **not** in the template's `roles`
  list — an honest stretch the composing agent chose, never silent.
- `fill` keys must be fillable boxes in the template. By box kind:
  a **string** for single-line text boxes; an **array of strings** for
  `"content": "bullets"`; an **array of equal-length string rows** (first row =
  header) for `"content": "table"`; a
  `{"categories": [...], "series": [{"name": …, "values": [...]}]}` object
  (values matching categories) for `"content": "chart"`.
- Every fillable box must have a fill entry. Unresolved material renders as a
  literal visible `OPEN: …` line on the slide — never silently dropped, never
  plausibly filled.

## template

Geometry + role bindings from one analyzed archetype, **all source text
stripped** (the privacy wall — templates are committable, analysis is not).

```json
{
  "template": "exhibit-table",
  "version": 1,
  "source": "meridian-pitch, archetype B (slide 7)",
  "roles": ["exhibit"],
  "aspect": 1.778,
  "boxes": [
    { "box": "kicker", "x_pct": 4.5, "y_pct": 6.0, "w_pct": 90.8, "h_pct": 4.0,
      "text_style": "kicker" },
    { "box": "exhibit", "x_pct": 4.5, "y_pct": 29.3, "w_pct": 90.8, "h_pct": 32.0,
      "content": "table", "text_style": "table-body", "label_style": "table-label",
      "header": { "text_style": "table-header", "fill": "navy" },
      "banding": ["paper", "panel"] },
    { "box": "rule", "x_pct": 4.5, "y_pct": 23.3, "w_pct": 9.0, "h_pct": 0.4,
      "fill": "gold" }
  ],
  "open": []
}
```

- Geometry is `%` of slide (extract.py's convention) — templates survive
  aspect/size changes.
- Box kinds: a box with `text_style` accepts **text** (add
  `"content": "bullets"` when it takes an array — rendered as real `buChar`
  bullets with hanging indent, char from the theme's `bullet_char`);
  `"content": "table"` adds `header` (style + fill token for row 0), optional
  `banding` (color tokens cycled over body rows) and `label_style` (column 0);
  `"content": "chart"` takes `"chart": "column" | "bar" | "line"` and an
  optional `series_fill` color token; a box with only `fill` is a solid
  rectangle. `"align": "center" | "right"` optional on text boxes (default left).
  Tables render column 0 left, other columns right (the evidence's convention).
- Style and fill values are **theme token names, never literals** — the
  template owns geometry, the theme owns appearance.
- `roles` lists only roles the *evidence* showed this archetype serving.
- `open` carries unresolved facts (e.g. an untemplated variant).

## theme

The design guide as tokens. One per visual identity.

```json
{
  "theme": "meridian",
  "version": 1,
  "source": "meridian-pitch visual grammar",
  "tokens": {
    "colors": { "navy": "0B2340", "ink": "3B4652", "gold": "C9A227" },
    "bullet_char": "▪",
    "text_styles": {
      "kicker":   { "size_pt": 11, "bold": true, "color": "gold", "font": "Arial", "caps": true },
      "headline": { "size_pt": 24, "bold": true, "color": "navy", "font": "Georgia" },
      "source":   { "size_pt": 9, "bold": false, "color": "mute", "font": "Arial", "italic": true }
    }
  },
  "open": []
}
```

- `colors` are 6-hex strings, no `#`. `text_styles[].color` names a color token.
- Optional per-style: `"font": "<name>"` (omit to inherit the renderer
  default), `"italic": true`, `"caps": true` (uppercases the fill at render).
- Optional `tokens.bullet_char` (default `•`) — the `buChar` for bullet boxes.

## Enforcement

**Gate:** `.venv/Scripts/python .claude/skills/compose/build.py library/decks/constellation-intro/deck-spec.json` — exits non-zero on any violation. `library/decks/meridian-demo/deck-spec.json` exercises the v1-only kinds (table, chart, right-align).

`build.py` (the compose skill's renderer) is the validator: it refuses a spec
whose template/theme/box/token references don't resolve, a non-1
`spec_version`, an unmarked role stretch, a fillable box with no fill, ragged
table rows, and chart series that don't match their categories — every error
listed at once. Round-read verify additionally proves each promised
table/chart came back as a real graphic frame. There is no separate schema
checker — if `build.py` builds it, it's a valid v1 spec. (The wall here is
the Gate itself — no lint/test-tag walls exist yet, there is no test
framework; see root CLAUDE.md **Test**.)

## OPEN

- OPEN: numbered lists (`buAutoNum`, evidenced by meridian-pitch slide 2) have
  no content kind — bullets-only; a `"content": "numbered"` kind awaits more
  evidence.
- OPEN: no `picture` box kind — no evidence yet (real decks will supply it).
- OPEN: v1 still derives from synthetic decks; real-deck evidence
  (multi-master decks, pictures, complex tables) may revise every shape here.
