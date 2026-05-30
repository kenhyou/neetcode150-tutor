# NeetCode 150 — Interactive Practice with Claude Code

A study kit for working through the [NeetCode 150](https://neetcode.io/practice)
with Claude Code as your **Socratic tutor**. Claude presents a problem, coaches you
with progressive hints (no spoilers unless you ask), lets you solve it in the
language of your choice, and tracks your progress.

Your own solutions and progress stay **local** — they are gitignored, so this repo
can be shared/cloned without leaking anyone's answers.

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Whichever language runtime you want to practice in:
  - Python 3 (`python3`)
  - Node.js (`node`) — and `npx ts-node` for TypeScript
  - JDK (`javac` / `java`) for Java

## Getting started

Open this folder in Claude Code and run:

```
/practice
```

That serves the next unsolved problem in NeetCode roadmap order. You can also:

```
/practice two sum                 # a specific problem (by title or id)
/practice sliding window          # next unsolved in a category
/practice next                    # next unsolved overall
/progress                         # see your dashboard
```

When a problem starts, Claude will:
1. Show the (paraphrased) problem statement + the LeetCode link.
2. Ask a couple of clarifying questions.
3. Ask which language you want and scaffold a starter file under `solutions/`.
4. Give you **one hint at a time** as you work. Ask "show me the solution" any time
   you want the full answer and complexity analysis.
5. Help you run your code and review correctness + time/space complexity.
6. Record the result in `progress/progress.json`.

## How it's organized

```
data/neetcode150.json     # the 150-problem index (id, category, difficulty, links)
problems/<category>/<id>.md   # paraphrased problem statements (shared)
solutions/<category>/<id>.<ext>   # YOUR code        (gitignored)
progress/progress.json    # YOUR progress           (gitignored)
.claude/skills/           # the /practice and /progress skills
CLAUDE.md                 # the tutor's behavior contract
```

Problem statements are authored on first visit and committed, so the library fills
in as people use the kit. The **Arrays & Hashing** category is pre-seeded so things
work right away.

## A note on spoilers

The tutor is deliberately hints-first and will not dump the solution on you. If you
want a guided walkthrough instead of the struggle, just say so at the start of a
problem.
