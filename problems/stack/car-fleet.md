# Car Fleet

- **Category:** Stack · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/car-fleet/
- **Patterns:** Stack, Sorting

## Problem
There are `n` cars heading to the same destination `target` miles away. Car `i` starts
at `position[i]` with constant `speed[i]`. A faster car cannot pass a slower one — it
catches up and they move together as one "fleet" (a fleet may be a single car).
Return how many fleets arrive at the destination.

## Examples
**Example 1**
- Input: `target = 12`, `position = [10, 8, 0, 5, 3]`, `speed = [2, 4, 1, 1, 3]`
- Output: `3`

**Example 2**
- Input: `target = 10`, `position = [3]`, `speed = [3]`
- Output: `1`

## Constraints
- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`, positions are distinct.
