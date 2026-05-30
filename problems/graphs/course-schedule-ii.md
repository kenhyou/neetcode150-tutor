# Course Schedule II

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/course-schedule-ii/
- **Patterns:** Topological Sort

## Problem
Same setup as Course Schedule: `numCourses` courses and prerequisite pairs `[a, b]`
meaning `b` before `a`. Return any valid ordering in which all courses can be taken.
If it is impossible (a cycle exists), return an empty array.

## Examples
**Example 1**
- Input: `numCourses = 2`, `prerequisites = [[1, 0]]`
- Output: `[0, 1]`

**Example 2**
- Input: `numCourses = 4`, `prerequisites = [[1,0],[2,0],[3,1],[3,2]]`
- Output: `[0, 1, 2, 3]` (or `[0, 2, 1, 3]`)

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= numCourses * (numCourses - 1)`, pairs distinct.
