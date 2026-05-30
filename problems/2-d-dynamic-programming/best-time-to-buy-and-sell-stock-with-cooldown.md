# Best Time to Buy and Sell Stock with Cooldown

- **Category:** 2-D Dynamic Programming · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
- **Patterns:** DP, State Machine

## Problem
Given an array `prices` of daily stock prices, find the maximum profit from as many
buy/sell transactions as you like, with two rules: you can hold at most one share at a
time, and after you sell you must wait one day (cooldown) before buying again.

## Examples
**Example 1**
- Input: `prices = [1, 2, 3, 0, 2]`
- Output: `3`  (buy, sell, cooldown, buy, sell)

**Example 2**
- Input: `prices = [1]`
- Output: `0`

## Constraints
- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`
