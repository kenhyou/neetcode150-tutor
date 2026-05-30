#!/usr/bin/env python3
"""One-shot generator for data/neetcode150.json.

Kept in the repo so the canonical index can be regenerated/extended. Each tuple is
(title, leetcode_slug, difficulty, [patterns]). Category order follows the official
NeetCode 150 roadmap.
"""
import json
import os
import re

ROADMAP = [
    ("Arrays & Hashing", [
        ("Contains Duplicate", "contains-duplicate", "Easy", ["Hash Set"]),
        ("Valid Anagram", "valid-anagram", "Easy", ["Hash Map", "Counting"]),
        ("Two Sum", "two-sum", "Easy", ["Hash Map"]),
        ("Group Anagrams", "group-anagrams", "Medium", ["Hash Map"]),
        ("Top K Frequent Elements", "top-k-frequent-elements", "Medium", ["Bucket Sort", "Heap"]),
        ("Encode and Decode Strings", "encode-and-decode-strings", "Medium", ["Design", "String"]),
        ("Product of Array Except Self", "product-of-array-except-self", "Medium", ["Prefix/Suffix"]),
        ("Valid Sudoku", "valid-sudoku", "Medium", ["Hash Set", "Matrix"]),
        ("Longest Consecutive Sequence", "longest-consecutive-sequence", "Medium", ["Hash Set"]),
    ]),
    ("Two Pointers", [
        ("Valid Palindrome", "valid-palindrome", "Easy", ["Two Pointers"]),
        ("Two Sum II - Input Array Is Sorted", "two-sum-ii-input-array-is-sorted", "Medium", ["Two Pointers"]),
        ("3Sum", "3sum", "Medium", ["Two Pointers", "Sorting"]),
        ("Container With Most Water", "container-with-most-water", "Medium", ["Two Pointers", "Greedy"]),
        ("Trapping Rain Water", "trapping-rain-water", "Hard", ["Two Pointers", "Monotonic Stack"]),
    ]),
    ("Sliding Window", [
        ("Best Time to Buy and Sell Stock", "best-time-to-buy-and-sell-stock", "Easy", ["Sliding Window"]),
        ("Longest Substring Without Repeating Characters", "longest-substring-without-repeating-characters", "Medium", ["Sliding Window", "Hash Set"]),
        ("Longest Repeating Character Replacement", "longest-repeating-character-replacement", "Medium", ["Sliding Window"]),
        ("Permutation in String", "permutation-in-string", "Medium", ["Sliding Window"]),
        ("Minimum Window Substring", "minimum-window-substring", "Hard", ["Sliding Window"]),
        ("Sliding Window Maximum", "sliding-window-maximum", "Hard", ["Monotonic Deque"]),
    ]),
    ("Stack", [
        ("Valid Parentheses", "valid-parentheses", "Easy", ["Stack"]),
        ("Min Stack", "min-stack", "Medium", ["Stack", "Design"]),
        ("Evaluate Reverse Polish Notation", "evaluate-reverse-polish-notation", "Medium", ["Stack"]),
        ("Generate Parentheses", "generate-parentheses", "Medium", ["Backtracking", "Stack"]),
        ("Daily Temperatures", "daily-temperatures", "Medium", ["Monotonic Stack"]),
        ("Car Fleet", "car-fleet", "Medium", ["Stack", "Sorting"]),
        ("Largest Rectangle in Histogram", "largest-rectangle-in-histogram", "Hard", ["Monotonic Stack"]),
    ]),
    ("Binary Search", [
        ("Binary Search", "binary-search", "Easy", ["Binary Search"]),
        ("Search a 2D Matrix", "search-a-2d-matrix", "Medium", ["Binary Search", "Matrix"]),
        ("Koko Eating Bananas", "koko-eating-bananas", "Medium", ["Binary Search on Answer"]),
        ("Find Minimum in Rotated Sorted Array", "find-minimum-in-rotated-sorted-array", "Medium", ["Binary Search"]),
        ("Search in Rotated Sorted Array", "search-in-rotated-sorted-array", "Medium", ["Binary Search"]),
        ("Time Based Key-Value Store", "time-based-key-value-store", "Medium", ["Binary Search", "Design"]),
        ("Median of Two Sorted Arrays", "median-of-two-sorted-arrays", "Hard", ["Binary Search"]),
    ]),
    ("Linked List", [
        ("Reverse Linked List", "reverse-linked-list", "Easy", ["Linked List"]),
        ("Merge Two Sorted Lists", "merge-two-sorted-lists", "Easy", ["Linked List"]),
        ("Reorder List", "reorder-list", "Medium", ["Linked List", "Two Pointers"]),
        ("Remove Nth Node From End of List", "remove-nth-node-from-end-of-list", "Medium", ["Two Pointers"]),
        ("Copy List with Random Pointer", "copy-list-with-random-pointer", "Medium", ["Hash Map", "Linked List"]),
        ("Add Two Numbers", "add-two-numbers", "Medium", ["Linked List", "Math"]),
        ("Linked List Cycle", "linked-list-cycle", "Easy", ["Fast & Slow Pointers"]),
        ("Find the Duplicate Number", "find-the-duplicate-number", "Medium", ["Fast & Slow Pointers"]),
        ("LRU Cache", "lru-cache", "Medium", ["Hash Map", "Linked List", "Design"]),
        ("Merge k Sorted Lists", "merge-k-sorted-lists", "Hard", ["Heap", "Linked List"]),
        ("Reverse Nodes in k-Group", "reverse-nodes-in-k-group", "Hard", ["Linked List"]),
    ]),
    ("Trees", [
        ("Invert Binary Tree", "invert-binary-tree", "Easy", ["DFS", "Tree"]),
        ("Maximum Depth of Binary Tree", "maximum-depth-of-binary-tree", "Easy", ["DFS", "BFS"]),
        ("Diameter of Binary Tree", "diameter-of-binary-tree", "Easy", ["DFS"]),
        ("Balanced Binary Tree", "balanced-binary-tree", "Easy", ["DFS"]),
        ("Same Tree", "same-tree", "Easy", ["DFS"]),
        ("Subtree of Another Tree", "subtree-of-another-tree", "Easy", ["DFS"]),
        ("Lowest Common Ancestor of a Binary Search Tree", "lowest-common-ancestor-of-a-binary-search-tree", "Medium", ["BST"]),
        ("Binary Tree Level Order Traversal", "binary-tree-level-order-traversal", "Medium", ["BFS"]),
        ("Binary Tree Right Side View", "binary-tree-right-side-view", "Medium", ["BFS"]),
        ("Count Good Nodes in Binary Tree", "count-good-nodes-in-binary-tree", "Medium", ["DFS"]),
        ("Validate Binary Search Tree", "validate-binary-search-tree", "Medium", ["BST", "DFS"]),
        ("Kth Smallest Element in a BST", "kth-smallest-element-in-a-bst", "Medium", ["BST", "Inorder"]),
        ("Construct Binary Tree from Preorder and Inorder Traversal", "construct-binary-tree-from-preorder-and-inorder-traversal", "Medium", ["DFS", "Divide & Conquer"]),
        ("Binary Tree Maximum Path Sum", "binary-tree-maximum-path-sum", "Hard", ["DFS"]),
        ("Serialize and Deserialize Binary Tree", "serialize-and-deserialize-binary-tree", "Hard", ["BFS", "DFS", "Design"]),
    ]),
    ("Tries", [
        ("Implement Trie (Prefix Tree)", "implement-trie-prefix-tree", "Medium", ["Trie", "Design"]),
        ("Design Add and Search Words Data Structure", "design-add-and-search-words-data-structure", "Medium", ["Trie", "DFS", "Design"]),
        ("Word Search II", "word-search-ii", "Hard", ["Trie", "Backtracking"]),
    ]),
    ("Heap / Priority Queue", [
        ("Kth Largest Element in a Stream", "kth-largest-element-in-a-stream", "Easy", ["Heap", "Design"]),
        ("Last Stone Weight", "last-stone-weight", "Easy", ["Heap"]),
        ("K Closest Points to Origin", "k-closest-points-to-origin", "Medium", ["Heap"]),
        ("Kth Largest Element in an Array", "kth-largest-element-in-an-array", "Medium", ["Heap", "Quickselect"]),
        ("Task Scheduler", "task-scheduler", "Medium", ["Heap", "Greedy"]),
        ("Design Twitter", "design-twitter", "Medium", ["Heap", "Design"]),
        ("Find Median from Data Stream", "find-median-from-data-stream", "Hard", ["Two Heaps", "Design"]),
    ]),
    ("Backtracking", [
        ("Subsets", "subsets", "Medium", ["Backtracking"]),
        ("Combination Sum", "combination-sum", "Medium", ["Backtracking"]),
        ("Permutations", "permutations", "Medium", ["Backtracking"]),
        ("Subsets II", "subsets-ii", "Medium", ["Backtracking"]),
        ("Combination Sum II", "combination-sum-ii", "Medium", ["Backtracking"]),
        ("Word Search", "word-search", "Medium", ["Backtracking", "DFS", "Matrix"]),
        ("Palindrome Partitioning", "palindrome-partitioning", "Medium", ["Backtracking"]),
        ("Letter Combinations of a Phone Number", "letter-combinations-of-a-phone-number", "Medium", ["Backtracking"]),
        ("N-Queens", "n-queens", "Hard", ["Backtracking"]),
    ]),
    ("Graphs", [
        ("Number of Islands", "number-of-islands", "Medium", ["DFS", "BFS", "Union Find"]),
        ("Clone Graph", "clone-graph", "Medium", ["DFS", "BFS", "Hash Map"]),
        ("Max Area of Island", "max-area-of-island", "Medium", ["DFS", "BFS"]),
        ("Pacific Atlantic Water Flow", "pacific-atlantic-water-flow", "Medium", ["DFS", "BFS"]),
        ("Surrounded Regions", "surrounded-regions", "Medium", ["DFS", "BFS"]),
        ("Rotting Oranges", "rotting-oranges", "Medium", ["BFS"]),
        ("Walls and Gates", "walls-and-gates", "Medium", ["BFS"]),
        ("Course Schedule", "course-schedule", "Medium", ["Topological Sort", "DFS"]),
        ("Course Schedule II", "course-schedule-ii", "Medium", ["Topological Sort"]),
        ("Redundant Connection", "redundant-connection", "Medium", ["Union Find"]),
        ("Number of Connected Components in an Undirected Graph", "number-of-connected-components-in-an-undirected-graph", "Medium", ["Union Find", "DFS"]),
        ("Graph Valid Tree", "graph-valid-tree", "Medium", ["Union Find", "DFS"]),
        ("Word Ladder", "word-ladder", "Hard", ["BFS"]),
    ]),
    ("Advanced Graphs", [
        ("Reconstruct Itinerary", "reconstruct-itinerary", "Hard", ["Eulerian Path", "DFS"]),
        ("Min Cost to Connect All Points", "min-cost-to-connect-all-points", "Medium", ["MST", "Prim"]),
        ("Network Delay Time", "network-delay-time", "Medium", ["Dijkstra"]),
        ("Swim in Rising Water", "swim-in-rising-water", "Hard", ["Dijkstra", "Binary Search"]),
        ("Alien Dictionary", "alien-dictionary", "Hard", ["Topological Sort"]),
        ("Cheapest Flights Within K Stops", "cheapest-flights-within-k-stops", "Medium", ["Bellman-Ford", "BFS"]),
    ]),
    ("1-D Dynamic Programming", [
        ("Climbing Stairs", "climbing-stairs", "Easy", ["DP"]),
        ("Min Cost Climbing Stairs", "min-cost-climbing-stairs", "Easy", ["DP"]),
        ("House Robber", "house-robber", "Medium", ["DP"]),
        ("House Robber II", "house-robber-ii", "Medium", ["DP"]),
        ("Longest Palindromic Substring", "longest-palindromic-substring", "Medium", ["DP", "Expand Center"]),
        ("Palindromic Substrings", "palindromic-substrings", "Medium", ["DP", "Expand Center"]),
        ("Decode Ways", "decode-ways", "Medium", ["DP"]),
        ("Coin Change", "coin-change", "Medium", ["DP"]),
        ("Maximum Product Subarray", "maximum-product-subarray", "Medium", ["DP"]),
        ("Word Break", "word-break", "Medium", ["DP"]),
        ("Longest Increasing Subsequence", "longest-increasing-subsequence", "Medium", ["DP", "Binary Search"]),
        ("Partition Equal Subset Sum", "partition-equal-subset-sum", "Medium", ["DP", "0/1 Knapsack"]),
    ]),
    ("2-D Dynamic Programming", [
        ("Unique Paths", "unique-paths", "Medium", ["DP"]),
        ("Longest Common Subsequence", "longest-common-subsequence", "Medium", ["DP"]),
        ("Best Time to Buy and Sell Stock with Cooldown", "best-time-to-buy-and-sell-stock-with-cooldown", "Medium", ["DP", "State Machine"]),
        ("Coin Change II", "coin-change-ii", "Medium", ["DP", "Unbounded Knapsack"]),
        ("Target Sum", "target-sum", "Medium", ["DP"]),
        ("Interleaving String", "interleaving-string", "Medium", ["DP"]),
        ("Longest Increasing Path in a Matrix", "longest-increasing-path-in-a-matrix", "Hard", ["DP", "DFS", "Memoization"]),
        ("Distinct Subsequences", "distinct-subsequences", "Hard", ["DP"]),
        ("Edit Distance", "edit-distance", "Medium", ["DP"]),
        ("Burst Balloons", "burst-balloons", "Hard", ["DP", "Interval DP"]),
        ("Regular Expression Matching", "regular-expression-matching", "Hard", ["DP"]),
    ]),
    ("Greedy", [
        ("Maximum Subarray", "maximum-subarray", "Medium", ["Greedy", "Kadane"]),
        ("Jump Game", "jump-game", "Medium", ["Greedy"]),
        ("Jump Game II", "jump-game-ii", "Medium", ["Greedy", "BFS"]),
        ("Gas Station", "gas-station", "Medium", ["Greedy"]),
        ("Hand of Straights", "hand-of-straights", "Medium", ["Greedy", "Heap"]),
        ("Merge Triplets to Form Target Triplet", "merge-triplets-to-form-target-triplet", "Medium", ["Greedy"]),
        ("Partition Labels", "partition-labels", "Medium", ["Greedy", "Two Pointers"]),
        ("Valid Parenthesis String", "valid-parenthesis-string", "Medium", ["Greedy", "DP"]),
    ]),
    ("Intervals", [
        ("Insert Interval", "insert-interval", "Medium", ["Intervals"]),
        ("Merge Intervals", "merge-intervals", "Medium", ["Intervals", "Sorting"]),
        ("Non-overlapping Intervals", "non-overlapping-intervals", "Medium", ["Intervals", "Greedy"]),
        ("Meeting Rooms", "meeting-rooms", "Easy", ["Intervals", "Sorting"]),
        ("Meeting Rooms II", "meeting-rooms-ii", "Medium", ["Intervals", "Heap"]),
        ("Minimum Interval to Include Each Query", "minimum-interval-to-include-each-query", "Hard", ["Intervals", "Heap"]),
    ]),
    ("Math & Geometry", [
        ("Rotate Image", "rotate-image", "Medium", ["Matrix"]),
        ("Spiral Matrix", "spiral-matrix", "Medium", ["Matrix"]),
        ("Set Matrix Zeroes", "set-matrix-zeroes", "Medium", ["Matrix"]),
        ("Happy Number", "happy-number", "Easy", ["Math", "Fast & Slow Pointers"]),
        ("Plus One", "plus-one", "Easy", ["Math", "Array"]),
        ("Pow(x, n)", "powx-n", "Medium", ["Math", "Fast Exponentiation"]),
        ("Multiply Strings", "multiply-strings", "Medium", ["Math", "String"]),
        ("Detect Squares", "detect-squares", "Medium", ["Hash Map", "Design"]),
    ]),
    ("Bit Manipulation", [
        ("Single Number", "single-number", "Easy", ["XOR"]),
        ("Number of 1 Bits", "number-of-1-bits", "Easy", ["Bit Manipulation"]),
        ("Counting Bits", "counting-bits", "Easy", ["Bit Manipulation", "DP"]),
        ("Reverse Bits", "reverse-bits", "Easy", ["Bit Manipulation"]),
        ("Missing Number", "missing-number", "Easy", ["XOR", "Math"]),
        ("Sum of Two Integers", "sum-of-two-integers", "Medium", ["Bit Manipulation"]),
        ("Reverse Integer", "reverse-integer", "Medium", ["Math"]),
    ]),
]


def cat_slug(name):
    s = name.lower()
    s = s.replace("&", "and").replace("/", " ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


problems = []
for cat_order, (category, items) in enumerate(ROADMAP, start=1):
    cslug = cat_slug(category)
    for order, (title, slug, difficulty, patterns) in enumerate(items, start=1):
        problems.append({
            "id": slug,
            "title": title,
            "category": category,
            "categorySlug": cslug,
            "categoryOrder": cat_order,
            "order": order,
            "difficulty": difficulty,
            "leetcodeUrl": f"https://leetcode.com/problems/{slug}/",
            "statementFile": f"problems/{cslug}/{slug}.md",
            "patterns": patterns,
        })

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.join(here, "neetcode150.json")
with open(out, "w") as f:
    json.dump(problems, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"Wrote {len(problems)} problems to {out}")
assert len(problems) == 150, f"expected 150, got {len(problems)}"
