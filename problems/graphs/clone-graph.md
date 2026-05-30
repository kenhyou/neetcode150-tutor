# Clone Graph

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/clone-graph/
- **Patterns:** DFS, BFS, Hash Map

## Problem
Given a reference to a node in a connected, undirected graph, return a **deep copy** of
the entire graph. Each node holds an integer value and a list of its neighbors.

## Examples
**Example 1**
- Input: `adjList = [[2,4],[1,3],[2,4],[1,3]]`
- Output: a deep copy with the same structure.

**Example 2**
- Input: `adjList = [[]]` (a single node with no neighbors)
- Output: a single-node copy.

## Constraints
- `0 <= number of nodes <= 100`
- `1 <= Node.val <= 100`, values unique; the graph is connected and undirected.
