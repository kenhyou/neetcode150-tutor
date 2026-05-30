# Swim in Rising Water

- **Category:** Advanced Graphs · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/swim-in-rising-water/
- **Patterns:** Dijkstra, Binary Search

## Problem
Given an `n x n` grid where `grid[r][c]` is the elevation at that cell, water rises so
that at time `t` every cell with elevation at most `t` is submerged. Starting at the
top-left cell at time 0, you can swim to a 4-directionally adjacent cell instantly only
if both cells are submerged. Return the least time to reach the bottom-right cell.

## Examples
**Example 1**
- Input: `grid = [[0,2],[1,3]]`
- Output: `3`

**Example 2**
- Input: `grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]`
- Output: `16`

## Constraints
- `1 <= n <= 50`
- `grid` is a permutation of `0 .. n*n - 1`.
