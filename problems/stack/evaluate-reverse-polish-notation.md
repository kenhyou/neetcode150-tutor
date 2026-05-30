# Evaluate Reverse Polish Notation

- **Category:** Stack · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/evaluate-reverse-polish-notation/
- **Patterns:** Stack

## Problem
Evaluate the value of an arithmetic expression given in Reverse Polish Notation
(postfix). Valid operators are `+`, `-`, `*`, `/`; each operand is an integer.
Division truncates toward zero. The input is always a valid expression.

## Examples
**Example 1**
- Input: `tokens = ["2", "1", "+", "3", "*"]`
- Output: `9`
- Explanation: `((2 + 1) * 3)`.

**Example 2**
- Input: `tokens = ["4", "13", "5", "/", "+"]`
- Output: `6`
- Explanation: `(4 + (13 / 5))`.

## Constraints
- `1 <= tokens.length <= 10^4`
- Each token is an operator or an integer in `[-200, 200]`.
