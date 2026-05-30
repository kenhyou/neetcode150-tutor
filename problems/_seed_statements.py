#!/usr/bin/env python3
"""Seed paraphrased problem statements for every NeetCode 150 problem.

Header metadata (title, category, difficulty, LeetCode link, patterns) is pulled from
data/neetcode150.json so paths and labels stay consistent. The body for each problem
is authored below in our own words (paraphrased, not copied from LeetCode).

By default this SKIPS files that already exist, so hand-edited statements are kept.
Pass --force to overwrite everything.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INDEX = os.path.join(ROOT, "data", "neetcode150.json")

# id -> body markdown (starts at "## Problem"). Paraphrased descriptions.
STATEMENTS = {
    # ---------------- Two Pointers ----------------
    "valid-palindrome": r"""## Problem
Given a string `s`, return `true` if it reads the same forwards and backwards once you
consider only alphanumeric characters and ignore case. All other characters
(spaces, punctuation) are skipped. An empty string counts as a palindrome.

## Examples
**Example 1**
- Input: `s = "A man, a plan, a canal: Panama"`
- Output: `true`
- Explanation: After filtering, it reads `amanaplanacanalpanama`.

**Example 2**
- Input: `s = "race a car"`
- Output: `false`

## Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists of printable ASCII characters.
""",
    "two-sum-ii-input-array-is-sorted": r"""## Problem
Given a **1-indexed** array `numbers` sorted in non-decreasing order, find the two
elements that add up to a given `target`. Return their 1-based indices `[i, j]` with
`i < j`. Exactly one solution exists, and you must use only `O(1)` extra space (no
hash map).

## Examples
**Example 1**
- Input: `numbers = [2, 7, 11, 15]`, `target = 9`
- Output: `[1, 2]`

**Example 2**
- Input: `numbers = [2, 3, 4]`, `target = 6`
- Output: `[1, 3]`

## Constraints
- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`, sorted non-decreasing.
- Exactly one valid answer exists.
""",
    "3sum": r"""## Problem
Given an integer array `nums`, return all **unique** triplets `[a, b, c]` such that
`a + b + c == 0`. The solution set must not contain duplicate triplets, but the order
of triplets (and of values within them) does not matter.

## Examples
**Example 1**
- Input: `nums = [-1, 0, 1, 2, -1, -4]`
- Output: `[[-1, -1, 2], [-1, 0, 1]]`

**Example 2**
- Input: `nums = [0, 1, 1]`
- Output: `[]`

**Example 3**
- Input: `nums = [0, 0, 0]`
- Output: `[[0, 0, 0]]`

## Constraints
- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`
""",
    "container-with-most-water": r"""## Problem
You are given an array `height` where `height[i]` is the height of a vertical line at
position `i`. Pick two lines that, together with the x-axis, form a container. Return
the maximum amount of water it can hold — i.e. maximize `min(height[i], height[j]) *
(j - i)`.

## Examples
**Example 1**
- Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- Output: `49`
- Explanation: Lines at index 1 and 8 give `min(8, 7) * (8 - 1) = 49`.

**Example 2**
- Input: `height = [1, 1]`
- Output: `1`

## Constraints
- `2 <= height.length <= 10^5`
- `0 <= height[i] <= 10^4`
""",
    "trapping-rain-water": r"""## Problem
Given `n` non-negative integers `height` representing an elevation map where each bar
has width 1, compute how much rainwater can be trapped between the bars after it
rains.

## Examples
**Example 1**
- Input: `height = [0,1,0,2,1,0,1,3,2,1,2,1]`
- Output: `6`

**Example 2**
- Input: `height = [4, 2, 0, 3, 2, 5]`
- Output: `9`

## Constraints
- `1 <= height.length <= 2 * 10^4`
- `0 <= height[i] <= 10^5`
""",

    # ---------------- Sliding Window ----------------
    "best-time-to-buy-and-sell-stock": r"""## Problem
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.
You may buy on one day and sell on a later day. Return the maximum profit you can
make from a single buy/sell. If no profit is possible, return `0`.

## Examples
**Example 1**
- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `5`
- Explanation: Buy at 1 (day 2), sell at 6 (day 5).

**Example 2**
- Input: `prices = [7, 6, 4, 3, 1]`
- Output: `0`

## Constraints
- `1 <= prices.length <= 10^5`
- `0 <= prices[i] <= 10^4`
""",
    "longest-substring-without-repeating-characters": r"""## Problem
Given a string `s`, return the length of the longest substring that contains no
repeating characters.

## Examples
**Example 1**
- Input: `s = "abcabcbb"`
- Output: `3`
- Explanation: The answer is `"abc"`.

**Example 2**
- Input: `s = "bbbbb"`
- Output: `1`

**Example 3**
- Input: `s = "pwwkew"`
- Output: `3` (`"wke"`)

## Constraints
- `0 <= s.length <= 5 * 10^4`
- `s` consists of English letters, digits, symbols, and spaces.
""",
    "longest-repeating-character-replacement": r"""## Problem
Given a string `s` of uppercase English letters and an integer `k`, you may change at
most `k` characters to any other uppercase letter. Return the length of the longest
substring containing a single repeated letter that you can produce after these
changes.

## Examples
**Example 1**
- Input: `s = "ABAB"`, `k = 2`
- Output: `4`

**Example 2**
- Input: `s = "AABABBA"`, `k = 1`
- Output: `4`
- Explanation: Change one `B` so `"AABA"` -> `"AAAA"` style window of length 4.

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists of uppercase English letters.
- `0 <= k <= s.length`
""",
    "permutation-in-string": r"""## Problem
Given two strings `s1` and `s2`, return `true` if `s2` contains a substring that is a
permutation of `s1` (i.e. one of `s1`'s anagrams appears as a contiguous block in
`s2`). Otherwise return `false`.

## Examples
**Example 1**
- Input: `s1 = "ab"`, `s2 = "eidbaooo"`
- Output: `true`
- Explanation: `s2` contains `"ba"`, a permutation of `"ab"`.

**Example 2**
- Input: `s1 = "ab"`, `s2 = "eidboaoo"`
- Output: `false`

## Constraints
- `1 <= s1.length, s2.length <= 10^4`
- `s1` and `s2` consist of lowercase English letters.
""",
    "minimum-window-substring": r"""## Problem
Given strings `s` and `t`, return the shortest substring of `s` that contains every
character of `t` (including multiplicities). If no such window exists, return the
empty string `""`. The answer is guaranteed unique.

## Examples
**Example 1**
- Input: `s = "ADOBECODEBANC"`, `t = "ABC"`
- Output: `"BANC"`

**Example 2**
- Input: `s = "a"`, `t = "a"`
- Output: `"a"`

**Example 3**
- Input: `s = "a"`, `t = "aa"`
- Output: `""`

## Constraints
- `1 <= s.length, t.length <= 10^5`
- `s` and `t` consist of uppercase and lowercase English letters.
""",
    "sliding-window-maximum": r"""## Problem
Given an integer array `nums` and a window size `k`, the window slides from the left
end to the right end, one position at a time. Return an array of the maximum value
within each window position.

## Examples
**Example 1**
- Input: `nums = [1,3,-1,-3,5,3,6,7]`, `k = 3`
- Output: `[3, 3, 5, 5, 6, 7]`

**Example 2**
- Input: `nums = [1]`, `k = 1`
- Output: `[1]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= nums.length`
""",

    # ---------------- Stack ----------------
    "valid-parentheses": r"""## Problem
Given a string `s` of just the characters `()[]{}`, decide whether it is valid: every
opening bracket must be closed by the matching type, in the correct order, and every
closing bracket must have a corresponding opener.

## Examples
**Example 1**
- Input: `s = "()[]{}"`
- Output: `true`

**Example 2**
- Input: `s = "(]"`
- Output: `false`

**Example 3**
- Input: `s = "([])"`
- Output: `true`

## Constraints
- `1 <= s.length <= 10^4`
- `s` consists only of `()[]{}`.
""",
    "min-stack": r"""## Problem
Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element,
all in `O(1)` time. Implement the class:

- `push(val)` — push `val` onto the stack.
- `pop()` — remove the top element.
- `top()` — return the top element.
- `getMin()` — return the smallest element currently in the stack.

## Examples
**Example 1**
- Operations: `push(-2)`, `push(0)`, `push(-3)`, `getMin()`, `pop()`, `top()`, `getMin()`
- Output: `-3`, then `0`, then `-2`

## Constraints
- `-2^31 <= val <= 2^31 - 1`
- `pop`, `top`, `getMin` are always called on a non-empty stack.
- At most `3 * 10^4` calls total.
""",
    "evaluate-reverse-polish-notation": r"""## Problem
Evaluate the value of an arithmetic expression given in Reverse Polish Notation
(postfix). Valid operators are `+`, `-`, `*`, `/`; each operand is an integer.
Division truncates toward zero. The input is always a valid expression.

## Examples
**Example 1**
- Input: `tokens = ["2", "1", "+", "3", "*"]`
- Output: `9`
- Explanation: `((2 + 1) * 3)`.

**Example 2**
- Input: `tokens = ["4", "13", "5", "/", "+"]`
- Output: `6`
- Explanation: `(4 + (13 / 5))`.

## Constraints
- `1 <= tokens.length <= 10^4`
- Each token is an operator or an integer in `[-200, 200]`.
""",
    "generate-parentheses": r"""## Problem
Given `n` pairs of parentheses, generate all distinct strings of well-formed
(balanced) parentheses using exactly `n` opening and `n` closing brackets.

## Examples
**Example 1**
- Input: `n = 3`
- Output: `["((()))","(()())","(())()","()(())","()()()"]`

**Example 2**
- Input: `n = 1`
- Output: `["()"]`

## Constraints
- `1 <= n <= 8`
""",
    "daily-temperatures": r"""## Problem
Given an array `temperatures`, return an array `answer` such that `answer[i]` is the
number of days you must wait after day `i` to get a warmer temperature. If no warmer
day exists, set `answer[i] = 0`.

