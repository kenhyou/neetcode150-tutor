# Best Time to Buy and Sell Stock

- **Category:** Sliding Window · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
- **Patterns:** Sliding Window

## Problem
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.
You may buy on one day and sell on a later day. Return the maximum profit you can
make from a single buy/sell. If no profit is possible, return `0`.

## Examples
**Example 1**
- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `5`
- Explanation: Buy at 1 (day 2), sell at 6 (day 5).

**Example 2**
- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
