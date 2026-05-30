# Word Break

- **Category:** 1-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/word-break/
- **Patterns:** DP

## Problem
Given a string `s` and a dictionary `wordDict`, return `true` if `s` can be segmented
into a space-separated sequence of one or more dictionary words. Dictionary words may
be reused any number of times.

## Examples
**Example 1**
- Input: `s = "leetcode"`, `wordDict = ["leet", "code"]`
- Output: `true`

**Example 2**
- Input: `s = "applepenapple"`, `wordDict = ["apple", "pen"]`
- Output: `true`

**Example 3**
- Input: `s = "catsandog"`, `wordDict = ["cats","dog","sand","and","cat"]`
- Output: `false`

## Constraints
- `1 <= s.length <= 300`, `1 <= wordDict.length <= 1000`
- Dictionary words are unique; all lowercase English letters.
