# Minimum Window Substring

- **Category:** Sliding Window · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/minimum-window-substring/
- **Patterns:** Sliding Window

## Problem
Given strings `s` and `t`, return the shortest substring of `s` that contains every
character of `t` (including multiplicities). If no such window exists, return the
empty string `""`. The answer is guaranteed unique.

## Examples
**Example 1**
- Input: `s = "ADOBECODEBANC"`, `t = "ABC"`
- Output: `"BANC"`

**Example 2**
- Input: `s = "a"`, `t = "a"`
- Output: `"a"`

**Example 3**
- Input: `s = "a"`, `t = "aa"`
- Output: `""`

## Constraints
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.
