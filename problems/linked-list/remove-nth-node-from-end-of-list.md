# Remove Nth Node From End of List

- **Category:** Linked List · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- **Patterns:** Two Pointers

## Problem
Given the head of a linked list, remove the `n`-th node counting from the end and
return the head. Try to do it in a single pass.

## Examples
**Example 1**
- Input: `head = [1, 2, 3, 4, 5]`, `n = 2`
- Output: `[1, 2, 3, 5]`

**Example 2**
- Input: `head = [1]`, `n = 1`
- Output: `[]`

## Constraints
- The list has `1` to `30` nodes.
- `0 <= Node.val <= 100`
- `1 <= n <= list length`
