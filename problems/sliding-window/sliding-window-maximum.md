# Sliding Window Maximum

- **Category:** Sliding Window · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/sliding-window-maximum/
- **Patterns:** Monotonic Deque

## Problem
Given an integer array `nums` and a window size `k`, the window slides from the left
end to the right end, one position at a time. Return an array of the maximum value
within each window position.

## Examples
**Example 1**
- Input: `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
- Output: `[3, 3, 5, 5, 6, 7]`

**Example 2**
- Input: `nums = [1]`, `k = 1`
- Output: `[1]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`
