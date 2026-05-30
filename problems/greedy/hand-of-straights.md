# Hand of Straights

- **Category:** Greedy · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/hand-of-straights/
- **Patterns:** Greedy, Heap

## Problem
Given an array `hand` of integers and a group size `groupSize`, return `true` if the
cards can be rearranged into groups of `groupSize` consecutive cards each.

## Examples
**Example 1**
- Input: `hand = [1,2,3,6,2,3,4,7,8]`, `groupSize = 3`
- Output: `true`  (`[1,2,3]`, `[2,3,4]`, `[6,7,8]`)

**Example 2**
- Input: `hand = [1, 2, 3, 4, 5]`, `groupSize = 4`
- Output: `false`

## Constraints
- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`, `1 <= groupSize <= hand.length`.
