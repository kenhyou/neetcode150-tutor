# Insert Interval

- **Category:** Intervals · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/insert-interval/
- **Patterns:** Intervals

## Problem
Given a list of non-overlapping `intervals` sorted by start, and a `newInterval`,
insert the new interval and merge as needed so the result stays sorted and
non-overlapping. Return the resulting list.

## Examples
**Example 1**
- Input: `intervals = [[1,3],[6,9]]`, `newInterval = [2, 5]`
- Output: `[[1,5],[6,9]]`

**Example 2**
- Input: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4, 8]`
- Output: `[[1,2],[3,10],[12,16]]`

## Constraints
- `0 <= intervals.length <= 10^4`, sorted by start, non-overlapping.
- `0 <= start <= end <= 10^5`
