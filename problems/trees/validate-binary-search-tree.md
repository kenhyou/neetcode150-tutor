# Validate Binary Search Tree

- **Category:** Trees · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/validate-binary-search-tree/
- **Patterns:** BST, DFS

## Problem
Given the root of a binary tree, determine whether it is a valid binary search tree: at
every node, all values in the left subtree are strictly smaller and all values in the
right subtree are strictly larger, and both subtrees are themselves valid BSTs.

## Examples
**Example 1**
- Input: `root = [2,1,3]`
- Output: `true`

**Example 2**
- Input: `root = [5,1,4,null,null,3,6]`
- Output: `false`
- Explanation: `4` is in the right subtree of `5` but is smaller than `5`.

## Constraints
- The tree has `1` to `10^4` nodes.
- `-2^31 <= Node.val <= 2^31 - 1`
