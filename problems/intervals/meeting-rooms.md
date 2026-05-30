# Meeting Rooms

- **Category:** Intervals · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/meeting-rooms/
- **Patterns:** Intervals, Sorting

## Problem
Given an array of meeting time `intervals` `[start, end]`, determine whether a single
person could attend all meetings — i.e. no two meetings overlap. Meetings that end
exactly when another begins do not conflict.

## Examples
**Example 1**
- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `false`

**Example 2**
- Input: `intervals = [[7,10],[2,4]]`
- Output: `true`

## Constraints
- `0 <= intervals.length <= 10^4`
- `0 <= start < end <= 10^6`
