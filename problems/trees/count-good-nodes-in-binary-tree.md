# Count Good Nodes in Binary Tree

- **Category:** Trees · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/count-good-nodes-in-binary-tree/
- **Patterns:** DFS

## Problem
A node `X` in a binary tree is **good** if no node on the path from the root to `X` has
a value greater than `X`. Given the root, return the number of good nodes.

## Examples
**Example 1**
- Input: `root = [3,1,4,3,null,1,5]`
- Output: `4`

**Example 2**
- Input: `root = [3,3,null,4,2]`
- Output: `3`

## Constraints
- The tree has `1` to `10^5` nodes.
- `-10^4 <= Node.val <= 10^4`
