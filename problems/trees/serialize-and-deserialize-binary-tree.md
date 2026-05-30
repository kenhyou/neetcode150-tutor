# Serialize and Deserialize Binary Tree

- **Category:** Trees · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
- **Patterns:** BFS, DFS, Design

## Problem
Design an algorithm to serialize a binary tree into a string and deserialize that
string back into the identical tree. The encoding format is up to you, as long as the
round trip reproduces the original tree.

## Examples
**Example 1**
- Input: `root = [1,2,3,null,null,4,5]`
- Output (after serialize then deserialize): `[1,2,3,null,null,4,5]`

**Example 2**
- Input: `root = []`
- Output: `[]`

## Constraints
- The tree has `0` to `10^4` nodes.
- `-1000 <= Node.val <= 1000`
