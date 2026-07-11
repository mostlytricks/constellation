# constellation

Agent skill set for presentation building — analyze existing decks into component patterns, generalize them into templates, manage a design guide, then compose idea + pattern + theme into a final PPT. Used from Claude Code.

> **alias:** `cst`

---

## Docs in this project

- **CONTEXT.md** — start here: current state + the single next step. *Now.*
- **CLAUDE.md** (this file) — stable identity: stack, run/test, entry points, gotchas. *How.*

## The Pipeline (the shape of the project)

A deck is stars arranged into a picture: components are stars, patterns are the lines between them, the design theme is the sky. Four capabilities, each a Claude Code skill:

1. **ideate** — build/refine the presentation idea (narrative, audience, message arc).
2. **analyze** — read an existing/given `.pptx`, extract its component patterns (layouts, recurring slide shapes, visual grammar).
3. **templatize** — generalize extracted patterns into reusable templates + maintain the design guide (type, color tokens, spacing).
4. **compose** — combine idea × pattern × theme → generate the final `.pptx`.

## Stack

- **Skills:** Claude Code skills (`.claude/skills/<name>/SKILL.md`) — markdown instructions + helper scripts.
- **Language / runtime:** Python 3.12 for pptx read/write helpers.
- **Key dependency:** `python-pptx` (read + generate `.pptx`). OPEN: confirm it covers pattern extraction needs, or whether raw OOXML (zip + lxml) is needed for deep analysis.
- **Datastore:** none — templates and design guides are files in this repo.

## Run

```bash
# venv lives in this repo (workspace rule §4 — one venv per project)
python -m venv .venv && .venv/Scripts/pip install python-pptx
```

Skills are invoked from Claude Code sessions, not run standalone.

## Test

```bash
# smoke loop: synthetic fixture → extractor → structural dump
.venv/Scripts/python fixtures/make_fixture.py
.venv/Scripts/python .claude/skills/analyze/extract.py fixtures/orion-sample.pptx \
  -o library/analysis/orion-sample/structure.json
```

No test framework yet — the honest gate is the smoke loop above plus eyeballing the dump against `library/analysis/orion-sample/PATTERNS.md` (the worked example).

## Conventions

- Commit style: imperative one-liner, `<skill>: <what changed>` when scoped to one skill.
- Skill layout: one folder per skill under `.claude/skills/`, helper scripts inside the skill folder.
- Templates/design guides the skills *produce* live under `library/` (patterns, themes) — the skills are the machine, `library/` is the output shelf.

## Constraints & Gotchas

- `.pptx` fidelity: python-pptx cannot write every OOXML feature it can read — round-tripping a complex deck may drop effects. Prefer *generating from template* over *editing in place*.
- Korean text/fonts in decks: watch encoding and font fallback (cp949 legacy files exist in the wild).
- Distant ancestor: `antigravity--pptx-template-manager` (workspace, archived thinking) — its JSON deck-spec idea may get reused here.

## Entry Points

- `.claude/skills/` — the four skills (the product).
- `library/` — extracted patterns, templates, design guides (the output shelf).
- Seam: the **deck-spec** — the intermediate representation between analyze/templatize and compose. OPEN: define its schema before compose exists.

## Git

- Remote: `https://github.com/mostlytricks/constellation.git`
- Default branch: `main`
