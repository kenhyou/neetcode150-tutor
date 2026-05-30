# Longest Consecutive Sequence

- **Category:** Arrays & Hashing · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/longest-consecutive-sequence/
- **Patterns:** Hash Set

## Problem
Given an unsorted integer array `nums`, return the length of the longest run of
consecutive integers (e.g. `3, 4, 5, 6`) that can be formed from its values. The
numbers do not need to be adjacent in the array. You must solve it in `O(n)` time.

## Examples
**Example 1**
- Input: `nums = [100, 4, 200, 1, 3, 2]`
- Output: `4`
- Explanation: The consecutive run `1, 2, 3, 4` has length 4.

**Example 2**
- Input: `nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`
- Output: `9`

## Constraints
- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
