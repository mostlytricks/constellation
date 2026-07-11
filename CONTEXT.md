# CONTEXT — constellation

Last touched: 2026-07-11

## Completed
- **v0.2.0 cut** — the evidence-and-fidelity release: theme-sighted extraction, the meridian consultant fixture + template family, breaking deck-spec v1 (tables/charts/style keys/real bullets), and the `storyline` skill (fifth star: stakes → skeptic → action titles → mood curve → ghost-deck read-back). Gate green at cut. Release commit `f6416db` pushed on `claude/constellation-gravity-release-i64nqq`; see `CHANGELOG.md [0.2.0]`.
- **Tag `v0.2.0` NOT on remote** — the remote session's token can only push `claude/*` branches (403 on tag refs). Recreate + push from the local machine: `git tag -a v0.2.0 -m "v0.2.0" f6416db && git push origin v0.2.0` (after fetching; ideally after the branch merges to `main`).

## Current State
- **Five skills** (ideate · storyline · analyze · templatize · compose); seam at **v1** (provisional — synthetic evidence only). Three template families, two themes, machine green end-to-end. Branch unmerged into `main` — open the PR when ready.
- Remaining OPENs (SPEC) all wait on real-deck evidence: numbered-list content kind, `picture` box kind, layout-level style walking, multi-master. Small shelf item: title-grammar census in `analyze` stage 2.

## Next Step
- On the local machine: merge the branch, push the `v0.2.0` tag (command above), then drop a **real deck** into `fixtures/` and run `analyze` — that evidence decides v1→v2 and replaces synthetic templates with earned ones.

---
