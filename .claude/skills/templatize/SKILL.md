---
name: templatize
description: Generalize an analyzed deck's slide archetypes into reusable text-free template JSONs plus a theme token file (the design guide). Use after the analyze skill has produced a PATTERNS.md, when the user wants the found patterns turned into composable templates.
---

# templatize — pattern report → reusable parts

Input: `library/analysis/<deck>/PATTERNS.md` + `structure.json` (from `analyze`).
Output: `library/templates/<slug>.template.json` per archetype +
`library/themes/<name>.theme.json` — shapes defined in `.gravity/deck-spec/SPEC.md`
(read it first; it is the contract, this file is only the procedure).

## Procedure

1. **Take only what recurred.** Each **template candidate** in PATTERNS.md
   (archetype recurring ≥2×) becomes one template file. Singletons don't —
   a pattern seen once is an anecdote, not a template.

2. **Strip every trace of source text.** Boxes keep geometry, style bindings,
   and a generic box name (`title`, `body`, `accent-bar`) — never the deck's
   words, names, or numbers. This is the **privacy wall**: analysis output is
   git-ignored, templates are committed, and the strip is what makes that safe.

3. **Bind appearance to tokens, not values.** Read PATTERNS.md's visual grammar,
   mint the theme file (color roles, the type hierarchy), then have every
   template box reference token names. If the same literal (`2E5CFF`) does two
   jobs in the grammar (heading text + bar fill), that's **one token** used
   twice — the grammar's insight is exactly that reuse.

4. **Record what the evidence couldn't show.** Theme-inherited styling
   (`(inherit)` censuses) means the true value lives in master/theme XML the
   extractor doesn't read. Write a provisional value if compose needs one, and
   an `open` entry saying it's provisional — never present a guess as extracted
   fact.

5. **Verify with the real gate.** A template is proven by being built from:
   compose a minimal spec that uses it and run
   `.venv/Scripts/python .claude/skills/compose/build.py <spec> -o <out>.pptx`.
   Green build = valid template. (No separate validator exists — DECK-SPEC
   "Enforcement".)

6. **Privacy check before commit.** Grep the new JSONs for any
   `text_preview` string from the source `structure.json`. One hit = the wall
   is breached; strip and re-check.

## Rules

- `roles` lists only what the evidence showed. Compose may stretch a template
  to other roles, but it marks `stretch: true` in the spec — the template never
  pre-claims range it didn't earn.
- Slug the template by what it *is* (`accent-headline-content`), not by the
  source deck — the source lives in the `source` field.
- One theme per visual identity, not per deck: if a second deck shows the same
  grammar, it joins the existing theme rather than minting a near-duplicate.

## Worked example

`library/templates/accent-headline-content.template.json` +
`title-bookend.template.json` + `library/themes/orion.theme.json` — generalized
from `library/analysis/orion-sample/PATTERNS.md`.
