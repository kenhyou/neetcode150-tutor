# Longest Increasing Subsequence

- **Category:** 1-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/longest-increasing-subsequence/
- **Patterns:** DP, Binary Search

## Problem
Given an integer array `nums`, return the length of the longest strictly increasing
subsequence (elements need not be contiguous, but must keep their relative order).

## Examples
**Example 1**
- Input: `nums = [10, 9, 2, 5, 3, 7, 101, 18]`
- Output: `4`  (e.g. `[2, 3, 7, 101]`)

**Example 2**
- Input: `nums = [0, 1, 0, 3, 2, 3]`
- Output: `4`

## Constraints
- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

**Follow-up:** Can you achieve `O(n log n)` time?
