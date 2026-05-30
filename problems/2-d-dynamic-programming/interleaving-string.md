# Interleaving String

- **Category:** 2-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/interleaving-string/
- **Patterns:** DP

## Problem
Given strings `s1`, `s2`, and `s3`, return `true` if `s3` is formed by interleaving
`s1` and `s2` — i.e. `s3` can be split into pieces that, read in order, alternate
between (preserving order of) the characters of `s1` and `s2`.

## Examples
**Example 1**
- Input: `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbcbcac"`
- Output: `true`

**Example 2**
- Input: `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbbaccc"`
- Output: `false`

**Example 3**
- Input: `s1 = ""`, `s2 = ""`, `s3 = ""`
- Output: `true`

## Constraints
- `0 <= s1.length, s2.length <= 100`, `0 <= s3.length <= 200`
- All strings consist of lowercase English letters.
