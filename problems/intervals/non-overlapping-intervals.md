# Non-overlapping Intervals

- **Category:** Intervals · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/non-overlapping-intervals/
- **Patterns:** Intervals, Greedy

## Problem
Given an array of `intervals`, return the minimum number of intervals you must remove
so that the rest are non-overlapping. Intervals that merely touch at an endpoint
(e.g. `[1,2]` and `[2,3]`) are not considered overlapping.

## Examples
**Example 1**
- Input: `intervals = [[1,2],[2,3],[3,4],[1,3]]`
- Output: `1`

**Example 2**
- Input: `intervals = [[1,2],[1,2],[1,2]]`
- Output: `2`

## Constraints
- `1 <= intervals.length <= 10^5`
- `-5 * 10^4 <= start < end <= 5 * 10^4`
