# Reconstruct Itinerary

- **Category:** Advanced Graphs · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/reconstruct-itinerary/
- **Patterns:** Eulerian Path, DFS

## Problem
Given a list of airline `tickets` `[from, to]`, reconstruct the itinerary that uses
every ticket exactly once, starting from `"JFK"`. If multiple valid itineraries exist,
return the one that is smallest in lexical (alphabetical) order when read as a single
list. A valid itinerary is guaranteed.

## Examples
**Example 1**
- Input: `tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]`
- Output: `["JFK","MUC","LHR","SFO","SJC"]`

**Example 2**
- Input: `tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]`
- Output: `["JFK","ATL","JFK","SFO","ATL","SFO"]`

## Constraints
- `1 <= tickets.length <= 300`
- Airport codes are 3 uppercase letters; all tickets form at least one valid itinerary.
