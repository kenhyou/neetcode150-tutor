# Surrounded Regions

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/surrounded-regions/
- **Patterns:** DFS, BFS

## Problem
Given an `m x n` board of `'X'` and `'O'`, capture all regions of `'O'` that are fully
surrounded by `'X'` by flipping them to `'X'`. An `'O'` region is **not** captured if
any of its cells touches the border. Modify the board in place.

## Examples
**Example 1**
- Input: `board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`
- Output: `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`

**Example 2**
- Input: `board = [["X"]]`
- Output: `[["X"]]`

## Constraints
- `1 <= m, n <= 200`
- Each cell is `'X'` or `'O'`.
