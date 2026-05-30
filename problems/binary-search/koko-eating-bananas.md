# Koko Eating Bananas

- **Category:** Binary Search · **Difficulty:** Medium
- **LeetCode:** https://leetcode.com/problems/koko-eating-bananas/
- **Patterns:** Binary Search on Answer

## Problem
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
