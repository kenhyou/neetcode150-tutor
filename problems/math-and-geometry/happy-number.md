# Happy Number

- **Category:** Math & Geometry · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/happy-number/
- **Patterns:** Math, Fast & Slow Pointers

## Problem
A number is "happy" if repeatedly replacing it with the sum of the squares of its
digits eventually reaches `1`. If the process loops endlessly without hitting `1`, the
number is not happy. Given `n`, return `true` if it is a happy number.

## Examples
**Example 1**
- Input: `n = 19`
- Output: `true`  (`1+81=82 -> 68 -> 100 -> 1`)

**Example 2**
- Input: `n = 2`
- Output: `false`

## Constraints
- `1 <= n <= 2^31 - 1`
