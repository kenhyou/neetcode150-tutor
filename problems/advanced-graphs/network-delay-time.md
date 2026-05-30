# Network Delay Time

- **Category:** Advanced Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/network-delay-time/
- **Patterns:** Dijkstra

## Problem
A network has `n` nodes labeled `1`–`n`. `times[i] = [u, v, w]` is a directed edge
from `u` to `v` taking `w` time. A signal starts at node `k`. Return the time for all
nodes to receive it, or `-1` if some node is unreachable.

## Examples
**Example 1**
- Input: `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`
- Output: `2`

**Example 2**
- Input: `times = [[1,2,1]]`, `n = 2`, `k = 2`
- Output: `-1`

## Constraints
- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`, `1 <= w <= 100`, no self-loops or duplicate edges.
