# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Versions are anchored by annotated git tags `vX.Y.Z` — the tag plus the `VERSION`
file are the source of truth, never this file.

## [Unreleased]

### Changed

- **deck-spec v0→v1** (breaking; slice: `.gravity/deck-spec/PLAN.v1.md`) —
  `build.py` refuses v0 specs and renders four box kinds: text (now with real
  `buChar` bullets from `tokens.bullet_char`, default `•`), solid fill,
  `table` (header style/fill token + `banding` cycle + optional `label_style`)
  and `chart` (`column`/`bar`/`line`, `series_fill` token). Style keys gain
  `italic`/`caps`; `align` gains `right`. Round-read verify also proves each
  promised graphic frame. Committed specs/templates/themes bumped; the
  meridian exhibit archetype is now templated (`exhibit-table`,
  `exhibit-chart`) and exercised by two new meridian-demo slides.

### Added

- **Theme/master extraction** — `extract.py` dumps a per-master `themes`
  section (theme color scheme, font scheme, the master's color map and
  title/body/other text-style defaults, lvl 1–3) parsed from raw OOXML, so
  `(inherit)` font/size/color censuses resolve from the dump instead of
  staying invisible. Closes the read side of the master-XML OPEN.
- **Bullet extraction** — per-paragraph `bullet_census`
  (`char:`/`autonum:`/`none`/`(inherit)`) per text shape plus a deck-wide
  aggregate. The write side (real `buChar` in `build.py`) stays OPEN.

- **Second fixture: meridian-pitch** — a synthetic consultant-mood financial
  pitch (`fixtures/make_meridian_fixture.py`, 11 slides, 16:9, all content
  fictional) exercising a rewritten theme (custom scheme colors,
  Georgia/Arial), real `buChar`/`buAutoNum` bullet XML, theme-inherited
  placeholders, a table, and a chart. Committed as the second `analyze`
  worked example (`library/analysis/meridian-pitch/`).
- **Meridian template family** — `kicker-headline-content` +
  `numbered-divider` templates and the `meridian` theme, generalized from the
  fixture per the `templatize` skill; proven by the committed
  `library/decks/meridian-demo/` verification spec (green build, zero
  stretches, full-circle geometry-exact).

### Changed

- `analyze` SKILL stage-2 rule: `(inherit)` values are now resolved against
  the dump's `themes` section, citing the chain; only an incomplete chain
  stays `OPEN:`. Worked example (`orion-sample` structure + PATTERNS)
  regenerated accordingly.
- CLAUDE.md smoke loops now cover both fixtures and both composed decks;
  deck-spec SPEC OPEN upgraded with concrete v1 evidence: `table`/`chart` box
  kinds (meridian exhibit archetype, 2×) and missing right-`align`/`caps`/
  `italic` style keys.

## [0.1.0] - 2026-07-11

First tagged release. The complete four-skill pipeline, built in one arc from a
synthetic evidence base.

### Added

- **`ideate` skill** — strawman-first brief elicitation: five themes, named
  arcs, per-slide content roles; output `library/ideas/<slug>/IDEA.md`.
- **`analyze` skill** — two-stage deck analysis: `extract.py` (deterministic
  structural facts → JSON) + agent interpretation (`PATTERNS.md` with cited
  slide numbers). Worked example: the synthetic orion-sample fixture.
- **`templatize` skill** — pattern report → text-free template JSONs + a theme
  token file (the design guide). Privacy wall: geometry survives, source text
  is stripped.
- **`compose` skill** — agent composes a deck-spec from brief × templates ×
  theme; `build.py` renders it deterministically, validating every reference
  (unmarked stretches, unfilled boxes, and dead refs are refused) and
  round-read verifying the output.
- **Deck-spec seam (v0, provisional)** — `.gravity/deck-spec/SPEC.md`: the
  deck-spec × template × theme JSON contract between the skills, enforced by
  `build.py`. Synthetic evidence only; real-deck analysis revises it.
- **Self-composing demo** — `library/decks/constellation-intro/` builds the
  project's own intro deck from its own brief (9 slides; extractor re-run on
  the output matches the templates exactly).
- **`.gravity/` doc system (gravity v1.8)** — protocol card, deck-spec domain,
  root-CLAUDE.md router.

[Unreleased]: https://github.com/mostlytricks/constellation/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/mostlytricks/constellation/releases/tag/v0.1.0
