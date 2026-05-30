# Merge Triplets to Form Target Triplet

- **Category:** Greedy · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/merge-triplets-to-form-target-triplet/
- **Patterns:** Greedy

## Problem
You have a list of `triplets` `[a, b, c]` and a `target` triplet. You may repeatedly
pick two triplets and replace them with their element-wise maximum. Return `true` if
it is possible to obtain the `target` triplet using some sequence of such merges.

## Examples
**Example 1**
- Input: `triplets = [[2,5,3],[1,8,4],[1,7,5]]`, `target = [2, 7, 5]`
- Output: `true`

**Example 2**
- Input: `triplets = [[3,4,5],[4,5,6]]`, `target = [3, 2, 5]`
- Output: `false`

## Constraints
- `1 <= triplets.length <= 10^5`
- `1 <= ai, bi, ci, target values <= 1000`
