# Word Ladder

- **Category:** Graphs · **Difficulty:** Hard
- **LeetCode:** https://leetcode.com/problems/word-ladder/
- **Patterns:** BFS

## Problem
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
