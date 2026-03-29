# 1. Two Sum

**Difficulty:** Easy | **Category:** Hash Table  
**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem Statement

Given an array of integers and a target, return indices of two numbers that add up to target.

## Key Insight

For each number, its complement (target - num) is what you need. A hash map lets you check if the complement exists in O(1).

## Pattern: Hash Table

Use a hash map/set to achieve O(1) lookups, enabling you to trade space for time. Store previously seen values and check for complements or duplicates in constant time.

### When to Use This Pattern

- You need O(1) lookup for previously seen elements
- Finding pairs/groups that satisfy a condition (e.g., two sum, anagrams)
- Counting frequencies of elements
- Detecting duplicates
- Mapping relationships between elements

### When NOT to Use This Pattern

- Data is already sorted — binary search is more space-efficient
- You need ordered traversal — use a BST or sorted array instead
- Memory is extremely constrained — hash maps have overhead
- The key space is small and bounded — a simple array works better

### Alternatives to Consider

- Sorting + two pointers: O(n log n) time, O(1) space — better when space matters
- Binary search: works when data is sorted, O(log n) per lookup
- Bit manipulation: for specific problems like finding single numbers

## Approach

### Brute Force

Check all pairs with two nested loops. O(n^2) time, O(1) space.

### Optimal

One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Don't use the same element twice
- Handle case where complement equals the number itself
- Return indices, not values

## Related Problems

- [15. 3Sum](../0015-3sum)
- [167. Two Sum II - Input array is sorted](../0167-two-sum-ii-input-array-is-sorted)

## Interview Tips

- What if the array is sorted? (Two pointers)
- What if you need all pairs? (Two pointers or hash set)
- What about duplicates?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
