# Pacific Atlantic Water Flow

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/pacific-atlantic-water-flow/
- **Patterns:** DFS, BFS

## Problem
Given an `m x n` matrix of cell heights, the Pacific ocean touches the top and left
edges, the Atlantic touches the bottom and right edges. Water flows from a cell to a
neighbor of **equal or lower** height. Return all cells `[r, c]` from which water can
reach **both** oceans.

## Examples
**Example 1**
- Input: `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
- Output: `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

**Example 2**
- Input: `heights = [[1]]`
- Output: `[[0, 0]]`

## Constraints
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`
