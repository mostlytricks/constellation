# constellation

Agent skill set for presentation building — analyze existing decks into component patterns, generalize them into templates, manage a design guide, then compose idea + pattern + theme into a final PPT. Used from Claude Code.

> **alias:** `cst`

---

<!-- gravity:router v3.2 — managed by /adopt-gravity + /sync-gravity; do not hand-edit inside the fences -->
> **gravity: v3.2** — docs live in `.gravity/`. Before working here, read `.gravity/GRAVITY.md`
> (the protocol: doc kinds + rates, navigation discipline) and `.gravity/ROUTER.md` (the Doc Map +
> what to read before changing what). Session ritual: read `CONTEXT.md` first; update it before stopping.
<!-- /gravity:router -->

## The Pipeline (the shape of the project)

A deck is stars arranged into a picture: components are stars, patterns are the lines between them, the design theme is the sky — and the storyline is the picture the constellation draws. Five capabilities, each a Claude Code skill:

1. **ideate** — build/refine the presentation idea (narrative, audience, message arc).
2. **storyline** — pressure-test one pitch's narrative: action titles, stakes + skeptic, mood curve, ghost-deck flow check (interview; upgrades the brief in place).
3. **analyze** — read an existing/given `.pptx`, extract its component patterns (layouts, recurring slide shapes, visual grammar).
4. **templatize** — generalize extracted patterns into reusable templates + maintain the design guide (type, color tokens, spacing).
5. **compose** — combine idea × pattern × theme → generate the final `.pptx`.

## Stack

- **Skills:** Claude Code skills (`.claude/skills/<name>/SKILL.md`) — markdown instructions + helper scripts.
- **Language / runtime:** Python 3.13 for pptx read/write helpers (the repo venv is built on 3.13).
- **Key dependency:** `python-pptx` — confirmed for generation (`compose/build.py`: text, fills, tables, charts, real `buChar` bullets) and structural extraction; `extract.py` additionally parses raw OOXML (via python-pptx's bundled `lxml`) for theme/master facts and bullet facts. Remaining fidelity OPENs live in `.gravity/deck-spec/SPEC.md` (numbered lists, pictures).
- **Datastore:** none — templates and design guides are files in this repo.

## Run

```bash
# venv lives in this repo (workspace rule §4 — one venv per project)
python -m venv .venv && .venv/Scripts/pip install python-pptx
```

Skills are invoked from Claude Code sessions, not run standalone.

## Test

```bash
# smoke loop 1: synthetic fixtures → extractor → structural dumps
.venv/Scripts/python fixtures/make_fixture.py
.venv/Scripts/python .claude/skills/analyze/extract.py fixtures/orion-sample.pptx \
  -o library/analysis/orion-sample/structure.json
.venv/Scripts/python fixtures/make_meridian_fixture.py
.venv/Scripts/python .claude/skills/analyze/extract.py fixtures/meridian-pitch.pptx \
  -o library/analysis/meridian-pitch/structure.json

# smoke loop 2: deck-specs → rendered decks (round-read verified by the script)
.venv/Scripts/python .claude/skills/compose/build.py \
  library/decks/constellation-intro/deck-spec.json \
  -o library/decks/constellation-intro/constellation-intro.pptx
.venv/Scripts/python .claude/skills/compose/build.py \
  library/decks/meridian-demo/deck-spec.json \
  -o library/decks/meridian-demo/meridian-demo.pptx
```

No test framework yet — the honest gate is the two smoke loops (loop 2 exits
non-zero on any broken spec reference or a slide that round-reads empty) plus
eyeballing loop 1's dump against `library/analysis/orion-sample/PATTERNS.md`
(the worked example). Full-circle check: run loop 1's extractor **on loop 2's
output** — geometry and censuses must match the templates/theme exactly.

## Conventions

- Commit style: imperative one-liner, `<skill>: <what changed>` when scoped to one skill.
- Skill layout: one folder per skill under `.claude/skills/`, helper scripts inside the skill folder.
- Templates/design guides the skills *produce* live under `library/` (patterns, themes) — the skills are the machine, `library/` is the output shelf.

## Constraints & Gotchas

- `.pptx` fidelity: python-pptx cannot write every OOXML feature it can read — round-tripping a complex deck may drop effects. Prefer *generating from template* over *editing in place*.
- Korean text/fonts in decks: watch encoding and font fallback (cp949 legacy files exist in the wild).
- Distant ancestor: `antigravity--pptx-template-manager` (workspace, archived thinking) — its JSON deck-spec idea may get reused here.

## Entry Points

- `.claude/skills/` — the five skills (the product).
- `library/` — extracted patterns, templates, design guides, composed decks (the output shelf).
- Seam: the **deck-spec** — the intermediate representation between analyze/templatize and compose. Defined at `.gravity/deck-spec/SPEC.md` (**v1, provisional** — schema fixed from synthetic evidence only; real-deck analysis is expected to revise it, bumping `spec_version`). Enforced by `compose/build.py`, which refuses unresolvable specs.

## Git

- Remote: `https://github.com/mostlytricks/constellation.git`
- Default branch: `main`

## Releasing

- Version source of truth: the `VERSION` file + annotated git tag `vX.Y.Z`
  (`CHANGELOG.md` records, never decides). Pre-1.0: breaking → minor,
  feature/fix → patch.
- Cut with `/cut-release constellation` (workspace command): it verifies
  `[Unreleased]` has content, runs the smoke loops as the gate, renames the
  block with the system date, bumps `VERSION`, commits, tags — and stops
  before push.
