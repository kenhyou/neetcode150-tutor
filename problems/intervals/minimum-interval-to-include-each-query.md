# Minimum Interval to Include Each Query

- **Category:** Intervals · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/minimum-interval-to-include-each-query/
- **Patterns:** Intervals, Heap

## Problem
Given a list of `intervals` `[left, right]` and an array of `queries`, for each query
`q` return the size (`right - left + 1`) of the **smallest** interval that contains
`q` (`left <= q <= right`). If no interval contains `q`, the answer is `-1`. Return the
answers in query order.

## Examples
**Example 1**
- Input: `intervals = [[1,4],[2,4],[3,6],[4,4]]`, `queries = [2, 3, 4, 5]`
- Output: `[3, 3, 1, 4]`

**Example 2**
- Input: `intervals = [[2,3],[2,5],[1,8],[20,25]]`, `queries = [2, 19, 5, 22]`
- Output: `[2, -1, 4, 6]`

## Constraints
- `1 <= intervals.length, queries.length <= 10^5`
- `1 <= left <= right <= 10^7`, `1 <= q <= 10^7`.
