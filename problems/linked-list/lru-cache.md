# LRU Cache

- **Category:** Linked List · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/lru-cache/
- **Patterns:** Hash Map, Linked List, Design

## Problem
Design a Least Recently Used (LRU) cache with fixed `capacity`. Implement:

- `get(key)` — return the value if present (and mark it most recently used), else `-1`.
- `put(key, value)` — insert/update; if over capacity, evict the least recently used
  key.

Both operations must run in average `O(1)` time.

## Examples
**Example 1**
- `LRUCache(2)`; `put(1,1)`; `put(2,2)`; `get(1)` -> `1`; `put(3,3)` (evicts 2);
  `get(2)` -> `-1`; `put(4,4)` (evicts 1); `get(1)` -> `-1`; `get(3)` -> `3`;
  `get(4)` -> `4`.

## Constraints
- `1 <= capacity <= 3000`
- `0 <= key, value <= 10^4`
- At most `2 * 10^5` calls to `get` and `put`.
