# Task Scheduler

- **Category:** Heap / Priority Queue · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/task-scheduler/
- **Patterns:** Heap, Greedy

## Problem
Given an array of CPU `tasks` labeled A–Z and a cooldown `n`, each task takes one unit
of time. Two identical tasks must be separated by at least `n` units; the CPU may be
idle. Return the minimum total time units needed to finish all tasks.

## Examples
**Example 1**
- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- Output: `8`
- Explanation: e.g. `A B idle A B idle A B`.

**Example 2**
- Input: `tasks = ["A","C","A","B","D","B"]`, `n = 1`
- Output: `6`

## Constraints
- `1 <= tasks.length <= 10^4`, tasks are uppercase letters.
- `0 <= n <= 100`