## Examples
**Example 1**
- Input: `temperatures = [73,74,75,71,69,72,76,73]`
- Output: `[1,1,4,2,1,1,0,0]`

**Example 2**
- Input: `temperatures = [30, 40, 50, 60]`
- Output: `[1, 1, 1, 0]`

## Constraints
- `1 <= temperatures.length <= 10^5`
- `30 <= temperatures[i] <= 100`
""",
    "car-fleet": r"""## Problem
There are `n` cars heading to the same destination `target` miles away. Car `i` starts
at `position[i]` with constant `speed[i]`. A faster car cannot pass a slower one — it
catches up and they move together as one "fleet" (a fleet may be a single car).
Return how many fleets arrive at the destination.

## Examples
**Example 1**
- Input: `target = 12`, `position = [10, 8, 0, 5, 3]`, `speed = [2, 4, 1, 1, 3]`
- Output: `3`

**Example 2**
- Input: `target = 10`, `position = [3]`, `speed = [3]`
- Output: `1`

## Constraints
- `n == position.length == speed.length`
- `1 <= n <= 10^5`
- `0 < target <= 10^6`, positions are distinct.
""",
    "largest-rectangle-in-histogram": r"""## Problem
Given an array `heights` representing the bar heights of a histogram (each bar width
1), return the area of the largest rectangle that fits entirely within the histogram.

## Examples
**Example 1**
- Input: `heights = [2, 1, 5, 6, 2, 3]`
- Output: `10`
- Explanation: The bars of height 5 and 6 form a `5 x 2 = 10` rectangle.

**Example 2**
- Input: `heights = [2, 4]`
- Output: `4`

## Constraints
- `1 <= heights.length <= 10^5`
- `0 <= heights[i] <= 10^4`
""",

    # ---------------- Binary Search ----------------
    "binary-search": r"""## Problem
Given a sorted (ascending) array `nums` of distinct integers and a `target`, return
the index of `target` if present, otherwise `-1`. Your algorithm must run in
`O(log n)` time.

## Examples
**Example 1**
- Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 9`
- Output: `4`

**Example 2**
- Input: `nums = [-1, 0, 3, 5, 9, 12]`, `target = 2`
- Output: `-1`

## Constraints
- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All values in `nums` are unique and sorted ascending.
""",
    "search-a-2d-matrix": r"""## Problem
You are given an `m x n` matrix where each row is sorted left-to-right and the first
integer of each row is greater than the last integer of the previous row. Return
`true` if `target` is in the matrix. Aim for `O(log(m * n))` time.

## Examples
**Example 1**
- Input: `matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]`, `target = 3`
- Output: `true`

**Example 2**
- Input: same matrix, `target = 13`
- Output: `false`

## Constraints
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`
""",
    "koko-eating-bananas": r"""## Problem
Koko has `piles` of bananas and `h` hours before the guards return. Each hour she
picks one pile and eats up to `k` bananas from it (if the pile has fewer, she eats it
all and stops for that hour). Return the smallest integer eating speed `k` such that
she finishes all bananas within `h` hours.

## Examples
**Example 1**
- Input: `piles = [3, 6, 7, 11]`, `h = 8`
- Output: `4`

**Example 2**
- Input: `piles = [30, 11, 23, 4, 20]`, `h = 5`
- Output: `30`

## Constraints
- `1 <= piles.length <= 10^4`
- `piles.length <= h <= 10^9`
- `1 <= piles[i] <= 10^9`
""",
    "find-minimum-in-rotated-sorted-array": r"""## Problem
A sorted ascending array of unique integers has been rotated between 1 and n times.
Given the resulting array `nums`, return its minimum element in `O(log n)` time.

## Examples
**Example 1**
- Input: `nums = [3, 4, 5, 1, 2]`
- Output: `1`

**Example 2**
- Input: `nums = [4, 5, 6, 7, 0, 1, 2]`
- Output: `0`

**Example 3**
- Input: `nums = [11, 13, 15, 17]`
- Output: `11`

## Constraints
- `1 <= nums.length <= 5000`
- `-5000 <= nums[i] <= 5000`, all unique.
""",
    "search-in-rotated-sorted-array": r"""## Problem
A sorted ascending array of unique integers may have been rotated at some pivot.
Given the rotated array `nums` and a `target`, return the index of `target`, or `-1`
if absent. Run in `O(log n)` time.

## Examples
**Example 1**
- Input: `nums = [4,5,6,7,0,1,2]`, `target = 0`
- Output: `4`

**Example 2**
- Input: `nums = [4,5,6,7,0,1,2]`, `target = 3`
- Output: `-1`

