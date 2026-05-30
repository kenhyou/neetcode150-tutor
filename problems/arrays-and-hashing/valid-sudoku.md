# Valid Sudoku

- **Category:** Arrays & Hashing · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/valid-sudoku/
- **Patterns:** Hash Set, Matrix

## Problem
Given a `9 x 9` Sudoku board, determine whether the **currently filled** cells make it
a valid configuration. Validity requires that each row, each column, and each of the
nine `3 x 3` sub-boxes contains the digits `1`–`9` without repetition. Empty cells are
marked `'.'` and are ignored. The board does **not** need to be solvable — only the
filled cells must not conflict.

## Examples
**Example 1**
- Input: a board whose filled cells follow Sudoku rules.
- Output: `true`

**Example 2**
- Input: the same board but with two `8`s in the same column (or row, or box).
- Output: `false`

## Constraints
- `board.length == 9` and `board[i].length == 9`.
- Each cell is a digit `'1'`–`'9'` or `'.'`.
