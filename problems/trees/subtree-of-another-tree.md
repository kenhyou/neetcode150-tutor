# Subtree of Another Tree

- **Category:** Trees · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/subtree-of-another-tree/
- **Patterns:** DFS

## Problem
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a
node in `root` whose subtree is structurally identical (same shape and values) to
`subRoot`.

## Examples
**Example 1**
- Input: `root = [3,4,5,1,2]`, `subRoot = [4,1,2]`
- Output: `true`

**Example 2**
- Input: `root = [3,4,5,1,2,null,null,null,null,0]`, `subRoot = [4,1,2]`
- Output: `false`

## Constraints
- `root` has `1` to `2000` nodes; `subRoot` has `1` to `1000` nodes.
- `-10^4 <= Node.val <= 10^4`