## Constraints
- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i], target <= 10^4`, all values unique.
""",
    "time-based-key-value-store": r"""## Problem
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
""",
    "median-of-two-sorted-arrays": r"""## Problem
Given two sorted arrays `nums1` and `nums2` of sizes `m` and `n`, return the median of
the combined sorted array. The overall run time should be `O(log(m + n))`.

## Examples
**Example 1**
- Input: `nums1 = [1, 3]`, `nums2 = [2]`
- Output: `2.0`

**Example 2**
- Input: `nums1 = [1, 2]`, `nums2 = [3, 4]`
- Output: `2.5`

## Constraints
- `0 <= m, n <= 1000`, `1 <= m + n <= 2000`
- `-10^6 <= nums1[i], nums2[i] <= 10^6`
""",

    # ---------------- Linked List ----------------
    "reverse-linked-list": r"""## Problem
Given the head of a singly linked list, reverse the list and return the new head.

## Examples
**Example 1**
- Input: `head = [1, 2, 3, 4, 5]`
- Output: `[5, 4, 3, 2, 1]`

**Example 2**
- Input: `head = []`
- Output: `[]`

## Constraints
- The list has `0` to `5000` nodes.
- `-5000 <= Node.val <= 5000`

**Follow-up:** Can you do it both iteratively and recursively?
""",
    "merge-two-sorted-lists": r"""## Problem
Given the heads of two sorted singly linked lists, splice them together into one
sorted list by reusing the existing nodes, and return the head of the merged list.

## Examples
**Example 1**
- Input: `list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`
- Output: `[1, 1, 2, 3, 4, 4]`

**Example 2**
- Input: `list1 = []`, `list2 = [0]`
- Output: `[0]`

## Constraints
- Each list has `0` to `50` nodes.
- `-100 <= Node.val <= 100`, both sorted non-decreasing.
""",
    "reorder-list": r"""## Problem
Given the head of a singly linked list `L0 -> L1 -> ... -> Ln-1 -> Ln`, reorder it
**in place** to `L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...`. You may not change node
values, only relink nodes.

## Examples
**Example 1**
- Input: `head = [1, 2, 3, 4]`
- Output: `[1, 4, 2, 3]`

**Example 2**
- Input: `head = [1, 2, 3, 4, 5]`
- Output: `[1, 5, 2, 4, 3]`

## Constraints
- The list has `1` to `5 * 10^4` nodes.
- `1 <= Node.val <= 1000`
""",
    "remove-nth-node-from-end-of-list": r"""## Problem
Given the head of a linked list, remove the `n`-th node counting from the end and
return the head. Try to do it in a single pass.

## Examples
**Example 1**
- Input: `head = [1, 2, 3, 4, 5]`, `n = 2`
- Output: `[1, 2, 3, 5]`

**Example 2**
- Input: `head = [1]`, `n = 1`
- Output: `[]`

## Constraints
- The list has `1` to `30` nodes.
- `0 <= Node.val <= 100`
- `1 <= n <= list length`
""",
    "copy-list-with-random-pointer": r"""## Problem
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
""",
    "add-two-numbers": r"""## Problem
You are given two non-empty linked lists representing non-negative integers, with the
digits stored in **reverse** order (ones digit first). Add the two numbers and return
the sum as a linked list in the same reverse-order format.

## Examples
**Example 1**
- Input: `l1 = [2, 4, 3]`, `l2 = [5, 6, 4]`  (342 + 465)
- Output: `[7, 0, 8]`  (807)

**Example 2**
- Input: `l1 = [9,9,9,9,9,9,9]`, `l2 = [9,9,9,9]`
- Output: `[8,9,9,9,0,0,0,1]`

## Constraints
- Each list has `1` to `100` nodes; digits `0`–`9`.
- No leading zeros except the number 0 itself.
""",
    "linked-list-cycle": r"""## Problem
Given the head of a linked list, return `true` if the list contains a cycle (some node
can be reached again by following `next` pointers), otherwise `false`. Aim for `O(1)`
extra space.

## Examples
**Example 1**
- Input: `head = [3, 2, 0, -4]` with the tail connecting back to index 1.
- Output: `true`

**Example 2**
- Input: `head = [1]`, no cycle.
- Output: `false`

## Constraints
- The list has `0` to `10^4` nodes.
- `-10^5 <= Node.val <= 10^5`
""",
    "find-the-duplicate-number": r"""## Problem
Given an array `nums` of `n + 1` integers where each value is in the range
`[1, n]`, there is exactly one value that is repeated (possibly multiple times).
Return that duplicate **without modifying the array** and using only `O(1)` extra
space.

## Examples
**Example 1**
- Input: `nums = [1, 3, 4, 2, 2]`
- Output: `2`

**Example 2**
- Input: `nums = [3, 1, 3, 4, 2]`
- Output: `3`

## Constraints
- `1 <= n <= 10^5`, `nums.length == n + 1`
- `1 <= nums[i] <= n`, exactly one value repeats.
""",
    "lru-cache": r"""## Problem
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
""",
    "merge-k-sorted-lists": r"""## Problem
You are given an array of `k` linked lists, each sorted ascending. Merge them all into
a single sorted linked list and return its head.

## Examples
**Example 1**
- Input: `lists = [[1,4,5],[1,3,4],[2,6]]`
- Output: `[1,1,2,3,4,4,5,6]`

**Example 2**
- Input: `lists = []`
- Output: `[]`

## Constraints
- `0 <= k <= 10^4`
- Each list is sorted; total nodes `<= 10^4`.
- `-10^4 <= Node.val <= 10^4`
""",
    "reverse-nodes-in-k-group": r"""## Problem
Given the head of a linked list, reverse the nodes `k` at a time and return the
modified list. If the number of remaining nodes is fewer than `k`, leave them as-is.
You may not change node values, only relink nodes.

## Examples
**Example 1**
- Input: `head = [1,2,3,4,5]`, `k = 2`
- Output: `[2,1,4,3,5]`

**Example 2**
- Input: `head = [1,2,3,4,5]`, `k = 3`
- Output: `[3,2,1,4,5]`

## Constraints
- The list has `1` to `5000` nodes.
- `0 <= Node.val <= 1000`, `1 <= k <= n`.

**Follow-up:** Can you do it using only `O(1)` extra memory?
""",

    # ---------------- Trees ----------------
    "invert-binary-tree": r"""## Problem
Given the root of a binary tree, invert it (mirror every left/right pair of children)
and return the root.

## Examples
**Example 1**
- Input: `root = [4,2,7,1,3,6,9]`
- Output: `[4,7,2,9,6,3,1]`

**Example 2**
- Input: `root = [2,1,3]`
- Output: `[2,3,1]`

## Constraints
- The tree has `0` to `100` nodes.
- `-100 <= Node.val <= 100`
""",
    "maximum-depth-of-binary-tree": r"""## Problem
Given the root of a binary tree, return its maximum depth — the number of nodes along
the longest path from the root down to a leaf.

## Examples
**Example 1**
- Input: `root = [3,9,20,null,null,15,7]`
- Output: `3`

**Example 2**
- Input: `root = [1,null,2]`
- Output: `2`

## Constraints
- The tree has `0` to `10^4` nodes.
- `-100 <= Node.val <= 100`
""",
    "diameter-of-binary-tree": r"""## Problem
Given the root of a binary tree, return its diameter: the length (in edges) of the
longest path between any two nodes. This path may or may not pass through the root.

## Examples
**Example 1**
- Input: `root = [1,2,3,4,5]`
- Output: `3`
- Explanation: The path `4 -> 2 -> 1 -> 3` (or `5 -> 2 -> 1 -> 3`) has 3 edges.

**Example 2**
- Input: `root = [1,2]`
- Output: `1`

## Constraints
- The tree has `1` to `10^4` nodes.
- `-100 <= Node.val <= 100`
""",
    "balanced-binary-tree": r"""## Problem
Given the root of a binary tree, return `true` if it is height-balanced — for every
node, the heights of its two subtrees differ by at most 1.

## Examples
**Example 1**
- Input: `root = [3,9,20,null,null,15,7]`
- Output: `true`

**Example 2**
- Input: `root = [1,2,2,3,3,null,null,4,4]`
- Output: `false`

## Constraints
- The tree has `0` to `5000` nodes.
- `-10^4 <= Node.val <= 10^4`
""",
    "same-tree": r"""## Problem
Given the roots of two binary trees `p` and `q`, return `true` if they are identical in
both structure and node values.

## Examples
**Example 1**
- Input: `p = [1,2,3]`, `q = [1,2,3]`
- Output: `true`

**Example 2**
- Input: `p = [1,2]`, `q = [1,null,2]`
- Output: `false`

## Constraints
- Each tree has `0` to `100` nodes.
- `-10^4 <= Node.val <= 10^4`
""",
    "subtree-of-another-tree": r"""## Problem
Given the roots of two binary trees `root` and `subRoot`, return `true` if there is a
node in `root` whose subtree is structurally identical (same shape and values) to
`subRoot`.

## Examples
**Example 1**
- Input: `root = [3,4,5,1,2]`, `subRoot = [4,1,2]`
- Output: `true`

**Example 2**
- Input: `root = [3,4,5,1,2,null,null,null,null,0]`, `subRoot = [4,1,2]`
- Output: `false`

## Constraints
- `root` has `1` to `2000` nodes; `subRoot` has `1` to `1000` nodes.
- `-10^4 <= Node.val <= 10^4`
""",
    "lowest-common-ancestor-of-a-binary-search-tree": r"""## Problem
Given a binary **search** tree and two nodes `p` and `q` present in it, return their
lowest common ancestor — the deepest node that has both `p` and `q` as descendants (a
node can be a descendant of itself).

## Examples
**Example 1**
- Input: `root = [6,2,8,0,4,7,9,null,null,3,5]`, `p = 2`, `q = 8`
- Output: `6`

**Example 2**
- Input: same tree, `p = 2`, `q = 4`
- Output: `2`

## Constraints
- The tree has `2` to `10^5` nodes, all values unique.
- `p` and `q` exist in the BST and `p != q`.
""",
    "binary-tree-level-order-traversal": r"""## Problem
Given the root of a binary tree, return its level-order traversal: a list of levels,
each level being the node values from left to right.

## Examples
**Example 1**
- Input: `root = [3,9,20,null,null,15,7]`
- Output: `[[3],[9,20],[15,7]]`

**Example 2**
- Input: `root = [1]`
- Output: `[[1]]`

## Constraints
- The tree has `0` to `2000` nodes.
- `-1000 <= Node.val <= 1000`
""",
    "binary-tree-right-side-view": r"""## Problem
Given the root of a binary tree, imagine standing on its right side. Return the values
of the nodes you can see, ordered top to bottom (the last node of each level).

## Examples
**Example 1**
- Input: `root = [1,2,3,null,5,null,4]`
- Output: `[1, 3, 4]`

**Example 2**
- Input: `root = [1,null,3]`
- Output: `[1, 3]`

## Constraints
- The tree has `0` to `100` nodes.
- `-100 <= Node.val <= 100`
""",
    "count-good-nodes-in-binary-tree": r"""## Problem
A node `X` in a binary tree is **good** if no node on the path from the root to `X` has
a value greater than `X`. Given the root, return the number of good nodes.

## Examples
**Example 1**
- Input: `root = [3,1,4,3,null,1,5]`
- Output: `4`

**Example 2**
- Input: `root = [3,3,null,4,2]`
- Output: `3`

## Constraints
- The tree has `1` to `10^5` nodes.
- `-10^4 <= Node.val <= 10^4`
""",
    "validate-binary-search-tree": r"""## Problem
Given the root of a binary tree, determine whether it is a valid binary search tree: at
every node, all values in the left subtree are strictly smaller and all values in the
right subtree are strictly larger, and both subtrees are themselves valid BSTs.

## Examples
**Example 1**
- Input: `root = [2,1,3]`
- Output: `true`

**Example 2**
- Input: `root = [5,1,4,null,null,3,6]`
- Output: `false`
- Explanation: `4` is in the right subtree of `5` but is smaller than `5`.

## Constraints
- The tree has `1` to `10^4` nodes.
- `-2^31 <= Node.val <= 2^31 - 1`
""",
    "kth-smallest-element-in-a-bst": r"""## Problem
Given the root of a binary search tree and an integer `k`, return the `k`-th smallest
value (1-indexed) among all the nodes.

## Examples
**Example 1**
- Input: `root = [3,1,4,null,2]`, `k = 1`
- Output: `1`

**Example 2**
- Input: `root = [5,3,6,2,4,null,null,1]`, `k = 3`
- Output: `3`

## Constraints
- The tree has `n` nodes, `1 <= k <= n <= 10^4`.
- `0 <= Node.val <= 10^4`
""",
    "construct-binary-tree-from-preorder-and-inorder-traversal": r"""## Problem
Given two integer arrays `preorder` and `inorder` representing the preorder and inorder
traversals of a binary tree (all values unique), reconstruct and return the tree.

## Examples
**Example 1**
- Input: `preorder = [3,9,20,15,7]`, `inorder = [9,3,15,20,7]`
- Output: `[3,9,20,null,null,15,7]`

**Example 2**
- Input: `preorder = [-1]`, `inorder = [-1]`
- Output: `[-1]`

## Constraints
- `1 <= preorder.length <= 3000`, same length as `inorder`.
- Values are unique; `inorder` is a permutation of `preorder`.
""",
    "binary-tree-maximum-path-sum": r"""## Problem
A path in a binary tree is a sequence of nodes connected by edges, where each node is
used at most once; the path need not pass through the root. Given the root, return the
maximum possible sum of node values along any such path.

## Examples
**Example 1**
- Input: `root = [1,2,3]`
- Output: `6`

**Example 2**
- Input: `root = [-10,9,20,null,null,15,7]`
- Output: `42`
- Explanation: `15 -> 20 -> 7`.

## Constraints
- The tree has `1` to `3 * 10^4` nodes.
- `-1000 <= Node.val <= 1000`
""",
    "serialize-and-deserialize-binary-tree": r"""## Problem
Design an algorithm to serialize a binary tree into a string and deserialize that
string back into the identical tree. The encoding format is up to you, as long as the
round trip reproduces the original tree.

## Examples
**Example 1**
- Input: `root = [1,2,3,null,null,4,5]`
- Output (after serialize then deserialize): `[1,2,3,null,null,4,5]`

**Example 2**
- Input: `root = []`
- Output: `[]`

## Constraints
- The tree has `0` to `10^4` nodes.
- `-1000 <= Node.val <= 1000`
""",

    # ---------------- Tries ----------------
    "implement-trie-prefix-tree": r"""## Problem
Implement a trie (prefix tree) supporting:

- `insert(word)` — add `word` to the trie.
- `search(word)` — return `true` if `word` was inserted exactly.
- `startsWith(prefix)` — return `true` if any inserted word begins with `prefix`.

## Examples
**Example 1**
- `insert("apple")`; `search("apple")` -> `true`; `search("app")` -> `false`;
  `startsWith("app")` -> `true`; `insert("app")`; `search("app")` -> `true`.

## Constraints
- `1 <= word.length, prefix.length <= 2000`, lowercase English letters.
- At most `3 * 10^4` calls total.
""",
    "design-add-and-search-words-data-structure": r"""## Problem
Design a data structure that supports adding words and searching with wildcards:

- `addWord(word)` — store `word`.
- `search(word)` — return `true` if any stored word matches `word`, where `.` can
  match any single letter.

## Examples
**Example 1**
- `addWord("bad")`; `addWord("dad")`; `addWord("mad")`; `search("pad")` -> `false`;
  `search("bad")` -> `true`; `search(".ad")` -> `true`; `search("b..")` -> `true`.

## Constraints
- `1 <= word.length <= 25`; `addWord` uses lowercase letters, `search` may include `.`.
- At most `10^4` calls total.
""",
    "word-search-ii": r"""## Problem
Given an `m x n` board of characters and a list of `words`, return all words from the
list that can be formed by sequentially adjacent cells (horizontally or vertically).
A single cell may not be used more than once within the same word.

## Examples
**Example 1**
- Input: `board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]`,
  `words = ["oath","pea","eat","rain"]`
- Output: `["eat", "oath"]`

**Example 2**
- Input: `board = [["a","b"],["c","d"]]`, `words = ["abcb"]`
- Output: `[]`

## Constraints
- `1 <= m, n <= 12`
- `1 <= words.length <= 3 * 10^4`, each word `1`–`10` lowercase letters.
""",

    # ---------------- Heap / Priority Queue ----------------
    "kth-largest-element-in-a-stream": r"""## Problem
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
""",
    "last-stone-weight": r"""## Problem
You have stones with positive integer weights. Each turn, smash the two heaviest
stones together: if equal, both are destroyed; otherwise the lighter is destroyed and
the heavier becomes their difference. Return the weight of the last remaining stone,
or `0` if none remain.

## Examples
**Example 1**
- Input: `stones = [2, 7, 4, 1, 8, 1]`
- Output: `1`

**Example 2**
- Input: `stones = [1]`
- Output: `1`

## Constraints
- `1 <= stones.length <= 30`
- `1 <= stones[i] <= 1000`
""",
    "k-closest-points-to-origin": r"""## Problem
Given an array of `points` on the plane and an integer `k`, return the `k` points
closest to the origin `(0, 0)` by Euclidean distance. The answer may be in any order;
it is guaranteed unique except for order.

## Examples
**Example 1**
- Input: `points = [[1,3],[-2,2]]`, `k = 1`
- Output: `[[-2,2]]`

**Example 2**
- Input: `points = [[3,3],[5,-1],[-2,4]]`, `k = 2`
- Output: `[[3,3],[-2,4]]`

## Constraints
- `1 <= k <= points.length <= 10^4`
- `-10^4 <= xi, yi <= 10^4`
""",
    "kth-largest-element-in-an-array": r"""## Problem
Given an integer array `nums` and an integer `k`, return the `k`-th largest element in
the array (by value, not distinct). Try to solve it without fully sorting.

## Examples
**Example 1**
- Input: `nums = [3, 2, 1, 5, 6, 4]`, `k = 2`
- Output: `5`

**Example 2**
- Input: `nums = [3,2,3,1,2,4,5,5,6]`, `k = 4`
- Output: `4`

## Constraints
- `1 <= k <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
""",
    "task-scheduler": r"""## Problem
