# Linked List Cycle

- **Category:** Linked List · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/linked-list-cycle/
- **Patterns:** Fast & Slow Pointers

## Problem
Given the head of a linked list, return `true` if the list contains a cycle (some node
can be reached again by following `next` pointers), otherwise `false`. Aim for `O(1)`
extra space.

## Examples
**Example 1**
- Input: `head = [3, 2, 0, -4]` with the tail connecting back to index 1.
- Output: `true`

**Example 2**
- Input: `head = [1]`, no cycle.
- Output: `false`

## Constraints
- The list has `0` to `10^4` nodes.
- `-10^5 <= Node.val <= 10^5`
