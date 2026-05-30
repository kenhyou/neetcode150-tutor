# Search a 2D Matrix

- **Category:** Binary Search · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/search-a-2d-matrix/
- **Patterns:** Binary Search, Matrix

## Problem
You are given an `m x n` matrix where each row is sorted left-to-right and the first
integer of each row is greater than the last integer of the previous row. Return
`true` if `target` is in the matrix. Aim for `O(log(m * n))` time.

## Examples
**Example 1**
- Input: `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]`, `target = 3`
- Output: `true`

**Example 2**
- Input: same matrix, `target = 13`
- Output: `false`

## Constraints
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`
