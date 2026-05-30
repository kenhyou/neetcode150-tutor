# Largest Rectangle in Histogram

- **Category:** Stack · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/largest-rectangle-in-histogram/
- **Patterns:** Monotonic Stack

## Problem
Given an array `heights` representing the bar heights of a histogram (each bar width
1), return the area of the largest rectangle that fits entirely within the histogram.

## Examples
**Example 1**
- Input: `heights = [2, 1, 5, 6, 2, 3]`
- Output: `10`
- Explanation: The bars of height 5 and 6 form a `5 x 2 = 10` rectangle.

**Example 2**
- Input: `heights = [2, 4]`
- Output: `4`

## Constraints
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`
