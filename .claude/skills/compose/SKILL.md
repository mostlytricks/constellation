---
name: compose
description: Combine a presentation brief (IDEA.md), templates, and a theme into a deck-spec JSON, then render it to a final .pptx with build.py. Use when the user wants a deck actually generated — the last stage of the pipeline, after ideate has produced a brief.
---

# compose — idea × pattern × theme → .pptx

Two stages with a hard boundary, mirror of `analyze`'s:

1. **Compose (you — judgment).** Match each brief slide to a template, write
   the fills, produce `library/decks/<slug>/deck-spec.json`.
2. **Render (script — deterministic).** `build.py` validates every reference
   and draws the file. It refuses what doesn't resolve; it never improvises.

Read `.gravity/deck-spec/SPEC.md` first — it is the contract; this file is the procedure.

## Prerequisites

- A brief: `library/ideas/<slug>/IDEA.md` (from `ideate`). No brief → run
  `ideate` first, don't invent one.
- Templates + a theme in `library/templates/` / `library/themes/` (from
  `templatize`). None that fit → say so; don't hand-draw geometry inline.

## Stage 1 — compose the spec

1. **Match roles to templates.** For each outline row, pick the template whose
   `roles` list contains the row's role. No exact match → pick the nearest
   shape and set `"stretch": true` (build.py rejects an unmarked stretch).
   Note every stretch to the user — repeated stretching of the same role is
   the signal that `templatize` should mint a template for it.
2. **Write the fills.** The brief's `message` line becomes the title box;
   `material` becomes body bullets. Stay inside the brief — compose arranges
   content, it doesn't author new claims. `OPEN:` material from the brief goes
   onto the slide as a literal visible `OPEN: …` bullet, never silently
   dropped, never plausibly filled.
3. **Respect the brief's language** (KR briefs → KR decks; the dump/render
   path is UTF-8-safe end to end).

## Stage 2 — render

```bash
.venv/Scripts/python .claude/skills/compose/build.py \
  library/decks/<slug>/deck-spec.json -o library/decks/<slug>/<slug>.pptx
```

Green output line = built **and** round-read verified (slide count + text
present). Fix spec errors by editing the spec, not by weakening build.py.

## Outputs & privacy

- `deck-spec.json` is committed (it's authored content, the reproducible
  source). The rendered `.pptx` is **git-ignored** (regenerable binary) —
  same pattern as `fixtures/`.
- A deck composed from a *private* brief stays out of git entirely: put the
  brief and spec under a git-ignored path and say so in the session notes.

## Worked example

`library/decks/constellation-intro/` — the demo brief composed with the
orion-sample templates; slides 4 and 8 are honest stretches (`section`,
`demo` have no evidence-backed template yet).
