# Graph Valid Tree

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/graph-valid-tree/
- **Patterns:** Union Find, DFS

## Problem
Given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, return `true`
if these edges form a valid tree — the graph is fully connected and contains no
cycles.

## Examples
**Example 1**
- Input: `n = 5`, `edges = [[0,1],[0,2],[0,3],[1,4]]`
- Output: `true`

**Example 2**
- Input: `n = 5`, `edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]`
- Output: `false`

## Constraints
- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`, no self-loops or duplicate edges.
