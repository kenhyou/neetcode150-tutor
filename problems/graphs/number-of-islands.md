# Number of Islands

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/number-of-islands/
- **Patterns:** DFS, BFS, Union Find

## Problem
Given an `m x n` grid of `'1'` (land) and `'0'` (water), return the number of islands.
An island is a maximal group of land cells connected horizontally or vertically; all
edges of the grid are surrounded by water.

## Examples
**Example 1**
- Input: `grid = [["1","1","0","0"],["1","1","0","0"],["0","0","1","0"],["0","0","0","1"]]`
- Output: `3`

**Example 2**
- Input: `grid = [["1","1","1"],["0","1","0"],["1","1","1"]]`
- Output: `1`

## Constraints
- `1 <= m, n <= 300`
- Each cell is `'0'` or `'1'`.
