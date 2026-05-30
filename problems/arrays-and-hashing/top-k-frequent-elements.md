# Top K Frequent Elements

- **Category:** Arrays & Hashing · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/top-k-frequent-elements/
- **Patterns:** Bucket Sort, Heap

## Problem
Given an integer array `nums` and an integer `k`, return the `k` most frequently
occurring elements. The answer may be returned in any order, and it is guaranteed to
be unique.

## Examples
**Example 1**
- Input: `nums = [1, 1, 1, 2, 2, 3]`, `k = 2`
- Output: `[1, 2]`

**Example 2**
- Input: `nums = [1]`, `k = 1`
- Output: `[1]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= ` number of distinct elements in `nums`.

**Follow-up:** Can you do better than `O(n log n)` time?
