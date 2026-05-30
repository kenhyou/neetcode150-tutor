# Min Cost Climbing Stairs

- **Category:** 1-D Dynamic Programming · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/min-cost-climbing-stairs/
- **Patterns:** DP

## Problem
Given an array `cost` where `cost[i]` is the cost of step `i`, you pay the cost to step
on `i` then climb 1 or 2 steps. You may start at index 0 or index 1. Return the
minimum total cost to reach the top (just past the last step).

## Examples
**Example 1**
- Input: `cost = [10, 15, 20]`
- Output: `15`

**Example 2**
- Input: `cost = [1,100,1,1,1,100,1,1,100,1]`
- Output: `6`

## Constraints
- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`
