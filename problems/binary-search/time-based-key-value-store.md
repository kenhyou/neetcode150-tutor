# Time Based Key-Value Store

- **Category:** Binary Search · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/time-based-key-value-store/
- **Patterns:** Binary Search, Design

## Problem
Design a key-value store that records multiple values for a key at different
timestamps and can retrieve the right value for a given time. Implement:

- `set(key, value, timestamp)` — store `value` for `key` at time `timestamp`.
- `get(key, timestamp)` — return the value with the largest stored time
  `<= timestamp`. If none exists, return `""`. Calls to `set` for a key arrive with
  strictly increasing timestamps.

## Examples
**Example 1**
- `set("foo", "bar", 1)`; `get("foo", 1)` -> `"bar"`; `get("foo", 3)` -> `"bar"`;
  `set("foo", "bar2", 4)`; `get("foo", 4)` -> `"bar2"`; `get("foo", 5)` -> `"bar2"`.

## Constraints
- `1 <= key.length, value.length <= 100`
- `1 <= timestamp <= 10^7`
- At most `2 * 10^5` calls total across `set` and `get`.
