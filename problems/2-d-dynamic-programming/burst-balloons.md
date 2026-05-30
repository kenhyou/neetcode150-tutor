# Burst Balloons

- **Category:** 2-D Dynamic Programming · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/burst-balloons/
- **Patterns:** DP, Interval DP

## Problem
Given `n` balloons with values in `nums`, bursting balloon `i` earns
`nums[i-1] * nums[i] * nums[i+1]` coins (treat out-of-range neighbors as `1`). After a
burst its neighbors become adjacent. Return the maximum coins you can collect by
bursting all balloons in some order.

## Examples
**Example 1**
- Input: `nums = [3, 1, 5, 8]`
- Output: `167`

**Example 2**
- Input: `nums = [1, 5]`
- Output: `10`

## Constraints
- `1 <= n <= 300`
- `0 <= nums[i] <= 100`
