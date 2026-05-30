# Longest Repeating Character Replacement

- **Category:** Sliding Window · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/longest-repeating-character-replacement/
- **Patterns:** Sliding Window

## Problem
Given a string `s` of uppercase English letters and an integer `k`, you may change at
most `k` characters to any other uppercase letter. Return the length of the longest
substring containing a single repeated letter that you can produce after these
changes.

## Examples
**Example 1**
- Input: `s = "ABAB"`, `k = 2`
- Output: `4`

**Example 2**
- Input: `s = "AABABBA"`, `k = 1`
- Output: `4`
- Explanation: Change one `B` so `"AABA"` -> `"AAAA"` style window of length 4.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of uppercase English letters.
- `0 <= k <= s.length`
