# Lowest Common Ancestor of a Binary Search Tree

- **Category:** Trees · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
- **Patterns:** BST

## Problem
Given a binary **search** tree and two nodes `p` and `q` present in it, return their
lowest common ancestor — the deepest node that has both `p` and `q` as descendants (a
node can be a descendant of itself).

## Examples
**Example 1**
- Input: `root = [6,2,8,0,4,7,9,null,null,3,5]`, `p = 2`, `q = 8`
- Output: `6`

**Example 2**
- Input: same tree, `p = 2`, `q = 4`
- Output: `2`

## Constraints
- The tree has `2` to `10^5` nodes, all values unique.
- `p` and `q` exist in the BST and `p != q`.
