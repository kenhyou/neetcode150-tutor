# Redundant Connection

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/redundant-connection/
- **Patterns:** Union Find

## Problem
A tree with `n` nodes (labeled `1`–`n`) had exactly one extra edge added, forming a
single cycle. Given `edges`, return the one edge that can be removed so the result is
again a tree. If multiple answers exist, return the one that appears last in `edges`.

## Examples
**Example 1**
- Input: `edges = [[1,2],[1,3],[2,3]]`
- Output: `[2, 3]`

**Example 2**
- Input: `edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]`
- Output: `[1, 4]`

## Constraints
- `n == edges.length`, `3 <= n <= 1000`
- No repeated edges or self-loops; the graph is connected.
