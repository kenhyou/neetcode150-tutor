# Set Matrix Zeroes

- **Category:** Math & Geometry · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/set-matrix-zeroes/
- **Patterns:** Matrix

## Problem
Given an `m x n` matrix, if any element is `0`, set its entire row and column to `0`.
Do it **in place**. (The follow-up asks for `O(1)` extra space.)

## Examples
**Example 1**
- Input: `matrix = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `[[1,0,1],[0,0,0],[1,0,1]]`

**Example 2**
- Input: `matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]`
- Output: `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`

## Constraints
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`
