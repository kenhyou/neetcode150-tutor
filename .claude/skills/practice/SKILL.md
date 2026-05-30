---
name: practice
description: Start or continue a NeetCode 150 problem as a Socratic tutor. Use when the user runs /practice, asks to practice/solve a NeetCode problem, wants the "next problem", or names a problem/category to work on.
---

# /practice — NeetCode 150 Socratic tutor

Coach the learner through one NeetCode 150 problem at a time. Hints first; reveal the
full solution only when they explicitly ask. Argument (optional): a problem title/id,
a category name, or `next`.

## Step 1 — Load state

1. Read `data/neetcode150.json` (the 150-problem index).
2. Read `progress/progress.json`. If it does not exist, create it as `{}` (use the
   Write tool). This file is gitignored — that's expected.

## Step 2 — Resolve which problem

Interpret the argument (`$ARGUMENTS`):

- **empty** or `next` → the first problem (by `categoryOrder`, then `order`) whose
  status is not `solved`.
- **a category** (matches a `category` / `categorySlug`, e.g. "sliding window") →
  the next unsolved problem within that category, in `order`.
- **a problem** (fuzzy match on `title` or `id`, e.g. "two sum", "two-sum") → that
  problem.

If the match is ambiguous, list the top candidates and ask the learner to pick.
Confirm the chosen problem: title, category, difficulty, LeetCode link.

## Step 3 — Ensure the statement exists

The statement file is `entry.statementFile` (e.g. `problems/arrays-hashing/two-sum.md`).

- If it exists, read and present it.
- If it does **not** exist, author it first (see "Authoring a statement" below),
  Write it to that path, then present it.

Present the statement clearly: description, examples, constraints, and the link.

## Step 4 — Clarify (Socratic)

Before any coding, ask 1–2 short clarifying questions to confirm the learner
understands inputs, outputs, and edge cases. Then ask what approach they're thinking
of. Do **not** volunteer the optimal approach yet.

## Step 5 — Pick language & scaffold

Ask which language they want: **Python**, **JavaScript**, **TypeScript**, or **Java**
(unless they already said). Then scaffold `solutions/<categorySlug>/<id>.<ext>`:

- A header comment: title, difficulty, LeetCode link.
- A function/method stub with the correct signature and a `TODO` body.
- A few example-based assertions derived from the statement so they can run-and-check.

Extension/run map (also in `CLAUDE.md`):

| Language   | ext     | run                                                   |
|------------|---------|-------------------------------------------------------|
| Python     | `.py`   | `python3 <file>`                                      |
| JavaScript | `.js`   | `node <file>`                                         |
| TypeScript | `.ts`   | `npx ts-node <file>`                                  |
| Java       | `.java` | `cd <dir> && javac <Id>.java && java <Id>`            |

(For Java, name the class/file in PascalCase, e.g. `TwoSum.java`.)

Update the problem's progress record: set `status: "in_progress"`, `language`,
`startedAt` (today, YYYY-MM-DD), and increment `attempts`.

## Step 6 — Socratic hint loop

- Give **one hint at a time**. Start high-level (which pattern/data structure to
  consider), escalate toward specifics only as the learner gets stuck or asks.
- Each time you give a substantive hint, increment `hintsUsed` in their record.
- Do **not** paste the full solution unless the learner explicitly asks
  ("show me the solution", "I give up", "just show the answer"). When they do, give
  the clean optimal solution **and** its time/space complexity, then offer a brief
  walkthrough.

## Step 7 — Review the attempt

When the learner has written code, help them run it (use the run command above).
Review for correctness against the examples and edge cases, then discuss time/space
complexity and possible improvements. Suggest fixes as guidance — let them edit.

## Step 8 — Record result

When the solution passes:
- Set `status: "solved"`, `solvedAt` (today), keep the final `language`,
  `attempts`, `hintsUsed`, and any short `notes`.
- Write `progress/progress.json`.
- Congratulate and offer the next problem (`/practice next`).

## Authoring a statement (lazy fill-in)

When a `problems/<cat>/<id>.md` file is missing, write it in your **own words**
(do not copy LeetCode verbatim). Use this template:

```markdown
# <Title>

- **Category:** <category> · **Difficulty:** <difficulty>
- **LeetCode:** <leetcodeUrl>
- **Patterns:** <comma-separated patterns>

## Problem
<2–5 sentence paraphrased description of the task.>

## Examples
**Example 1**
- Input: `...`
- Output: `...`
- Explanation: ...

**Example 2**
- Input: `...`
- Output: `...`

## Constraints
- <constraint>
- <constraint>
```
