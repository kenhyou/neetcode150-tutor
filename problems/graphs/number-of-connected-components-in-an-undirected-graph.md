# Number of Connected Components in an Undirected Graph

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
- **Patterns:** Union Find, DFS

## Problem
Given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, return the
number of connected components in the graph.

## Examples
**Example 1**
- Input: `n = 5`, `edges = [[0,1],[1,2],[3,4]]`
- Output: `2`

**Example 2**
- Input: `n = 5`, `edges = [[0,1],[1,2],[2,3],[3,4]]`
- Output: `1`

## Constraints
- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`, no self-loops or duplicate edges.
