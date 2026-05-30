# Reverse Nodes in k-Group

- **Category:** Linked List · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/reverse-nodes-in-k-group/
- **Patterns:** Linked List

## Problem
Given the head of a linked list, reverse the nodes `k` at a time and return the
modified list. If the number of remaining nodes is fewer than `k`, leave them as-is.
You may not change node values, only relink nodes.

## Examples
**Example 1**
- Input: `head = [1,2,3,4,5]`, `k = 2`
- Output: `[2,1,4,3,5]`

**Example 2**
- Input: `head = [1,2,3,4,5]`, `k = 3`
- Output: `[3,2,1,4,5]`

## Constraints
- The list has `1` to `5000` nodes.
- `0 <= Node.val <= 1000`, `1 <= k <= n`.

**Follow-up:** Can you do it using only `O(1)` extra memory?
