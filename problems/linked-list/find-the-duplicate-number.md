# Find the Duplicate Number

- **Category:** Linked List · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/find-the-duplicate-number/
- **Patterns:** Fast & Slow Pointers

## Problem
Given an array `nums` of `n + 1` integers where each value is in the range
`[1, n]`, there is exactly one value that is repeated (possibly multiple times).
Return that duplicate **without modifying the array** and using only `O(1)` extra
space.

## Examples
**Example 1**
- Input: `nums = [1, 3, 4, 2, 2]`
- Output: `2`

**Example 2**
- Input: `nums = [3, 1, 3, 4, 2]`
- Output: `3`

## Constraints
- `1 <= n <= 10^5`, `nums.length == n + 1`
- `1 <= nums[i] <= n`, exactly one value repeats.
