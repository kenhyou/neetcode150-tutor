# Word Search

- **Category:** Backtracking · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/word-search/
- **Patterns:** Backtracking, DFS, Matrix

## Problem
Given an `m x n` grid of characters `board` and a string `word`, return `true` if
`word` can be spelled out by a path of horizontally/vertically adjacent cells. The
same cell may not be reused within the path.

## Examples
**Example 1**
- Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`
- Output: `true`

**Example 2**
- Input: same board, `word = "ABCB"`
- Output: `false`

## Constraints
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`, all uppercase/lowercase English letters.
