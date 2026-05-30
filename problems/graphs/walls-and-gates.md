# Walls and Gates

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/walls-and-gates/
- **Patterns:** BFS

## Problem
You are given an `m x n` grid where `-1` is a wall, `0` is a gate, and `INF`
(`2^31 - 1`) is an empty room. Fill each empty room with the distance to its nearest
gate (moving 4-directionally). If a room cannot reach any gate, leave it as `INF`.
Modify the grid in place.

## Examples
**Example 1**
- Input: `rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]`
- Output: `[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]`

**Example 2**
- Input: `rooms = [[-1]]`
- Output: `[[-1]]`

## Constraints
- `1 <= m, n <= 250`
- Each cell is `-1`, `0`, or `2^31 - 1`.
