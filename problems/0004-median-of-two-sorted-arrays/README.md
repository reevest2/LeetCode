# 4. Median of Two Sorted Arrays

**Difficulty:** Hard | **Category:** Array, Sorting, Heap  
**Link:** [https://leetcode.com/problems/median-of-two-sorted-arrays/](https://leetcode.com/problems/median-of-two-sorted-arrays/)

## Problem Statement

Find the median of two sorted arrays in O(log(m+n)) time.

## Key Insight

Binary search on the smaller array to find the correct partition point where all left elements <= all right elements.

## Pattern: Array

Direct array manipulation using indices, iteration, and in-place modifications. Many array problems use two pointers, sliding window, or prefix sums as sub-patterns.

### When to Use This Pattern

- Problems involving contiguous elements or subarrays
- In-place modifications to save space
- When element positions/indices matter
- Prefix sum problems (range sum queries)

### When NOT to Use This Pattern

- Frequent insertions/deletions in the middle — use linked list
- Need O(1) lookup by value — use hash table
- Data has hierarchical structure — use tree

### Alternatives to Consider

- Hash table: when you need value-based lookups
- Linked list: when you need frequent insertions/deletions
- Deque: when you need efficient operations at both ends

## Approach

### Brute Force

Merge both arrays and find median. O(m+n) time.

### Optimal

Binary search on partition. O(log(min(m,n))) time, O(1) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Always binary search on the smaller array
- Handle odd vs even total length
- Edge partitions (empty left or right)

## Related Problems

- [295. Find Median from Data Stream](../0295-find-median-from-data-stream)
- [480. Sliding Window Median](../0480-sliding-window-median)

## Interview Tips

- Why not merge and find? (O(m+n) violates requirement)
- Can you generalize to find k-th element?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
