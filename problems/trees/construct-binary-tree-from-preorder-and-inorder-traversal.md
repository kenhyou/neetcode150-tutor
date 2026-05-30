# Construct Binary Tree from Preorder and Inorder Traversal

- **Category:** Trees · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
- **Patterns:** DFS, Divide & Conquer

## Problem
Given two integer arrays `preorder` and `inorder` representing the preorder and inorder
traversals of a binary tree (all values unique), reconstruct and return the tree.

## Examples
**Example 1**
- Input: `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`
- Output: `[3,9,20,null,null,15,7]`

**Example 2**
- Input: `preorder = [-1]`, `inorder = [-1]`
- Output: `[-1]`

## Constraints
- `1 <= preorder.length <= 3000`, same length as `inorder`.
- Values are unique; `inorder` is a permutation of `preorder`.
