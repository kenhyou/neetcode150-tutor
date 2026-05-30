# Reorder List

- **Category:** Linked List · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/reorder-list/
- **Patterns:** Linked List, Two Pointers

## Problem
Given the head of a singly linked list `L0 -> L1 -> ... -> Ln-1 -> Ln`, reorder it
**in place** to `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`. You may not change node
values, only relink nodes.

## Examples
**Example 1**
- Input: `head = [1, 2, 3, 4]`
- Output: `[1, 4, 2, 3]`

**Example 2**
- Input: `head = [1, 2, 3, 4, 5]`
- Output: `[1, 5, 2, 4, 3]`

## Constraints
- The list has `1` to `5 * 10^4` nodes.
- `1 <= Node.val <= 1000`
