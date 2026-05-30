# Cheapest Flights Within K Stops

- **Category:** Advanced Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/cheapest-flights-within-k-stops/
- **Patterns:** Bellman-Ford, BFS

## Problem
There are `n` cities connected by `flights` `[from, to, price]`. Given `src`, `dst`,
and `k`, return the cheapest price to fly from `src` to `dst` using at most `k`
intermediate stops. If no such route exists, return `-1`.

## Examples
**Example 1**
- Input: `n = 4`, `flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]`,
  `src = 0`, `dst = 3`, `k = 1`
- Output: `700`

**Example 2**
- Input: `n = 3`, `flights = [[0,1,100],[1,2,100],[0,2,500]]`, `src = 0`, `dst = 2`, `k = 0`
- Output: `500`

## Constraints
- `1 <= n <= 100`, `0 <= flights.length <= n * (n - 1)`
- `0 <= src, dst, k < n`, `src != dst`, `1 <= price <= 10^4`.
