# Min Cost to Connect All Points

- **Category:** Advanced Graphs · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/min-cost-to-connect-all-points/
- **Patterns:** MST, Prim

## Problem
Given `points` on a 2D plane, the cost to connect two points is their Manhattan
distance `|x1-x2| + |y1-y2|`. Return the minimum total cost to connect all points so
that there is exactly one path between any two (a minimum spanning tree).

## Examples
**Example 1**
- Input: `points = [[0,0],[2,2],[3,10],[5,2],[7,0]]`
- Output: `20`

**Example 2**
- Input: `points = [[3,12],[-2,5],[-4,1]]`
- Output: `18`

## Constraints
- `1 <= points.length <= 1000`
- `-10^6 <= xi, yi <= 10^6`, all points distinct.
