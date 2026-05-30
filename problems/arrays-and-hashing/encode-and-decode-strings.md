# Encode and Decode Strings

- **Category:** Arrays & Hashing · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/encode-and-decode-strings/ (premium)
- **Patterns:** Design, String

## Problem
Design an algorithm to serialize a list of strings into a single string, and then
deserialize that single string back into the original list. Implement two functions:

- `encode(strs)` → returns one string encoding the whole list.
- `decode(s)` → returns the original list of strings.

Your encoding must survive any possible characters in the input strings (including
delimiters, digits, and empty strings).

## Examples
**Example 1**
- Input: `["neet", "code", "love", "you"]`
- After `encode` then `decode`: `["neet", "code", "love", "you"]`

**Example 2**
- Input: `["we", "say", ":", "yes"]`
- After `encode` then `decode`: `["we", "say", ":", "yes"]`

## Constraints
- `0 <= strs.length < 100`
- `0 <= strs[i].length < 200`
- `strs[i]` may contain any ASCII characters.

**Hint to keep in mind:** a naive single-character separator won't work, because that
character can appear inside a string. Think length-prefixing.