Given an array of CPU `tasks` labeled A–Z and a cooldown `n`, each task takes one unit
of time. Two identical tasks must be separated by at least `n` units; the CPU may be
idle. Return the minimum total time units needed to finish all tasks.

## Examples
**Example 1**
- Input: `tasks = ["A","A","A","B","B","B"]`, `n = 2`
- Output: `8`
- Explanation: e.g. `A B idle A B idle A B`.

**Example 2**
- Input: `tasks = ["A","C","A","B","D","B"]`, `n = 1`
- Output: `6`

## Constraints
- `1 <= tasks.length <= 10^4`, tasks are uppercase letters.
- `0 <= n <= 100`
""",
    "design-twitter": r"""## Problem
Design a simplified Twitter. Implement:

- `postTweet(userId, tweetId)` — user posts a tweet.
- `getNewsFeed(userId)` — return the 10 most recent tweet IDs from the user and the
  people they follow, newest first.
- `follow(followerId, followeeId)` / `unfollow(followerId, followeeId)`.

## Examples
**Example 1**
- `postTweet(1, 5)`; `getNewsFeed(1)` -> `[5]`; `follow(1, 2)`; `postTweet(2, 6)`;
  `getNewsFeed(1)` -> `[6, 5]`; `unfollow(1, 2)`; `getNewsFeed(1)` -> `[5]`.

## Constraints
- `1 <= userId, followerId, followeeId <= 500`, `0 <= tweetId <= 10^4`.
- At most `3 * 10^4` calls total.
""",
    "find-median-from-data-stream": r"""## Problem
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
""",

    # ---------------- Backtracking ----------------
    "subsets": r"""## Problem
Given an array `nums` of **unique** integers, return all possible subsets (the power
set). The result must not contain duplicate subsets; any order is acceptable.

## Examples
**Example 1**
- Input: `nums = [1, 2, 3]`
- Output: `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`

**Example 2**
- Input: `nums = [0]`
- Output: `[[], [0]]`

## Constraints
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`, all unique.
""",
    "combination-sum": r"""## Problem
Given an array of **distinct** integers `candidates` and a `target`, return all unique
combinations whose elements sum to `target`. The same candidate may be chosen an
unlimited number of times; two combinations are different only if their multiset of
chosen numbers differs.

## Examples
**Example 1**
- Input: `candidates = [2, 3, 6, 7]`, `target = 7`
- Output: `[[2,2,3],[7]]`

**Example 2**
- Input: `candidates = [2, 3, 5]`, `target = 8`
- Output: `[[2,2,2,2],[2,3,3],[3,5]]`

## Constraints
- `1 <= candidates.length <= 30`, values distinct.
- `2 <= candidates[i] <= 40`, `1 <= target <= 500`.
""",
    "permutations": r"""## Problem
Given an array `nums` of distinct integers, return all possible permutations in any
order.

## Examples
**Example 1**
- Input: `nums = [1, 2, 3]`
- Output: `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

**Example 2**
- Input: `nums = [0, 1]`
- Output: `[[0,1],[1,0]]`

## Constraints
- `1 <= nums.length <= 6`
- `-10 <= nums[i] <= 10`, all unique.
""",
    "subsets-ii": r"""## Problem
Given an integer array `nums` that **may contain duplicates**, return all possible
subsets (the power set) without any duplicate subsets. Any order is fine.

## Examples
**Example 1**
- Input: `nums = [1, 2, 2]`
- Output: `[[],[1],[1,2],[1,2,2],[2],[2,2]]`

**Example 2**
- Input: `nums = [0]`
- Output: `[[], [0]]`

## Constraints
- `1 <= nums.length <= 10`
- `-10 <= nums[i] <= 10`
""",
    "combination-sum-ii": r"""## Problem
Given a collection of candidate numbers `candidates` (which may contain duplicates) and
a `target`, return all unique combinations summing to `target`. Each number may be
used **at most once** in a combination, and the result must not contain duplicate
combinations.

## Examples
**Example 1**
- Input: `candidates = [10,1,2,7,6,1,5]`, `target = 8`
- Output: `[[1,1,6],[1,2,5],[1,7],[2,6]]`

**Example 2**
- Input: `candidates = [2,5,2,1,2]`, `target = 5`
- Output: `[[1,2,2],[5]]`

## Constraints
- `1 <= candidates.length <= 100`
- `1 <= candidates[i] <= 50`, `1 <= target <= 30`.
""",
    "word-search": r"""## Problem
Given an `m x n` grid of characters `board` and a string `word`, return `true` if
`word` can be spelled out by a path of horizontally/vertically adjacent cells. The
same cell may not be reused within the path.

## Examples
**Example 1**
- Input: `board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]`, `word = "ABCCED"`
- Output: `true`

**Example 2**
- Input: same board, `word = "ABCB"`
- Output: `false`

## Constraints
- `1 <= m, n <= 6`
- `1 <= word.length <= 15`, all uppercase/lowercase English letters.
""",
    "palindrome-partitioning": r"""## Problem
Given a string `s`, partition it so that **every** substring in the partition is a
palindrome, and return all such partitionings.

## Examples
**Example 1**
- Input: `s = "aab"`
- Output: `[["a","a","b"],["aa","b"]]`

**Example 2**
- Input: `s = "a"`
- Output: `[["a"]]`

## Constraints
- `1 <= s.length <= 16`
- `s` contains only lowercase English letters.
""",
    "letter-combinations-of-a-phone-number": r"""## Problem
Given a string of digits `2`–`9`, return all possible letter combinations the number
could spell on a classic phone keypad (2->abc, 3->def, ..., 9->wxyz). Return the
answer in any order; an empty input yields an empty list.

## Examples
**Example 1**
- Input: `digits = "23"`
- Output: `["ad","ae","af","bd","be","bf","cd","ce","cf"]`

**Example 2**
- Input: `digits = ""`
- Output: `[]`

## Constraints
- `0 <= digits.length <= 4`
- Each digit is in `['2'..'9']`.
""",
    "n-queens": r"""## Problem
Place `n` queens on an `n x n` chessboard so that no two attack each other (no shared
row, column, or diagonal). Return all distinct solutions, each as a board where `'Q'`
marks a queen and `'.'` marks empty.

## Examples
**Example 1**
- Input: `n = 4`
- Output: `[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]`

**Example 2**
- Input: `n = 1`
- Output: `[["Q"]]`

## Constraints
- `1 <= n <= 9`
""",

    # ---------------- Graphs ----------------
    "number-of-islands": r"""## Problem
Given an `m x n` grid of `'1'` (land) and `'0'` (water), return the number of islands.
An island is a maximal group of land cells connected horizontally or vertically; all
edges of the grid are surrounded by water.

## Examples
**Example 1**
- Input: `grid = [["1","1","0","0"],["1","1","0","0"],["0","0","1","0"],["0","0","0","1"]]`
- Output: `3`

**Example 2**
- Input: `grid = [["1","1","1"],["0","1","0"],["1","1","1"]]`
- Output: `1`

