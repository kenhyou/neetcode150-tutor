# Product of Array Except Self

- **Category:** Arrays & Hashing · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/product-of-array-except-self/
- **Patterns:** Prefix/Suffix Products

## Problem
Given an integer array `nums`, return an array `answer` such that `answer[i]` equals
the product of every element of `nums` except `nums[i]`. You must solve it **without
using division**, and the intended solution runs in `O(n)` time.

## Examples
**Example 1**
- Input: `nums = [1, 2, 3, 4]`
- Output: `[24, 12, 8, 6]`

**Example 2**
- Input: `nums = [-1, 1, 0, -3, 3]`
- Output: `[0, 0, 9, 0, 0]`

## Constraints
- `2 <= nums.length <= 10^5`
- `-30 <= nums[i] <= 30`
- The product of any prefix or suffix fits in a 32-bit integer.

**Follow-up:** Can you do it using `O(1)` extra space (the output array doesn't count)?
