# Detect Squares

- **Category:** Math & Geometry · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/detect-squares/
- **Patterns:** Hash Map, Design

## Problem
Design a data structure that processes a stream of points and can count axis-aligned
squares. Implement:

- `add(point)` — add a point (duplicates allowed).
- `count(point)` — given a query point, return how many axis-aligned squares can be
  formed using the query point and three points already added, where the square has
  positive area and sides parallel to the axes.

## Examples
**Example 1**
- `add([3,10])`; `add([11,2])`; `add([3,2])`; `count([11,10])` -> `1`;
  `count([14,8])` -> `0`; `add([11,2])`; `count([11,10])` -> `2`.

## Constraints
- `0 <= x, y <= 1000`
- At most `3000` calls total to `add` and `count`.