## Constraints
- `1 <= m, n <= 300`
- Each cell is `'0'` or `'1'`.
""",
    "clone-graph": r"""## Problem
Given a reference to a node in a connected, undirected graph, return a **deep copy** of
the entire graph. Each node holds an integer value and a list of its neighbors.

## Examples
**Example 1**
- Input: `adjList = [[2,4],[1,3],[2,4],[1,3]]`
- Output: a deep copy with the same structure.

**Example 2**
- Input: `adjList = [[]]` (a single node with no neighbors)
- Output: a single-node copy.

## Constraints
- `0 <= number of nodes <= 100`
- `1 <= Node.val <= 100`, values unique; the graph is connected and undirected.
""",
    "max-area-of-island": r"""## Problem
Given an `m x n` binary grid where `1` is land and `0` is water, return the area (cell
count) of the largest island. Cells connect horizontally or vertically. If there is no
island, return `0`.

## Examples
**Example 1**
- Input: a grid whose largest connected land region has 6 cells.
- Output: `6`

**Example 2**
- Input: `grid = [[0,0,0],[0,0,0]]`
- Output: `0`

## Constraints
- `1 <= m, n <= 50`
- Each cell is `0` or `1`.
""",
    "pacific-atlantic-water-flow": r"""## Problem
Given an `m x n` matrix of cell heights, the Pacific ocean touches the top and left
edges, the Atlantic touches the bottom and right edges. Water flows from a cell to a
neighbor of **equal or lower** height. Return all cells `[r, c]` from which water can
reach **both** oceans.

## Examples
**Example 1**
- Input: `heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]`
- Output: `[[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]`

**Example 2**
- Input: `heights = [[1]]`
- Output: `[[0, 0]]`

## Constraints
- `1 <= m, n <= 200`
- `0 <= heights[r][c] <= 10^5`
""",
    "surrounded-regions": r"""## Problem
Given an `m x n` board of `'X'` and `'O'`, capture all regions of `'O'` that are fully
surrounded by `'X'` by flipping them to `'X'`. An `'O'` region is **not** captured if
any of its cells touches the border. Modify the board in place.

## Examples
**Example 1**
- Input: `board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]`
- Output: `[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]`

**Example 2**
- Input: `board = [["X"]]`
- Output: `[["X"]]`

## Constraints
- `1 <= m, n <= 200`
- Each cell is `'X'` or `'O'`.
""",
    "rotting-oranges": r"""## Problem
In an `m x n` grid, each cell is `0` (empty), `1` (fresh orange), or `2` (rotten). Each
minute, any fresh orange adjacent (4-directionally) to a rotten one becomes rotten.
Return the minimum minutes until no fresh orange remains, or `-1` if impossible.

## Examples
**Example 1**
- Input: `grid = [[2,1,1],[1,1,0],[0,1,1]]`
- Output: `4`

**Example 2**
- Input: `grid = [[2,1,1],[0,1,1],[1,0,1]]`
- Output: `-1`

## Constraints
- `1 <= m, n <= 10`
- Each cell is `0`, `1`, or `2`.
""",
    "walls-and-gates": r"""## Problem
You are given an `m x n` grid where `-1` is a wall, `0` is a gate, and `INF`
(`2^31 - 1`) is an empty room. Fill each empty room with the distance to its nearest
gate (moving 4-directionally). If a room cannot reach any gate, leave it as `INF`.
Modify the grid in place.

## Examples
**Example 1**
- Input: `rooms = [[INF,-1,0,INF],[INF,INF,INF,-1],[INF,-1,INF,-1],[0,-1,INF,INF]]`
- Output: `[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]`

**Example 2**
- Input: `rooms = [[-1]]`
- Output: `[[-1]]`

## Constraints
- `1 <= m, n <= 250`
- Each cell is `-1`, `0`, or `2^31 - 1`.
""",
    "course-schedule": r"""## Problem
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
""",
    "course-schedule-ii": r"""## Problem
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
""",
    "redundant-connection": r"""## Problem
A tree with `n` nodes (labeled `1`–`n`) had exactly one extra edge added, forming a
single cycle. Given `edges`, return the one edge that can be removed so the result is
again a tree. If multiple answers exist, return the one that appears last in `edges`.

## Examples
**Example 1**
- Input: `edges = [[1,2],[1,3],[2,3]]`
- Output: `[2, 3]`

**Example 2**
- Input: `edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]`
- Output: `[1, 4]`

## Constraints
- `n == edges.length`, `3 <= n <= 1000`
- No repeated edges or self-loops; the graph is connected.
""",
    "number-of-connected-components-in-an-undirected-graph": r"""## Problem
Given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, return the
number of connected components in the graph.

## Examples
**Example 1**
- Input: `n = 5`, `edges = [[0,1],[1,2],[3,4]]`
- Output: `2`

**Example 2**
- Input: `n = 5`, `edges = [[0,1],[1,2],[2,3],[3,4]]`
- Output: `1`

## Constraints
- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`, no self-loops or duplicate edges.
""",
    "graph-valid-tree": r"""## Problem
Given `n` nodes labeled `0` to `n - 1` and a list of undirected `edges`, return `true`
if these edges form a valid tree — the graph is fully connected and contains no
cycles.

## Examples
**Example 1**
- Input: `n = 5`, `edges = [[0,1],[0,2],[0,3],[1,4]]`
- Output: `true`

**Example 2**
- Input: `n = 5`, `edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]`
- Output: `false`

## Constraints
- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`, no self-loops or duplicate edges.
""",
    "word-ladder": r"""## Problem
Given two words `beginWord` and `endWord` and a `wordList`, return the length of the
shortest transformation sequence from `beginWord` to `endWord`, changing exactly one
letter at a time, where every intermediate word must be in `wordList`. Return `0` if
no such sequence exists. The length counts the number of words in the sequence.

## Examples
**Example 1**
- Input: `beginWord = "hit"`, `endWord = "cog"`, `wordList = ["hot","dot","dog","lot","log","cog"]`
- Output: `5`
- Explanation: `hit -> hot -> dot -> dog -> cog`.

**Example 2**
- Input: same as above but `wordList = ["hot","dot","dog","lot","log"]`
- Output: `0`

## Constraints
- `1 <= beginWord.length <= 10`, all words equal length, lowercase letters.
- `1 <= wordList.length <= 5000`, words unique.
""",

    # ---------------- Advanced Graphs ----------------
    "reconstruct-itinerary": r"""## Problem
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
""",
    "min-cost-to-connect-all-points": r"""## Problem
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
""",
    "network-delay-time": r"""## Problem
A network has `n` nodes labeled `1`–`n`. `times[i] = [u, v, w]` is a directed edge
from `u` to `v` taking `w` time. A signal starts at node `k`. Return the time for all
nodes to receive it, or `-1` if some node is unreachable.

## Examples
**Example 1**
- Input: `times = [[2,1,1],[2,3,1],[3,4,1]]`, `n = 4`, `k = 2`
- Output: `2`

**Example 2**
- Input: `times = [[1,2,1]]`, `n = 2`, `k = 2`
- Output: `-1`

## Constraints
- `1 <= k <= n <= 100`
- `1 <= times.length <= 6000`, `1 <= w <= 100`, no self-loops or duplicate edges.
""",
    "swim-in-rising-water": r"""## Problem
Given an `n x n` grid where `grid[r][c]` is the elevation at that cell, water rises so
that at time `t` every cell with elevation at most `t` is submerged. Starting at the
top-left cell at time 0, you can swim to a 4-directionally adjacent cell instantly only
if both cells are submerged. Return the least time to reach the bottom-right cell.

## Examples
**Example 1**
- Input: `grid = [[0,2],[1,3]]`
- Output: `3`

**Example 2**
- Input: `grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]`
- Output: `16`

## Constraints
- `1 <= n <= 50`
- `grid` is a permutation of `0 .. n*n - 1`.
""",
    "alien-dictionary": r"""## Problem
A new language uses lowercase letters in an unknown order. Given a list of `words`
sorted according to this language's alphabet, derive any valid ordering of its letters
as a string. If the ordering is invalid (contradictory), return `""`. If multiple
orderings are valid, any is accepted.

## Examples
**Example 1**
- Input: `words = ["wrt","wrf","er","ett","rftt"]`
- Output: `"wertf"`

**Example 2**
- Input: `words = ["z", "x"]`
- Output: `"zx"`

**Example 3**
- Input: `words = ["abc", "ab"]`  (prefix appears after its extension)
- Output: `""`

## Constraints
- `1 <= words.length <= 100`, `1 <= words[i].length <= 100`, lowercase letters.
""",
    "cheapest-flights-within-k-stops": r"""## Problem
There are `n` cities connected by `flights` `[from, to, price]`. Given `src`, `dst`,
and `k`, return the cheapest price to fly from `src` to `dst` using at most `k`
intermediate stops. If no such route exists, return `-1`.

## Examples
**Example 1**
- Input: `n = 4`, `flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]`,
  `src = 0`, `dst = 3`, `k = 1`
- Output: `700`

**Example 2**
- Input: `n = 3`, `flights = [[0,1,100],[1,2,100],[0,2,500]]`, `src = 0`, `dst = 2`, `k = 0`
- Output: `500`

## Constraints
- `1 <= n <= 100`, `0 <= flights.length <= n * (n - 1)`
- `0 <= src, dst, k < n`, `src != dst`, `1 <= price <= 10^4`.
""",

    # ---------------- 1-D DP ----------------
    "climbing-stairs": r"""## Problem
You are climbing a staircase that takes `n` steps to reach the top. Each move you can
climb either 1 or 2 steps. Return the number of distinct ways to reach the top.

## Examples
**Example 1**
- Input: `n = 2`
- Output: `2`  (`1+1`, `2`)

**Example 2**
- Input: `n = 3`
- Output: `3`  (`1+1+1`, `1+2`, `2+1`)

## Constraints
- `1 <= n <= 45`
""",
    "min-cost-climbing-stairs": r"""## Problem
