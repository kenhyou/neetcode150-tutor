# Daily Temperatures

- **Category:** Stack · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/daily-temperatures/
- **Patterns:** Monotonic Stack

## Problem
Given an array `temperatures`, return an array `answer` such that `answer[i]` is the
number of days you must wait after day `i` to get a warmer temperature. If no warmer
day exists, set `answer[i] = 0`.

## Examples
**Example 1**
- Input: `temperatures = [73,74,75,71,69,72,76,73]`
- Output: `[1,1,4,2,1,1,0,0]`

**Example 2**
- Input: `temperatures = [30, 40, 50, 60]`
- Output: `[1, 1, 1, 0]`

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
