# Decode Ways

- **Category:** 1-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/decode-ways/
- **Patterns:** DP

## Problem
A message of digits is encoded with the mapping `1 -> A`, `2 -> B`, ..., `26 -> Z`.
Given a digit string `s`, return the number of ways to decode it. Leading zeros are
invalid (e.g. `"06"` cannot be decoded).

## Examples
**Example 1**
- Input: `s = "12"`
- Output: `2`  (`"AB"` or `"L"`)

**Example 2**
- Input: `s = "226"`
- Output: `3`  (`"BBF"`, `"BZ"`, `"VF"`)

**Example 3**
- Input: `s = "06"`
- Output: `0`

## Constraints
- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zeros.
