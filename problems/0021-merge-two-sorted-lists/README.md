# 21. Merge Two Sorted Lists

**Difficulty:** Easy | **Category:** Sorting  
**Link:** [https://leetcode.com/problems/merge-two-sorted-lists/](https://leetcode.com/problems/merge-two-sorted-lists/)

## Problem Statement

Merge two sorted linked lists into one sorted linked list.

## Key Insight

Use a dummy head node and compare current nodes from both lists, appending the smaller one. Don't forget to attach the remaining list.

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

Collect all values, sort, create new list. O((m+n) log(m+n)).

### Optimal

Two-pointer merge. O(m+n) time, O(1) space (iterative).

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Handle one or both lists being empty
- Don't forget to link the remaining list
- Recursive solution can stack overflow on very long lists

## Related Problems

- [23. Merge k Sorted Lists](../0023-merge-k-sorted-lists)
- [88. Merge Sorted Array](../0088-merge-sorted-array)
- [148. Sort List](../0148-sort-list)

## Interview Tips

- Iterative vs recursive?
- What if you had K sorted lists? (Heap or divide and conquer)

## My Notes

<!-- Write your own notes, observations, and learnings here -->
