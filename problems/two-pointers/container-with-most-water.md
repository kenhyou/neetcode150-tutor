# Container With Most Water

- **Category:** Two Pointers · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/container-with-most-water/
- **Patterns:** Two Pointers, Greedy

## Problem
You are given an array `height` where `height[i]` is the height of a vertical line at
position `i`. Pick two lines that, together with the x-axis, form a container. Return
the maximum amount of water it can hold — i.e. maximize `min(height[i], height[j]) *
(j - i)`.

## Examples
**Example 1**
- Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- Output: `49`
- Explanation: Lines at index 1 and 8 give `min(8, 7) * (8 - 1) = 49`.

**Example 2**
- Input: `height = [1, 1]`
- Output: `1`

## Constraints
- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`
