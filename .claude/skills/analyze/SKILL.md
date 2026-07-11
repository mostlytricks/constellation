---
name: analyze
description: Analyze a .pptx deck into a component-pattern report. Run the deterministic extractor on the deck, then interpret the structural JSON into slide archetypes, visual grammar, and template candidates. Use when the user gives a presentation file to study, or wants its patterns generalized into templates.
---

# analyze — deck → component-pattern report

Two stages with a hard boundary, never blurred:

1. **Extract (script — facts).** `extract.py` dumps the deck's structure to JSON. Deterministic; never interprets.
2. **Interpret (you — judgment).** Read the JSON and write the pattern report. Every claim cites slide numbers from the dump.

## Stage 1 — extract

```bash
# from the constellation repo root (venv already has python-pptx)
.venv/Scripts/python .claude/skills/analyze/extract.py <deck>.pptx \
  -o "library/analysis/<deck-name>/structure.json"
```

The dump gives you: slide size/aspect, the layout vocabulary per master, per-slide shapes with geometry (as % of slide — comparable across deck sizes), placeholder roles, text stats, per-run font/size/color censuses, and deck-wide aggregates.

## Stage 2 — interpret

Write `library/analysis/<deck-name>/PATTERNS.md` with these sections:

- **Slide archetypes** — cluster slides by shape signature (layout + shape types + geometry). Name each archetype (e.g. "title-bar + 2-col body + footer"), list which slides instantiate it. An archetype recurring ≥2× is a **template candidate**.
- **Visual grammar** — the font/size hierarchy (which size means heading vs body), color roles (which color is accent vs text vs background), from the censuses.
- **Grid** — recurring x/y/w/h percentages across slides = the implicit layout grid. Report the values you actually see.
- **Template candidates** — the archetypes worth generalizing, ranked by recurrence. These feed the `templatize` skill.

Rules:
- Facts come from the dump only; cite slide numbers (`slides 3, 5, 9`). Never claim a pattern you can't point at.
- Unknowns and ambiguities become `OPEN:` lines, never plausible filler.
- `(inherit)` counts mean theme-resolved values the extractor can't see — report them as inherited, don't invent the resolved value.
- Korean text: preserve as-is (dump is UTF-8, `ensure_ascii=False`).

## Privacy wall (this repo is public)

`fixtures/*.pptx` and `library/analysis/` are **git-ignored** — real decks and their extracted text never get committed. Only generalized templates with all source text stripped may graduate to `library/templates/`. Check before any commit that touches `library/`.
