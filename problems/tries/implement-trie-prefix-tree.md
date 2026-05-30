# Implement Trie (Prefix Tree)

- **Category:** Tries · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/implement-trie-prefix-tree/
- **Patterns:** Trie, Design

## Problem
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
