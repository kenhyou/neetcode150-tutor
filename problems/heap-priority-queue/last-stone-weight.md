# Last Stone Weight

- **Category:** Heap / Priority Queue · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/last-stone-weight/
- **Patterns:** Heap

## Problem
You have stones with positive integer weights. Each turn, smash the two heaviest
stones together: if equal, both are destroyed; otherwise the lighter is destroyed and
the heavier becomes their difference. Return the weight of the last remaining stone,
or `0` if none remain.

## Examples
**Example 1**
- Input: `stones = [2, 7, 4, 1, 8, 1]`
- Output: `1`

**Example 2**
- Input: `stones = [1]`
- Output: `1`

## Constraints
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`
