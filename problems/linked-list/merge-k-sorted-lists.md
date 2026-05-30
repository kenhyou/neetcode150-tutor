# Merge k Sorted Lists

- **Category:** Linked List · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/merge-k-sorted-lists/
- **Patterns:** Heap, Linked List

## Problem
You are given an array of `k` linked lists, each sorted ascending. Merge them all into
a single sorted linked list and return its head.

## Examples
**Example 1**
- Input: `lists = [[1,4,5],[1,3,4],[2,6]]`
- Output: `[1,1,2,3,4,4,5,6]`

**Example 2**
- Input: `lists = []`
- Output: `[]`

## Constraints
- `0 <= k <= 10^4`
- Each list is sorted; total nodes `<= 10^4`.
- `-10^4 <= Node.val <= 10^4`
