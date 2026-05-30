# Combination Sum

- **Category:** Backtracking · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/combination-sum/
- **Patterns:** Backtracking

## Problem
Given an array of **distinct** integers `candidates` and a `target`, return all unique
combinations whose elements sum to `target`. The same candidate may be chosen an
unlimited number of times; two combinations are different only if their multiset of
chosen numbers differs.

## Examples
**Example 1**
- Input: `candidates = [2, 3, 6, 7]`, `target = 7`
- Output: `[[2,2,3],[7]]`

**Example 2**
- Input: `candidates = [2, 3, 5]`, `target = 8`
- Output: `[[2,2,2,2],[2,3,3],[3,5]]`

## Constraints
- `1 <= candidates.length <= 30`, values distinct.
- `2 <= candidates[i] <= 40`, `1 <= target <= 500`.
