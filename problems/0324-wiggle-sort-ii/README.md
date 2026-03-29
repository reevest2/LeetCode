# 324. Wiggle Sort II

**Difficulty:** Medium | **Category:** Sorting  
**Link:** [https://leetcode.com/problems/wiggle-sort-ii/](https://leetcode.com/problems/wiggle-sort-ii/)

## Problem Statement

Solve the 'Wiggle Sort II' problem using sorting techniques.

## Key Insight

Identify the core sorting pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Sorting

Sort data to enable binary search, two-pointer techniques, or to group related elements together. Sorting often simplifies complex problems at the cost of O(n log n) time.

### When to Use This Pattern

- Problem becomes easier with ordered data
- Need to find pairs/triplets (sort + two pointers)
- Grouping identical/similar elements
- Merge intervals or overlapping ranges
- When O(n log n) is acceptable

### When NOT to Use This Pattern

- Order of original elements matters (indices needed)
- Data is already sorted or nearly sorted — exploit that directly
- O(n) solution exists via hash table or counting sort
- Streaming data that can't be stored fully

### Alternatives to Consider

- Hash table: O(n) for grouping/counting without sorting
- Counting sort: O(n+k) when value range is bounded
- Bucket sort: O(n) average for uniformly distributed data
- Heap: when you only need the top-k elements

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply sorting technique for optimal solution.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Consider edge cases carefully
- Check for off-by-one errors
- Handle empty or minimal inputs

## Interview Tips

- Explain your thought process before coding
- Start with brute force, then optimize
- Discuss time and space complexity

## My Notes

<!-- Write your own notes, observations, and learnings here -->
