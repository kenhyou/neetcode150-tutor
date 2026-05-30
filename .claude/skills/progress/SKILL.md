---
name: progress
description: Show the learner's NeetCode 150 progress dashboard. Use when the user runs /progress or asks how far along they are, what's solved/remaining, or what to do next.
---

# /progress — NeetCode 150 dashboard

Read-only. Summarize the learner's progress from their local records.

## Steps

1. Read `data/neetcode150.json` (all 150 problems).
2. Read `progress/progress.json`. If it doesn't exist, report that no problems have
   been started yet and suggest running `/practice` to begin. Do not create it here.
3. For each problem, derive status from the record (`solved` / `in_progress` /
   otherwise `not_started`).

## Output

Render a concise dashboard:

- **Overall:** `solved / 150` with a simple text progress bar, plus counts of
  in-progress and not-started.
- **By category:** for each of the 18 categories, `solved / total` (and flag any
  in-progress). Show in roadmap (`categoryOrder`) order.
- **Recent:** the last few solved problems with their `solvedAt` date, `language`,
  `attempts`, and `hintsUsed` if available.
- **Next up:** the first not-`solved` problem in roadmap order, with a nudge to run
  `/practice next`.

Keep it scannable. Do not modify any files.
