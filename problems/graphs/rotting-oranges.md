# Rotting Oranges

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/rotting-oranges/
- **Patterns:** BFS

## Problem
In an `m x n` grid, each cell is `0` (empty), `1` (fresh orange), or `2` (rotten). Each
minute, any fresh orange adjacent (4-directionally) to a rotten one becomes rotten.
Return the minimum minutes until no fresh orange remains, or `-1` if impossible.

## Examples
**Example 1**
- Input: `grid = [[2,1,1],[1,1,0],[0,1,1]]`
- Output: `4`

**Example 2**
- Input: `grid = [[2,1,1],[0,1,1],[1,0,1]]`
- Output: `-1`

## Constraints
- `1 <= m, n <= 10`
- Each cell is `0`, `1`, or `2`.
