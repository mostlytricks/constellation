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

The dump gives you: slide size/aspect, the layout vocabulary per master, per-master **theme facts** (color scheme, font scheme, color map, master text-style defaults — what `(inherit)` resolves to), per-slide shapes with geometry (as % of slide — comparable across deck sizes), placeholder roles, text stats, per-run font/size/color censuses, per-paragraph bullet censuses, and deck-wide aggregates.

## Stage 2 — interpret

Write `library/analysis/<deck-name>/PATTERNS.md` with these sections:

- **Slide archetypes** — cluster slides by shape signature (layout + shape types + geometry). Name each archetype (e.g. "title-bar + 2-col body + footer"), list which slides instantiate it. An archetype recurring ≥2× is a **template candidate**.
- **Visual grammar** — the font/size hierarchy (which size means heading vs body), color roles (which color is accent vs text vs background), from the censuses.
- **Title grammar** — classify each content-bearing slide's headline: **label** (names a topic: "Q2 Financials") vs **claim** (verb + so-what, an action title: "Q2 beat plan by 12pts"). Report the census with slide numbers, wayfinding slides (cover/divider/closing) excluded. A deck whose content titles are all claims argues on its titles alone — the `storyline` skill's ghost-deck property; this section is its *detection* twin.
- **Grid** — recurring x/y/w/h percentages across slides = the implicit layout grid. Report the values you actually see.
- **Template candidates** — the archetypes worth generalizing, ranked by recurrence. These feed the `templatize` skill.

Rules:
- Facts come from the dump only; cite slide numbers (`slides 3, 5, 9`). Never claim a pattern you can't point at.
- Unknowns and ambiguities become `OPEN:` lines, never plausible filler.
- `(inherit)` counts mean values unstated at the run/paragraph — resolve them against the dump's `themes` section (scheme colors via the color map, `+mj-lt`/`+mn-lt` via the font scheme, sizes via `master_text_styles`), citing the chain. If the chain itself is incomplete (e.g. layout-level overrides, which the dump doesn't walk), say so as an `OPEN:` — don't invent the resolved value.
- Korean text: preserve as-is (dump is UTF-8, `ensure_ascii=False`).

## Privacy wall (this repo is public)

`fixtures/*.pptx` and `library/analysis/` are **git-ignored** — real decks and their extracted text never get committed. Only generalized templates with all source text stripped may graduate to `library/templates/`. Check before any commit that touches `library/`.
