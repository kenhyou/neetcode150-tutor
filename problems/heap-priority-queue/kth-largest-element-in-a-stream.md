# Kth Largest Element in a Stream

- **Category:** Heap / Priority Queue · **Difficulty:** Easy
- **LeetCode:** https://leetcode.com/problems/kth-largest-element-in-a-stream/
- **Patterns:** Heap, Design

## Problem
Design a class that tracks the `k`-th largest value in a stream of numbers (not
necessarily distinct). Implement:

- `KthLargest(k, nums)` — initialize with `k` and an initial list.
- `add(val)` — append `val` to the stream and return the current `k`-th largest.

## Examples
**Example 1**
- `KthLargest(3, [4,5,8,2])`; `add(3)` -> `4`; `add(5)` -> `5`; `add(10)` -> `5`;
  `add(9)` -> `8`; `add(4)` -> `8`.

## Constraints
- `1 <= k <= 10^4`
- `-10^4 <= nums[i], val <= 10^4`
- At least `k` elements exist when `add` is called.
