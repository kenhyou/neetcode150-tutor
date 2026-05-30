# K Closest Points to Origin

- **Category:** Heap / Priority Queue · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/k-closest-points-to-origin/
- **Patterns:** Heap

## Problem
Given an array of `points` on the plane and an integer `k`, return the `k` points
closest to the origin `(0, 0)` by Euclidean distance. The answer may be in any order;
it is guaranteed unique except for order.

## Examples
**Example 1**
- Input: `points = [[1,3],[-2,2]]`, `k = 1`
- Output: `[[-2,2]]`

**Example 2**
- Input: `points = [[3,3],[5,-1],[-2,4]]`, `k = 2`
- Output: `[[3,3],[-2,4]]`

## Constraints
- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`
