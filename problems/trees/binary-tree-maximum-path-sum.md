# Binary Tree Maximum Path Sum

- **Category:** Trees · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/binary-tree-maximum-path-sum/
- **Patterns:** DFS

## Problem
A path in a binary tree is a sequence of nodes connected by edges, where each node is
used at most once; the path need not pass through the root. Given the root, return the
maximum possible sum of node values along any such path.

## Examples
**Example 1**
- Input: `root = [1,2,3]`
- Output: `6`

**Example 2**
- Input: `root = [-10,9,20,null,null,15,7]`
- Output: `42`
- Explanation: `15 -> 20 -> 7`.

## Constraints
- The tree has `1` to `3 * 10^4` nodes.
- `-1000 <= Node.val <= 1000`
