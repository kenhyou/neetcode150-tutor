# Longest Increasing Path in a Matrix

- **Category:** 2-D Dynamic Programming · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
- **Patterns:** DP, DFS, Memoization

## Problem
Given an `m x n` integer matrix, return the length of the longest strictly increasing
path. From a cell you may move to a 4-directionally adjacent cell with a strictly
greater value; you may not move diagonally or wrap around.

## Examples
**Example 1**
- Input: `matrix = [[9,9,4],[6,6,8],[2,1,1]]`
- Output: `4`  (`1 -> 2 -> 6 -> 9`)

**Example 2**
- Input: `matrix = [[3,4,5],[3,2,6],[2,2,1]]`
- Output: `4`  (`3 -> 4 -> 5 -> 6`)

## Constraints
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`
