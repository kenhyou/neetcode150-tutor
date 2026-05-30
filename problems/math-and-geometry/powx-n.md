# Pow(x, n)

- **Category:** Math & Geometry · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/powx-n/
- **Patterns:** Math, Fast Exponentiation

## Problem
Implement `pow(x, n)`, which raises `x` (a double) to the integer power `n`. Handle
negative exponents. Aim for `O(log n)` time.

## Examples
**Example 1**
- Input: `x = 2.00000`, `n = 10`
- Output: `1024.00000`

**Example 2**
- Input: `x = 2.10000`, `n = 3`
- Output: `9.26100`

**Example 3**
- Input: `x = 2.00000`, `n = -2`
- Output: `0.25000`

## Constraints
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`, and either `x != 0` or `n > 0`.
