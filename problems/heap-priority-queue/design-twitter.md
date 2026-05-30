# Design Twitter

- **Category:** Heap / Priority Queue · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/design-twitter/
- **Patterns:** Heap, Design

## Problem
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
