# Max Area of Island

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/max-area-of-island/
- **Patterns:** DFS, BFS

## Problem
Given an `m x n` binary grid where `1` is land and `0` is water, return the area (cell
count) of the largest island. Cells connect horizontally or vertically. If there is no
island, return `0`.

## Examples
**Example 1**
- Input: a grid whose largest connected land region has 6 cells.
- Output: `6`

**Example 2**
- Input: `grid = [[0,0,0],[0,0,0]]`
- Output: `0`

## Constraints
- `1 <= m, n <= 50`
- Each cell is `0` or `1`.
