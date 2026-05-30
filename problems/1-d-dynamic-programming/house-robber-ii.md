# House Robber II

- **Category:** 1-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/house-robber-ii/
- **Patterns:** DP

## Problem
Same as House Robber, but the houses are arranged in a **circle**: the first and last
houses are adjacent. Return the maximum amount you can rob without taking from two
adjacent houses.

## Examples
**Example 1**
- Input: `nums = [2, 3, 2]`
- Output: `3`  (you cannot rob both house 0 and house 2)

**Example 2**
- Input: `nums = [1, 2, 3, 1]`
- Output: `4`

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`
