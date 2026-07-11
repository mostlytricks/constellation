---
name: storyline
description: Pressure-test one presentation's narrative before compose — sharpen every outline message into an action title, elicit the stakes and the skeptic, set a mood curve per act, and verify flow with a ghost-deck read-back. An interviewing skill; use when the user has a brief (IDEA.md) and wants the pitch to land ("help me with the mood and flow", "make the titles tell the story"). Upgrades IDEA.md in place; run ideate first if no brief exists.
---

# storyline — make one pitch land

`ideate` gets the idea out of the head; **storyline makes it argue.** Input: an
existing `library/ideas/<slug>/IDEA.md` (no brief → run `ideate` first, don't
invent one) plus whatever strong context the user brings. Output: the **same
IDEA.md, upgraded in place** — messages become action titles, the arc carries a
mood curve, and a `## Flow` block records the stake, the skeptic, and the
verified title spine. No new artifact: IDEA.md stays the one home for content
and structure.

Interview, never generator: every claim you write must trace to the user's
words or the outline's `material` column. Missing evidence stays `OPEN:` —
a confident title on a fact that doesn't exist is the worst slide in any deck.

## Procedure — five moves, strawman-first

Gap-scan the brief first; skip any move it already answers. Each move opens
with your best guess for the user to correct — a strawman beats a blank
question.

### 1 · Stakes

A pitch opens on tension, not on the agenda. Ask: **what happens if the room
does nothing?** Strawman the one-line stake from the brief's core message and
material, then let the user sharpen it. The stake becomes the emotional floor
of act one and usually the claim of slide 2.

### 2 · The skeptic's seat

**Who is the hardest person in the room, and what is their killer objection?**
Flow is mostly deciding what the audience silently asks after each slide and
answering it next — the skeptic names the loudest of those questions. The
answer decides *placement*: the rebuttal slide goes before the ask, never
after. Record it in `## Flow` with the slide number that answers it.

### 3 · Action-title pass

Walk the outline row by row. A title without a verb and a so-what is a
**label**; rewrite it as a **claim** the slide then has to prove — strawman
each rewrite, user corrects:

| label (before) | claim (strawman — user fixes) |
|---|---|
| Market context | The mid-market is 14% penetrated while incumbents fight over the enterprise tier |
| Financials | Revenue triples by FY28 — and the installed base alone funds it |

Bounds: a claim may only promise what its `material` cell can show
(no material → the claim gets an `OPEN:` in the material column, or softens);
`title` / `section` / `closing` rows are wayfinding, not arguments — leave
them as labels.

### 4 · Mood curve

Propose one register per act — e.g. *problem: **sober** → solution:
**confident** → ask: **direct*** — as a short mood-word list the user vetoes
or replaces. Register vocabulary (open, not exhaustive): sober · urgent ·
confident · warm · playful · visionary · direct. Keep it to one word per act,
≤4 acts; a mood curve that needs a paragraph is a mood the deck can't render.

Mood words are compose inputs, not decoration — they steer theme choice,
divider cadence, exhibit density, and the weight of the ask slide (see the
compose skill's stage 1). Write the curve into the `Arc:` line.

### 5 · Ghost-deck read-back (the exit test)

Read the user **only the titles, in order** — nothing else. The spine passes
when each title answers the question the previous one raised (*so what? →
but how? → prove it → what do you want?*) and the last title is the core
message's cash-out. If the spine doesn't argue, the problem is the **arc, not
the wording** — reorder or cut slides (back to `ideate` if the arc itself is
wrong), never paper over a broken sequence with better prose. Only a spine
that survives read-back gets written to the file.

## Write-back — the IDEA.md upgrade

```markdown
Arc: findings → implications → asks (mood: sober → confident → direct)

## Outline
| # | role | message (action title) | material |
| 4 | content | An $18B market growing 12% annually, still under-penetrated | TAM + penetration data |

## Flow
- Stake: <the one-line why-now>
- Skeptic: <who + objection> → answered on slide <n>
- Spine: verified <date> — <one line: how the titles alone argue the case>
```

- `message` column header becomes `message (action title)` once the pass ran.
- Unresolved moves stay visible: `OPEN: mood for act 2 undecided`, never a
  plausible fill.

## Rules

- **No brief, no storyline.** Elicitation order is ideate → storyline; don't
  reconstruct a brief from hallway context inside this skill.
- **Claims trace to material.** You may sharpen wording freely; you may not
  add a number, name, or fact the user didn't give.
- **The ghost-deck test is the gate.** A `Spine: verified …` line you didn't
  actually read back to the user is a lie in a file.
- **One home.** Never fork a STORYLINE.md — this skill edits IDEA.md.
- **Language follows the brief** (KR briefs get KR titles; the spine is read
  back in the brief's language).

## Worked example

`library/ideas/meridian-pitch/IDEA.md` — the consultant-pitch fixture
reverse-briefed into a storyline-upgraded shape (synthetic, labeled as such):
action-title spine, sober→confident→direct mood curve, stake + skeptic on
record. It shows the *output* shape; the interview itself is the live part.