Given an array `cost` where `cost[i]` is the cost of step `i`, you pay the cost to step
on `i` then climb 1 or 2 steps. You may start at index 0 or index 1. Return the
minimum total cost to reach the top (just past the last step).

## Examples
**Example 1**
- Input: `cost = [10, 15, 20]`
- Output: `15`

**Example 2**
- Input: `cost = [1,100,1,1,1,100,1,1,100,1]`
- Output: `6`

## Constraints
- `2 <= cost.length <= 1000`
- `0 <= cost[i] <= 999`
""",
    "house-robber": r"""## Problem
Given an array `nums` of money in each house along a street, return the maximum amount
you can rob without robbing two **adjacent** houses (which would alert the police).

## Examples
**Example 1**
- Input: `nums = [1, 2, 3, 1]`
- Output: `4`  (rob houses 0 and 2)

**Example 2**
- Input: `nums = [2, 7, 9, 3, 1]`
- Output: `12`  (rob houses 0, 2, 4)

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 400`
""",
    "house-robber-ii": r"""## Problem
Same as House Robber, but the houses are arranged in a **circle**: the first and last
houses are adjacent. Return the maximum amount you can rob without taking from two
adjacent houses.

## Examples
**Example 1**
- Input: `nums = [2, 3, 2]`
- Output: `3`  (you cannot rob both house 0 and house 2)

**Example 2**
- Input: `nums = [1, 2, 3, 1]`
- Output: `4`

## Constraints
- `1 <= nums.length <= 100`
- `0 <= nums[i] <= 1000`
""",
    "longest-palindromic-substring": r"""## Problem
Given a string `s`, return the longest contiguous substring that is a palindrome. If
several have the same maximal length, any one of them is acceptable.

## Examples
**Example 1**
- Input: `s = "babad"`
- Output: `"bab"`  (or `"aba"`)

**Example 2**
- Input: `s = "cbbd"`
- Output: `"bb"`

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of digits and English letters.
""",
    "palindromic-substrings": r"""## Problem
Given a string `s`, count how many of its substrings are palindromes. Substrings at
different start/end positions are counted separately even if identical in content.

## Examples
**Example 1**
- Input: `s = "abc"`
- Output: `3`  (`"a"`, `"b"`, `"c"`)

**Example 2**
- Input: `s = "aaa"`
- Output: `6`

## Constraints
- `1 <= s.length <= 1000`
- `s` consists of lowercase English letters.
""",
    "decode-ways": r"""## Problem
A message of digits is encoded with the mapping `1 -> A`, `2 -> B`, ..., `26 -> Z`.
Given a digit string `s`, return the number of ways to decode it. Leading zeros are
invalid (e.g. `"06"` cannot be decoded).

## Examples
**Example 1**
- Input: `s = "12"`
- Output: `2`  (`"AB"` or `"L"`)

**Example 2**
- Input: `s = "226"`
- Output: `3`  (`"BBF"`, `"BZ"`, `"VF"`)

**Example 3**
- Input: `s = "06"`
- Output: `0`

## Constraints
- `1 <= s.length <= 100`
- `s` contains only digits and may contain leading zeros.
""",
    "coin-change": r"""## Problem
Given coin denominations `coins` and a target `amount`, return the fewest number of
coins needed to make up that amount. You have an unlimited supply of each coin. If the
amount cannot be made, return `-1`.

## Examples
**Example 1**
- Input: `coins = [1, 2, 5]`, `amount = 11`
- Output: `3`  (`5 + 5 + 1`)

**Example 2**
- Input: `coins = [2]`, `amount = 3`
- Output: `-1`

## Constraints
- `1 <= coins.length <= 12`
- `1 <= coins[i] <= 2^31 - 1`, `0 <= amount <= 10^4`.
""",
    "maximum-product-subarray": r"""## Problem
Given an integer array `nums`, find the contiguous non-empty subarray with the largest
product, and return that product. The answer fits in a 32-bit integer.

## Examples
**Example 1**
- Input: `nums = [2, 3, -2, 4]`
- Output: `6`  (subarray `[2, 3]`)

**Example 2**
- Input: `nums = [-2, 0, -1]`
- Output: `0`

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
""",
    "word-break": r"""## Problem
Given a string `s` and a dictionary `wordDict`, return `true` if `s` can be segmented
into a space-separated sequence of one or more dictionary words. Dictionary words may
be reused any number of times.

## Examples
**Example 1**
- Input: `s = "leetcode"`, `wordDict = ["leet", "code"]`
- Output: `true`

**Example 2**
- Input: `s = "applepenapple"`, `wordDict = ["apple", "pen"]`
- Output: `true`

**Example 3**
- Input: `s = "catsandog"`, `wordDict = ["cats","dog","sand","and","cat"]`
- Output: `false`

## Constraints
- `1 <= s.length <= 300`, `1 <= wordDict.length <= 1000`
- Dictionary words are unique; all lowercase English letters.
""",
    "longest-increasing-subsequence": r"""## Problem
Given an integer array `nums`, return the length of the longest strictly increasing
subsequence (elements need not be contiguous, but must keep their relative order).

## Examples
**Example 1**
- Input: `nums = [10, 9, 2, 5, 3, 7, 101, 18]`
- Output: `4`  (e.g. `[2, 3, 7, 101]`)

**Example 2**
- Input: `nums = [0, 1, 0, 3, 2, 3]`
- Output: `4`

## Constraints
- `1 <= nums.length <= 2500`
- `-10^4 <= nums[i] <= 10^4`

**Follow-up:** Can you achieve `O(n log n)` time?
""",
    "partition-equal-subset-sum": r"""## Problem
Given an array of positive integers `nums`, return `true` if it can be split into two
subsets whose sums are equal.

## Examples
**Example 1**
- Input: `nums = [1, 5, 11, 5]`
- Output: `true`  (`[1, 5, 5]` and `[11]`)

**Example 2**
- Input: `nums = [1, 2, 3, 5]`
- Output: `false`

## Constraints
- `1 <= nums.length <= 200`
- `1 <= nums[i] <= 100`
""",

    # ---------------- 2-D DP ----------------
    "unique-paths": r"""## Problem
A robot starts at the top-left of an `m x n` grid and wants to reach the bottom-right.
It can only move right or down. Return the number of distinct paths.

## Examples
**Example 1**
- Input: `m = 3`, `n = 7`
- Output: `28`

**Example 2**
- Input: `m = 3`, `n = 2`
- Output: `3`

## Constraints
- `1 <= m, n <= 100`
- The answer fits in a 32-bit integer.
""",
    "longest-common-subsequence": r"""## Problem
Given two strings `text1` and `text2`, return the length of their longest common
subsequence (characters appearing in both, in the same relative order, not necessarily
contiguous). Return `0` if there is none.

## Examples
**Example 1**
- Input: `text1 = "abcde"`, `text2 = "ace"`
- Output: `3`  (`"ace"`)

**Example 2**
- Input: `text1 = "abc"`, `text2 = "def"`
- Output: `0`

## Constraints
- `1 <= text1.length, text2.length <= 1000`
- Both consist of lowercase English letters.
""",
    "best-time-to-buy-and-sell-stock-with-cooldown": r"""## Problem
Given an array `prices` of daily stock prices, find the maximum profit from as many
buy/sell transactions as you like, with two rules: you can hold at most one share at a
time, and after you sell you must wait one day (cooldown) before buying again.

## Examples
**Example 1**
- Input: `prices = [1, 2, 3, 0, 2]`
- Output: `3`  (buy, sell, cooldown, buy, sell)

**Example 2**
- Input: `prices = [1]`
- Output: `0`

## Constraints
- `1 <= prices.length <= 5000`
- `0 <= prices[i] <= 1000`
""",
    "coin-change-ii": r"""## Problem
Given an `amount` and coin denominations `coins` (unlimited supply of each), return the
number of distinct combinations that make up the amount. Combinations differing only
in order count as one.

## Examples
**Example 1**
- Input: `amount = 5`, `coins = [1, 2, 5]`
- Output: `4`

**Example 2**
- Input: `amount = 3`, `coins = [2]`
- Output: `0`

## Constraints
- `1 <= coins.length <= 300`, coins distinct.
- `1 <= coins[i] <= 5000`, `0 <= amount <= 5000`.
""",
    "target-sum": r"""## Problem
Given an array of non-negative integers `nums` and an integer `target`, assign a `+` or
`-` sign to each number so the signed sum equals `target`. Return the number of ways to
do this.

## Examples
**Example 1**
- Input: `nums = [1, 1, 1, 1, 1]`, `target = 3`
- Output: `5`

**Example 2**
- Input: `nums = [1]`, `target = 1`
- Output: `1`

## Constraints
- `1 <= nums.length <= 20`
- `0 <= nums[i] <= 1000`, `0 <= sum(nums) <= 1000`
- `-1000 <= target <= 1000`
""",
    "interleaving-string": r"""## Problem
Given strings `s1`, `s2`, and `s3`, return `true` if `s3` is formed by interleaving
`s1` and `s2` — i.e. `s3` can be split into pieces that, read in order, alternate
between (preserving order of) the characters of `s1` and `s2`.

## Examples
**Example 1**
- Input: `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbcbcac"`
- Output: `true`

**Example 2**
- Input: `s1 = "aabcc"`, `s2 = "dbbca"`, `s3 = "aadbbbaccc"`
- Output: `false`

**Example 3**
- Input: `s1 = ""`, `s2 = ""`, `s3 = ""`
- Output: `true`

## Constraints
- `0 <= s1.length, s2.length <= 100`, `0 <= s3.length <= 200`
- All strings consist of lowercase English letters.
""",
    "longest-increasing-path-in-a-matrix": r"""## Problem
Given an `m x n` integer matrix, return the length of the longest strictly increasing
path. From a cell you may move to a 4-directionally adjacent cell with a strictly
greater value; you may not move diagonally or wrap around.

## Examples
**Example 1**
- Input: `matrix = [[9,9,4],[6,6,8],[2,1,1]]`
- Output: `4`  (`1 -> 2 -> 6 -> 9`)

