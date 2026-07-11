# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).
Versions are anchored by annotated git tags `vX.Y.Z` — the tag plus the `VERSION`
file are the source of truth, never this file.

## [Unreleased]

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
