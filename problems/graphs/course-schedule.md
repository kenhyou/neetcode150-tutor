# Course Schedule

- **Category:** Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/course-schedule/
- **Patterns:** Topological Sort, DFS

## Problem
There are `numCourses` courses labeled `0` to `numCourses - 1`. `prerequisites[i] =
[a, b]` means you must take course `b` before course `a`. Return `true` if you can
finish all courses (i.e. the prerequisite graph has no cycle).

## Examples
**Example 1**
- Input: `numCourses = 2`, `prerequisites = [[1, 0]]`
- Output: `true`

**Example 2**
- Input: `numCourses = 2`, `prerequisites = [[1, 0], [0, 1]]`
- Output: `false`

## Constraints
- `1 <= numCourses <= 2000`
- `0 <= prerequisites.length <= 5000`, pairs are unique.
