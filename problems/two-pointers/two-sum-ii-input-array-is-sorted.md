# Two Sum II - Input Array Is Sorted

- **Category:** Two Pointers · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
- **Patterns:** Two Pointers

## Problem
Given a **1-indexed** array `numbers` sorted in non-decreasing order, find the two
elements that add up to a given `target`. Return their 1-based indices `[i, j]` with
`i < j`. Exactly one solution exists, and you must use only `O(1)` extra space (no
hash map).

## Examples
**Example 1**
- Input: `numbers = [2, 7, 11, 15]`, `target = 9`
- Output: `[1, 2]`

**Example 2**
- Input: `numbers = [2, 3, 4]`, `target = 6`
- Output: `[1, 3]`

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`, sorted non-decreasing.
- Exactly one valid answer exists.
