# Regular Expression Matching

- **Category:** 2-D Dynamic Programming · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/regular-expression-matching/
- **Patterns:** DP

## Problem
Implement regular expression matching with support for `.` (matches any single
character) and `*` (matches zero or more of the **preceding** element). Given an input
string `s` and a pattern `p`, return `true` if the pattern matches the **entire**
string.

## Examples
**Example 1**
- Input: `s = "aa"`, `p = "a*"`
- Output: `true`

**Example 2**
- Input: `s = "ab"`, `p = ".*"`
- Output: `true`

**Example 3**
- Input: `s = "mississippi"`, `p = "mis*is*p*."`
- Output: `false`

## Constraints
- `1 <= s.length <= 20`, `1 <= p.length <= 30`
- `s` is lowercase letters; `p` is lowercase letters, `.`, and `*`; each `*` has a
  valid preceding element.
