# Permutation in String

- **Category:** Sliding Window · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/permutation-in-string/
- **Patterns:** Sliding Window

## Problem
Given two strings `s1` and `s2`, return `true` if `s2` contains a substring that is a
permutation of `s1` (i.e. one of `s1`'s anagrams appears as a contiguous block in
`s2`). Otherwise return `false`.

## Examples
**Example 1**
- Input: `s1 = "ab"`, `s2 = "eidbaooo"`
- Output: `true`
- Explanation: `s2` contains `"ba"`, a permutation of `"ab"`.

**Example 2**
- Input: `s1 = "ab"`, `s2 = "eidboaoo"`
- Output: `false`

## Constraints
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.
