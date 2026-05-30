# Find Median from Data Stream

- **Category:** Heap / Priority Queue · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/find-median-from-data-stream/
- **Patterns:** Two Heaps, Design

## Problem
Design a structure that supports adding numbers from a stream and returning the median
of all numbers seen so far. Implement:

- `addNum(num)` — add an integer to the data structure.
- `findMedian()` — return the median of all elements added.

## Examples
**Example 1**
- `addNum(1)`; `addNum(2)`; `findMedian()` -> `1.5`; `addNum(3)`; `findMedian()` -> `2.0`.

## Constraints
- `-10^5 <= num <= 10^5`
- `findMedian` is only called after at least one `addNum`.
- At most `5 * 10^4` calls total.