**Example 2**
- Input: `matrix = [[3,4,5],[3,2,6],[2,2,1]]`
- Output: `4`  (`3 -> 4 -> 5 -> 6`)

## Constraints
- `1 <= m, n <= 200`
- `0 <= matrix[i][j] <= 2^31 - 1`
""",
    "distinct-subsequences": r"""## Problem
Given two strings `s` and `t`, return the number of distinct subsequences of `s` that
equal `t`. A subsequence keeps relative order but may drop characters. The answer fits
in a 32-bit signed integer.

## Examples
**Example 1**
- Input: `s = "rabbbit"`, `t = "rabbit"`
- Output: `3`

**Example 2**
- Input: `s = "babgbag"`, `t = "bag"`
- Output: `5`

## Constraints
- `1 <= s.length, t.length <= 1000`
- `s` and `t` consist of English letters.
""",
    "edit-distance": r"""## Problem
Given two strings `word1` and `word2`, return the minimum number of single-character
operations (insert, delete, or replace) needed to turn `word1` into `word2`.

## Examples
**Example 1**
- Input: `word1 = "horse"`, `word2 = "ros"`
- Output: `3`

**Example 2**
- Input: `word1 = "intention"`, `word2 = "execution"`
- Output: `5`

## Constraints
- `0 <= word1.length, word2.length <= 500`
- Both consist of lowercase English letters.
""",
    "burst-balloons": r"""## Problem
Given `n` balloons with values in `nums`, bursting balloon `i` earns
`nums[i-1] * nums[i] * nums[i+1]` coins (treat out-of-range neighbors as `1`). After a
burst its neighbors become adjacent. Return the maximum coins you can collect by
bursting all balloons in some order.

## Examples
**Example 1**
- Input: `nums = [3, 1, 5, 8]`
- Output: `167`

**Example 2**
- Input: `nums = [1, 5]`
- Output: `10`

## Constraints
- `1 <= n <= 300`
- `0 <= nums[i] <= 100`
""",
    "regular-expression-matching": r"""## Problem
Implement regular expression matching with support for `.` (matches any single
character) and `*` (matches zero or more of the **preceding** element). Given an input
string `s` and a pattern `p`, return `true` if the pattern matches the **entire**
string.

## Examples
**Example 1**
- Input: `s = "aa"`, `p = "a*"`
- Output: `true`

**Example 2**
- Input: `s = "ab"`, `p = ".*"`
- Output: `true`

**Example 3**
- Input: `s = "mississippi"`, `p = "mis*is*p*."`
- Output: `false`

## Constraints
- `1 <= s.length <= 20`, `1 <= p.length <= 30`
- `s` is lowercase letters; `p` is lowercase letters, `.`, and `*`; each `*` has a
  valid preceding element.
""",

    # ---------------- Greedy ----------------
    "maximum-subarray": r"""## Problem
Given an integer array `nums`, find the contiguous non-empty subarray with the largest
sum and return that sum.

## Examples
**Example 1**
- Input: `nums = [-2,1,-3,4,-1,2,1,-5,4]`
- Output: `6`  (subarray `[4, -1, 2, 1]`)

**Example 2**
- Input: `nums = [1]`
- Output: `1`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
""",
    "jump-game": r"""## Problem
Given an integer array `nums` where `nums[i]` is the maximum jump length from index
`i`, you start at index 0. Return `true` if you can reach the last index.

## Examples
**Example 1**
- Input: `nums = [2, 3, 1, 1, 4]`
- Output: `true`

**Example 2**
- Input: `nums = [3, 2, 1, 0, 4]`
- Output: `false`

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 10^5`
""",
    "jump-game-ii": r"""## Problem
Given `nums` where `nums[i]` is the maximum jump length from index `i`, return the
minimum number of jumps needed to reach the last index. The test cases guarantee the
last index is reachable.

## Examples
**Example 1**
- Input: `nums = [2, 3, 1, 1, 4]`
- Output: `2`

**Example 2**
- Input: `nums = [2, 3, 0, 1, 4]`
- Output: `2`

## Constraints
- `1 <= nums.length <= 10^4`
- `0 <= nums[i] <= 1000`, the last index is always reachable.
""",
    "gas-station": r"""## Problem
There are `n` gas stations in a circle. `gas[i]` is the fuel at station `i`, and
`cost[i]` is the fuel needed to travel from station `i` to `i + 1`. With an empty tank,
return the starting station index from which you can complete the full loop, or `-1`
if impossible. A unique answer is guaranteed when one exists.

## Examples
**Example 1**
- Input: `gas = [1, 2, 3, 4, 5]`, `cost = [3, 4, 5, 1, 2]`
- Output: `3`

**Example 2**
- Input: `gas = [2, 3, 4]`, `cost = [3, 4, 3]`
- Output: `-1`

## Constraints
- `n == gas.length == cost.length`, `1 <= n <= 10^5`
- `0 <= gas[i], cost[i] <= 10^4`
""",
    "hand-of-straights": r"""## Problem
Given an array `hand` of integers and a group size `groupSize`, return `true` if the
cards can be rearranged into groups of `groupSize` consecutive cards each.

## Examples
**Example 1**
- Input: `hand = [1,2,3,6,2,3,4,7,8]`, `groupSize = 3`
- Output: `true`  (`[1,2,3]`, `[2,3,4]`, `[6,7,8]`)

**Example 2**
- Input: `hand = [1, 2, 3, 4, 5]`, `groupSize = 4`
- Output: `false`

## Constraints
- `1 <= hand.length <= 10^4`
- `0 <= hand[i] <= 10^9`, `1 <= groupSize <= hand.length`.
""",
    "merge-triplets-to-form-target-triplet": r"""## Problem
You have a list of `triplets` `[a, b, c]` and a `target` triplet. You may repeatedly
pick two triplets and replace them with their element-wise maximum. Return `true` if
it is possible to obtain the `target` triplet using some sequence of such merges.

## Examples
**Example 1**
- Input: `triplets = [[2,5,3],[1,8,4],[1,7,5]]`, `target = [2, 7, 5]`
- Output: `true`

**Example 2**
- Input: `triplets = [[3,4,5],[4,5,6]]`, `target = [3, 2, 5]`
- Output: `false`

## Constraints
- `1 <= triplets.length <= 10^5`
- `1 <= ai, bi, ci, target values <= 1000`
""",
    "partition-labels": r"""## Problem
Given a string `s`, partition it into as many parts as possible so that each letter
appears in at most one part. Return a list of the sizes of these parts, in order. The
parts concatenated must reproduce `s`.

## Examples
**Example 1**
- Input: `s = "ababcbacadefegdehijhklij"`
- Output: `[9, 7, 8]`

**Example 2**
- Input: `s = "eccbbbbdec"`
- Output: `[10]`

## Constraints
- `1 <= s.length <= 500`
- `s` consists of lowercase English letters.
""",
    "valid-parenthesis-string": r"""## Problem
Given a string `s` containing `(`, `)`, and `*`, return `true` if it can be a valid
parenthesis string. A `*` may stand for a single `(`, a single `)`, or an empty string.

## Examples
**Example 1**
- Input: `s = "()"`
- Output: `true`

**Example 2**
- Input: `s = "(*)"`
- Output: `true`

**Example 3**
- Input: `s = "(*))"`
- Output: `true`

## Constraints
- `1 <= s.length <= 100`
- `s` consists of `(`, `)`, and `*`.
""",

    # ---------------- Intervals ----------------
    "insert-interval": r"""## Problem
Given a list of non-overlapping `intervals` sorted by start, and a `newInterval`,
insert the new interval and merge as needed so the result stays sorted and
non-overlapping. Return the resulting list.

## Examples
**Example 1**
- Input: `intervals = [[1,3],[6,9]]`, `newInterval = [2, 5]`
- Output: `[[1,5],[6,9]]`

**Example 2**
- Input: `intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]`, `newInterval = [4, 8]`
- Output: `[[1,2],[3,10],[12,16]]`

## Constraints
- `0 <= intervals.length <= 10^4`, sorted by start, non-overlapping.
- `0 <= start <= end <= 10^5`
""",
    "merge-intervals": r"""## Problem
Given an array of `intervals` where `intervals[i] = [start, end]`, merge all
overlapping intervals and return the non-overlapping intervals that cover all the
input ranges.

## Examples
**Example 1**
- Input: `intervals = [[1,3],[2,6],[8,10],[15,18]]`
- Output: `[[1,6],[8,10],[15,18]]`

**Example 2**
- Input: `intervals = [[1,4],[4,5]]`
- Output: `[[1,5]]`

## Constraints
- `1 <= intervals.length <= 10^4`
- `0 <= start <= end <= 10^4`
""",
    "non-overlapping-intervals": r"""## Problem
Given an array of `intervals`, return the minimum number of intervals you must remove
so that the rest are non-overlapping. Intervals that merely touch at an endpoint
(e.g. `[1,2]` and `[2,3]`) are not considered overlapping.

## Examples
**Example 1**
- Input: `intervals = [[1,2],[2,3],[3,4],[1,3]]`
- Output: `1`

**Example 2**
- Input: `intervals = [[1,2],[1,2],[1,2]]`
- Output: `2`

## Constraints
- `1 <= intervals.length <= 10^5`
- `-5 * 10^4 <= start < end <= 5 * 10^4`
""",
    "meeting-rooms": r"""## Problem
Given an array of meeting time `intervals` `[start, end]`, determine whether a single
person could attend all meetings — i.e. no two meetings overlap. Meetings that end
exactly when another begins do not conflict.

## Examples
**Example 1**
- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `false`

**Example 2**
- Input: `intervals = [[7,10],[2,4]]`
- Output: `true`

## Constraints
- `0 <= intervals.length <= 10^4`
- `0 <= start < end <= 10^6`
""",
    "meeting-rooms-ii": r"""## Problem
Given an array of meeting time `intervals` `[start, end]`, return the minimum number of
conference rooms required so that no two simultaneous meetings share a room.

## Examples
**Example 1**
- Input: `intervals = [[0,30],[5,10],[15,20]]`
- Output: `2`

**Example 2**
- Input: `intervals = [[7,10],[2,4]]`
- Output: `1`

## Constraints
- `1 <= intervals.length <= 10^4`
- `0 <= start < end <= 10^6`
""",
    "minimum-interval-to-include-each-query": r"""## Problem
Given a list of `intervals` `[left, right]` and an array of `queries`, for each query
`q` return the size (`right - left + 1`) of the **smallest** interval that contains
`q` (`left <= q <= right`). If no interval contains `q`, the answer is `-1`. Return the
answers in query order.

## Examples
**Example 1**
- Input: `intervals = [[1,4],[2,4],[3,6],[4,4]]`, `queries = [2, 3, 4, 5]`
- Output: `[3, 3, 1, 4]`

**Example 2**
- Input: `intervals = [[2,3],[2,5],[1,8],[20,25]]`, `queries = [2, 19, 5, 22]`
- Output: `[2, -1, 4, 6]`

## Constraints
- `1 <= intervals.length, queries.length <= 10^5`
- `1 <= left <= right <= 10^7`, `1 <= q <= 10^7`.
""",

    # ---------------- Math & Geometry ----------------
    "rotate-image": r"""## Problem
Given an `n x n` 2D `matrix` representing an image, rotate it 90 degrees clockwise.
You must do it **in place** — do not allocate another matrix.

## Examples
**Example 1**
- Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[[7,4,1],[8,5,2],[9,6,3]]`

