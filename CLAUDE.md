# constellation

Agent skill set for presentation building — analyze existing decks into component patterns, generalize them into templates, manage a design guide, then compose idea + pattern + theme into a final PPT. Used from Claude Code.

> **alias:** `cst`

---

> **gravity: v1.8** · _the version of the workspace gravity system this project adopted (root `VERSION` / `CHANGELOG.md`). Bump when you re-sync to a newer skeleton; `/triage` flags drift._

> **Docs live in `.gravity/`.** This `CLAUDE.md` (identity, *how*) and `CONTEXT.md` (*now*) stay at the project root and auto-load. Everything else — contracts and any future *why* / *what-next* docs — is organized **by subject domain** under `.gravity/`. See the **Doc Map** below. One concern, one home — link, don't restate.

> **Protocol card: read `.gravity/GRAVITY.md` before touching `.gravity/` docs.** It embeds the project-side gravity protocol so this repo is self-describing even when opened without the workspace. It's a versioned copy — never hand-edit; re-copy from the workspace on a gravity upgrade.

## Doc Map (`.gravity/`)

Docs are grouped by **subject domain**, not by doc-type. A domain folder holds whichever of three kinds it needs — `ARCHITECTURE.html` (human deep-dive), `SPEC.md` (agent contract), `PLAN.*.md` (what/next) — named by *kind* because the folder already names the subject. **Recognized only when present** — no MISSION/ARCHITECTURE/IMPLEMENTATION_PLAN exist yet; CONTEXT.md carries the arc until one earns its keep.

```
.gravity/
  GRAVITY.md          # the protocol card — how to work these docs (versioned copy, never hand-edit)
  deck-spec/ SPEC.md  # the seam — deck-spec × template × theme JSON shapes (v0), enforced by compose/build.py
```

## What to read before a change (router)

| If you're changing… | Read first | Human reference |
|---|---|---|
| deck-spec / template / theme JSON shapes, fill semantics, role→template matching, build.py validation rules | `.gravity/deck-spec/SPEC.md` | — |
| a skill's procedure (ideate / analyze / templatize / compose) | `.claude/skills/<skill>/SKILL.md` (+ the seam SPEC if it touches the shapes) | — |

## Adding a domain (start here for a new feature)

A **domain** is a durable subject area an agent will repeatedly navigate and change — not every feature is one. Mint a `.gravity/<domain>/` folder only when the feature has its own *gravity*; otherwise it's a slice under an existing domain. (`/new-domain constellation <domain>` does the wiring.)

**Gate — is it a domain?** It earns a folder when it has its own *principle* and most of: rules an agent must respect (`SPEC.md`), a "how it's built" beyond a file map (`ARCHITECTURE.html`), a multi-step arc (`PLAN.*.md`). If not, it's a `PLAN.*.md` slice under an existing domain.

**Wire the indexes** when minting: the Doc Map above + the router table row (once it has a SPEC). MISSION/IMPLEMENTATION_PLAN rows apply only when those docs exist.

## The Pipeline (the shape of the project)

A deck is stars arranged into a picture: components are stars, patterns are the lines between them, the design theme is the sky. Four capabilities, each a Claude Code skill:

1. **ideate** — build/refine the presentation idea (narrative, audience, message arc).
2. **analyze** — read an existing/given `.pptx`, extract its component patterns (layouts, recurring slide shapes, visual grammar).
3. **templatize** — generalize extracted patterns into reusable templates + maintain the design guide (type, color tokens, spacing).
4. **compose** — combine idea × pattern × theme → generate the final `.pptx`.

## Stack

- **Skills:** Claude Code skills (`.claude/skills/<name>/SKILL.md`) — markdown instructions + helper scripts.
- **Language / runtime:** Python 3.12 for pptx read/write helpers.
- **Key dependency:** `python-pptx` — confirmed for v0 generation (`compose/build.py`) and structural extraction; `extract.py` additionally parses raw OOXML (via python-pptx's bundled `lxml`) for theme/master facts and bullet facts. OPEN: *writing* real bullet/numbering XML in `build.py` is still a later fidelity pass (see `.gravity/deck-spec/SPEC.md` OPEN).
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

- `.claude/skills/` — the four skills (the product).
- `library/` — extracted patterns, templates, design guides, composed decks (the output shelf).
- Seam: the **deck-spec** — the intermediate representation between analyze/templatize and compose. Defined at `.gravity/deck-spec/SPEC.md` (**v0, provisional** — schema fixed from synthetic evidence only; real-deck analysis is expected to revise it, bumping `spec_version`). Enforced by `compose/build.py`, which refuses unresolvable specs.

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
