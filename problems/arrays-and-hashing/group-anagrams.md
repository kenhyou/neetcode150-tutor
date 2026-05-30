# Group Anagrams

- **Category:** Arrays & Hashing · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/group-anagrams/
- **Patterns:** Hash Map

## Problem
Given an array of strings `strs`, group the strings that are anagrams of one another
into the same list. Return the groups in any order, and the strings within each group
in any order.

## Examples
**Example 1**
- Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]`

**Example 2**
- Input: `strs = [""]`
- Output: `[[""]]`

**Example 3**
- Input: `strs = ["a"]`
- Output: `[["a"]]`

## Constraints
- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.