**Example 2**
- Input: `matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]`
- Output: `[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]`

## Constraints
- `n == matrix.length == matrix[i].length`, `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`
""",
    "spiral-matrix": r"""## Problem
Given an `m x n` matrix, return all of its elements in spiral order (clockwise starting
from the top-left).

## Examples
**Example 1**
- Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[1,2,3,6,9,8,7,4,5]`

**Example 2**
- Input: `matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]`
- Output: `[1,2,3,4,8,12,11,10,9,5,6,7]`

## Constraints
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`
""",
    "set-matrix-zeroes": r"""## Problem
Given an `m x n` matrix, if any element is `0`, set its entire row and column to `0`.
Do it **in place**. (The follow-up asks for `O(1)` extra space.)

## Examples
**Example 1**
- Input: `matrix = [[1,1,1],[1,0,1],[1,1,1]]`
- Output: `[[1,0,1],[0,0,0],[1,0,1]]`

**Example 2**
- Input: `matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]`
- Output: `[[0,0,0,0],[0,4,5,0],[0,3,1,0]]`

## Constraints
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`
""",
    "happy-number": r"""## Problem
A number is "happy" if repeatedly replacing it with the sum of the squares of its
digits eventually reaches `1`. If the process loops endlessly without hitting `1`, the
number is not happy. Given `n`, return `true` if it is a happy number.

## Examples
**Example 1**
- Input: `n = 19`
- Output: `true`  (`1+81=82 -> 68 -> 100 -> 1`)

**Example 2**
- Input: `n = 2`
- Output: `false`

## Constraints
- `1 <= n <= 2^31 - 1`
""",
    "plus-one": r"""## Problem
Given a large integer represented as an array of its `digits` (most significant first,
no leading zeros), add one to the integer and return the resulting array of digits.

## Examples
**Example 1**
- Input: `digits = [1, 2, 3]`
- Output: `[1, 2, 4]`

**Example 2**
- Input: `digits = [9]`
- Output: `[1, 0]`

## Constraints
- `1 <= digits.length <= 100`
- `0 <= digits[i] <= 9`, no leading zeros.
""",
    "powx-n": r"""## Problem
Implement `pow(x, n)`, which raises `x` (a double) to the integer power `n`. Handle
negative exponents. Aim for `O(log n)` time.

## Examples
**Example 1**
- Input: `x = 2.00000`, `n = 10`
- Output: `1024.00000`

**Example 2**
- Input: `x = 2.10000`, `n = 3`
- Output: `9.26100`

**Example 3**
- Input: `x = 2.00000`, `n = -2`
- Output: `0.25000`

## Constraints
- `-100.0 < x < 100.0`
- `-2^31 <= n <= 2^31 - 1`, and either `x != 0` or `n > 0`.
""",
    "multiply-strings": r"""## Problem
Given two non-negative integers represented as strings `num1` and `num2`, return their
product as a string. You must not use any built-in big-integer library or convert the
inputs to integers directly.

## Examples
**Example 1**
- Input: `num1 = "2"`, `num2 = "3"`
- Output: `"6"`

**Example 2**
- Input: `num1 = "123"`, `num2 = "456"`
- Output: `"56088"`

## Constraints
- `1 <= num1.length, num2.length <= 200`
- Both contain only digits and have no leading zeros (except "0" itself).
""",
    "detect-squares": r"""## Problem
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
""",

    # ---------------- Bit Manipulation ----------------
    "single-number": r"""## Problem
Given a non-empty array `nums` where every element appears twice except for one,
return that single element. Solve it in linear time with constant extra space.

## Examples
**Example 1**
- Input: `nums = [2, 2, 1]`
- Output: `1`

**Example 2**
- Input: `nums = [4, 1, 2, 1, 2]`
- Output: `4`

## Constraints
- `1 <= nums.length <= 3 * 10^4`
- `-3 * 10^4 <= nums[i] <= 3 * 10^4`; exactly one element appears once.
""",
    "number-of-1-bits": r"""## Problem
Write a function that takes an unsigned integer and returns the number of `1` bits in
its binary representation (also known as the Hamming weight).

## Examples
**Example 1**
- Input: `n = 11` (binary `1011`)
- Output: `3`

**Example 2**
- Input: `n = 128` (binary `10000000`)
- Output: `1`

## Constraints
- The input is a 32-bit integer.

**Follow-up:** If this function is called many times, how would you optimize it?
""",
    "counting-bits": r"""## Problem
Given an integer `n`, return an array `ans` of length `n + 1` where `ans[i]` is the
number of `1` bits in the binary representation of `i`, for every `i` from `0` to `n`.

## Examples
**Example 1**
- Input: `n = 2`
- Output: `[0, 1, 1]`

**Example 2**
- Input: `n = 5`
- Output: `[0, 1, 1, 2, 1, 2]`

## Constraints
- `0 <= n <= 10^5`

**Follow-up:** Can you do it in `O(n)` time using a single pass?
""",
    "reverse-bits": r"""## Problem
Reverse the bits of a given 32-bit unsigned integer and return the result.

## Examples
**Example 1**
- Input: `n = 00000010100101000001111010011100`
- Output: `00111001011110000010100101000000` (decimal `964176192`)

**Example 2**
- Input: `n = 11111111111111111111111111111101`
- Output: `10111111111111111111111111111111` (decimal `3221225471`)

## Constraints
- The input is a 32-bit integer.

**Follow-up:** If this is called many times, how would you optimize it?
""",
    "missing-number": r"""## Problem
Given an array `nums` containing `n` distinct numbers drawn from the range `[0, n]`,
return the single number in that range that is missing from the array.

## Examples
**Example 1**
- Input: `nums = [3, 0, 1]`
- Output: `2`

**Example 2**
- Input: `nums = [0, 1]`
- Output: `2`

**Example 3**
- Input: `nums = [9,6,4,2,3,5,7,0,1]`
- Output: `8`

## Constraints
- `n == nums.length`, `1 <= n <= 10^4`
- `0 <= nums[i] <= n`, all values distinct.

**Follow-up:** Can you do it in `O(n)` time and `O(1)` extra space?
""",
    "sum-of-two-integers": r"""## Problem
Given two integers `a` and `b`, return their sum **without** using the `+` or `-`
operators (use bitwise operations instead).

## Examples
**Example 1**
- Input: `a = 1`, `b = 2`
- Output: `3`

**Example 2**
- Input: `a = 2`, `b = 3`
- Output: `5`

## Constraints
- `-1000 <= a, b <= 1000`
""",
    "reverse-integer": r"""## Problem
Given a signed 32-bit integer `x`, return `x` with its digits reversed. If reversing
causes the value to fall outside the 32-bit signed range `[-2^31, 2^31 - 1]`, return
`0`. Assume the environment does not allow 64-bit integers.

## Examples
**Example 1**
- Input: `x = 123`
- Output: `321`

**Example 2**
- Input: `x = -123`
- Output: `-321`

**Example 3**
- Input: `x = 120`
- Output: `21`

## Constraints
- `-2^31 <= x <= 2^31 - 1`
""",
}


def build(force=False):
    with open(INDEX) as f:
        index = json.load(f)
    by_id = {p["id"]: p for p in index}

    written, skipped, missing = [], [], []
    for pid, body in STATEMENTS.items():
        if pid not in by_id:
            missing.append(pid)
            continue
        p = by_id[pid]
        path = os.path.join(ROOT, p["statementFile"])
        if os.path.exists(path) and not force:
            skipped.append(p["statementFile"])
            continue
        header = (
            f"# {p['title']}\n\n"
            f"- **Category:** {p['category']} · **Difficulty:** {p['difficulty']}\n"
            f"- **LeetCode:** {p['leetcodeUrl']}\n"
            f"- **Patterns:** {', '.join(p['patterns'])}\n\n"
        )
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(header + body.strip() + "\n")
        written.append(p["statementFile"])

    # Report any index problems we have no body for.
    have = set(STATEMENTS) | {os.path.splitext(os.path.basename(p["statementFile"]))[0]
                              for p in index if os.path.exists(os.path.join(ROOT, p["statementFile"]))}
    no_body = [p["id"] for p in index if p["id"] not in STATEMENTS
               and not os.path.exists(os.path.join(ROOT, p["statementFile"]))]

    print(f"wrote {len(written)}, skipped {len(skipped)} existing")
    if missing:
        print(f"WARNING: ids not in index: {missing}")
    if no_body:
        print(f"WARNING: index problems with no statement: {no_body}")


if __name__ == "__main__":
    build(force="--force" in sys.argv)
