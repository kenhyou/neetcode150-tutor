# Copy List with Random Pointer

- **Category:** Linked List · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/copy-list-with-random-pointer/
- **Patterns:** Hash Map, Linked List

## Problem
Each node of a linked list has a `next` pointer and a `random` pointer that may point
to any node in the list or be `null`. Return a **deep copy** of the list: new nodes
whose `next`/`random` mirror the originals' structure but reference only the copied
nodes.

## Examples
**Example 1**
- Input: `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]` (each pair = `[val, randomIndex]`)
- Output: an identical-structure deep copy.

**Example 2**
- Input: `head = [[1,1],[2,1]]`
- Output: `[[1,1],[2,1]]`

## Constraints
- `0 <= n <= 1000`
- `-10^4 <= Node.val <= 10^4`
- `random` is `null` or points to a node in the list.
