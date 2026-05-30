# Gas Station

- **Category:** Greedy · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/gas-station/
- **Patterns:** Greedy

## Problem
There are `n` gas stations in a circle. `gas[i]` is the fuel at station `i`, and
`cost[i]` is the fuel needed to travel from station `i` to `i + 1`. With an empty tank,
return the starting station index from which you can complete the full loop, or `-1`
if impossible. A unique answer is guaranteed when one exists.

## Examples
**Example 1**
- Input: `gas = [1, 2, 3, 4, 5]`, `cost = [3, 4, 5, 1, 2]`
- Output: `3`

**Example 2**
- Input: `gas = [2, 3, 4]`, `cost = [3, 4, 3]`
- Output: `-1`

## Constraints
- `n == gas.length == cost.length`, `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`
