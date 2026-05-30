# Word Search II

- **Category:** Tries · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/word-search-ii/
- **Patterns:** Trie, Backtracking

## Problem
Given an `m x n` board of characters and a list of `words`, return all words from the
list that can be formed by sequentially adjacent cells (horizontally or vertically).
A single cell may not be used more than once within the same word.

## Examples
**Example 1**
- Input: `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`,
  `words = ["oath","pea","eat","rain"]`
- Output: `["eat", "oath"]`

**Example 2**
- Input: `board = [["a","b"],["c","d"]]`, `words = ["abcb"]`
- Output: `[]`

## Constraints
- `1 <= m, n <= 12`
- `1 <= words.length <= 3 * 10^4`, each word `1`–`10` lowercase letters.
