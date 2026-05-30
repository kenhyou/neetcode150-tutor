# Min Stack

- **Category:** Stack · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/min-stack/
- **Patterns:** Stack, Design

## Problem
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element,
all in `O(1)` time. Implement the class:

- `push(val)` — push `val` onto the stack.
- `pop()` — remove the top element.
- `top()` — return the top element.
- `getMin()` — return the smallest element currently in the stack.

## Examples
**Example 1**
- Operations: `push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`
- Output: `-3`, then `0`, then `-2`

## Constraints
- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top`, `getMin` are always called on a non-empty stack.
- At most `3 * 10^4` calls total.
