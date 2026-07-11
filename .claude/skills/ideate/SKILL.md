---
name: ideate
description: Build or refine a presentation idea into a structured brief (IDEA.md) — audience, core message, narrative arc, per-slide outline with content roles. Use when the user has a presentation to make and the idea exists only in their head, or as a vague topic. The output feeds compose.
---

# ideate — head → presentation brief

Structured elicitation, **strawman-first**: a draft the user corrects beats a blank
question. Never ask what's already been said; never plausibly fill what wasn't.

## Procedure

1. **Gap-scan.** Read everything the user has given (topic, context, files). List
   which of the five themes below are already answered. Ask only about the gaps.

2. **Elicit the five themes** — with a strawman guess per question:
   - **Audience & occasion** — who's in the room, what do they already believe,
     what's the setting (pitch / report-out / lecture / all-hands)?
   - **Core message** — the ONE sentence the audience must still remember a week
     later. If the user gives three, make them pick.
   - **Arc** — propose one of the named arcs (below) as the strawman; let them
     bend it.
   - **Evidence & material** — what exists to show (data, demos, prior decks,
     screenshots)? Missing evidence becomes an `OPEN:` line, not a fake bullet.
   - **Constraints** — time limit, slide budget, tone, brand/design rules,
     language (EN/KR/mixed).

3. **Draft the outline.** Per-slide entries, each with a **role** (the seam —
   compose later matches roles to component archetypes from `analyze`):

   | role | means |
   |---|---|
   | `title` | opening bookend |
   | `agenda` | map of the talk |
   | `section` | act divider |
   | `content` | one idea + supporting bullets |
   | `comparison` | two+ things side by side |
   | `data` | a chart/table carries the message |
   | `quote` | borrowed authority / testimonial |
   | `demo` | screenshot / live-demo anchor |
   | `summary` | up-front executive summary — the whole case on one slide |
   | `exhibit` | a table/chart carries the message (evidence-earned name for `data`) |
   | `ask` | the direct request — funding, decision, headcount |
   | `closing` | takeaway bookend |

4. **Read back** the outline in one screen; get confirmation or corrections.

5. **Write** `library/ideas/<slug>/IDEA.md` (shape below). Unresolved items stay
   as visible `OPEN:` lines.

6. **Offer the storyline pass.** For a pitch that has to *land* (stakes, a
   skeptical room), suggest running the `storyline` skill next — it upgrades
   the outline's messages into action titles, sets a mood curve on the arc,
   and verifies flow with a ghost-deck read-back, in this same file.

## Named arcs (strawman menu)

- **problem → solution** — pain first, your thing as the relief (pitches)
- **before → after → bridge** — the transformation story (demos, launches)
- **three pillars** — parallel structure, one idea per pillar (strategy, overviews)
- **journey** — chronological, milestones as beats (retrospectives, reports)
- **findings → implications → asks** — data-led, decision-forcing (exec readouts)

## IDEA.md shape (the Minimal Shape)

```markdown
# IDEA — <title>

Audience: <who + what they believe walking in>
Occasion: <setting, time limit, language>
Core message: <the one sentence>
Arc: <named arc + any bends>
Tone: <e.g. confident-but-modest, playful, formal>

## Outline
| # | role | message (one line) | material |
|---|------|--------------------|----------|
| 1 | title | ... | — |
| 2 | agenda | ... | — |
| 3 | content | ... | OPEN: need Q2 numbers |

## OPEN
- OPEN: <anything unresolved — missing evidence, undecided sections>
```

## Rules

- The user's language choice governs the brief's language (KR decks get KR briefs).
- One core message. A brief with two theses is two presentations.
- Every outline row needs a role — a slide that can't name its role usually
  shouldn't exist (say so, gently).
- Don't design visuals here — that's `templatize`/`compose` territory. The brief
  is content and structure only.
