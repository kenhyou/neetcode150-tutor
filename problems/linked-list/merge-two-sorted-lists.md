# Merge Two Sorted Lists

- **Category:** Linked List · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/merge-two-sorted-lists/
- **Patterns:** Linked List

## Problem
Given the heads of two sorted singly linked lists, splice them together into one
sorted list by reusing the existing nodes, and return the head of the merged list.

## Examples
**Example 1**
- Input: `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`
- Output: `[1, 1, 2, 3, 4, 4]`

**Example 2**
- Input: `list1 = []`, `list2 = [0]`
- Output: `[0]`

## Constraints
- Each list has `0` to `50` nodes.
- `-100 <= Node.val <= 100`, both sorted non-decreasing.
