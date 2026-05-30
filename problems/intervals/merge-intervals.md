# Merge Intervals

- **Category:** Intervals · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/merge-intervals/
- **Patterns:** Intervals, Sorting

## Problem
Given an array of `intervals` where `intervals[i] = [start, end]`, merge all
overlapping intervals and return the non-overlapping intervals that cover all the
input ranges.

## Examples
**Example 1**
- Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
- Output: `[[1,6],[8,10],[15,18]]`

**Example 2**
- Input: `intervals = [[1,4],[4,5]]`
- Output: `[[1,5]]`

## Constraints
- `1 <= intervals.length <= 10^4`
- `0 <= start <= end <= 10^4`
