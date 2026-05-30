# Alien Dictionary

- **Category:** Advanced Graphs · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/alien-dictionary/
- **Patterns:** Topological Sort

## Problem
A new language uses lowercase letters in an unknown order. Given a list of `words`
sorted according to this language's alphabet, derive any valid ordering of its letters
as a string. If the ordering is invalid (contradictory), return `""`. If multiple
orderings are valid, any is accepted.

## Examples
**Example 1**
- Input: `words = ["wrt","wrf","er","ett","rftt"]`
- Output: `"wertf"`

**Example 2**
- Input: `words = ["z", "x"]`
- Output: `"zx"`

**Example 3**
- Input: `words = ["abc", "ab"]`  (prefix appears after its extension)
- Output: `""`

## Constraints
- `1 <= words.length <= 100`, `1 <= words[i].length <= 100`, lowercase letters.
