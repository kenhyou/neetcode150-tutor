# Design Add and Search Words Data Structure

- **Category:** Tries · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/design-add-and-search-words-data-structure/
- **Patterns:** Trie, DFS, Design

## Problem
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
