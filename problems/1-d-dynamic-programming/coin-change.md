# Coin Change

- **Category:** 1-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/coin-change/
- **Patterns:** DP

## Problem
Given coin denominations `coins` and a target `amount`, return the fewest number of
coins needed to make up that amount. You have an unlimited supply of each coin. If the
amount cannot be made, return `-1`.

## Examples
**Example 1**
- Input: `coins = [1, 2, 5]`, `amount = 11`
- Output: `3`  (`5 + 5 + 1`)

**Example 2**
- Input: `coins = [2]`, `amount = 3`
- Output: `-1`

## Constraints
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`, `0 <= amount <= 10^4`.
