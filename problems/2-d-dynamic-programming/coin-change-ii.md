# Coin Change II

- **Category:** 2-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/coin-change-ii/
- **Patterns:** DP, Unbounded Knapsack

## Problem
Given an `amount` and coin denominations `coins` (unlimited supply of each), return the
number of distinct combinations that make up the amount. Combinations differing only
in order count as one.

## Examples
**Example 1**
- Input: `amount = 5`, `coins = [1, 2, 5]`
- Output: `4`

**Example 2**
- Input: `amount = 3`, `coins = [2]`
- Output: `0`

## Constraints
- `1 <= coins.length <= 300`, coins distinct.
- `1 <= coins[i] <= 5000`, `0 <= amount <= 5000`.
