# 378. Kth Smallest Element in a Sorted Matrix

**Difficulty:** Medium | **Category:** Array, Sorting, Heap  
**Link:** [https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/)

## Problem Statement

Solve the 'Kth Smallest Element in a Sorted Matrix' problem using array techniques.

## Key Insight

Identify the core array pattern and apply it efficiently. Consider edge cases and optimize from brute force.

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

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply array technique for optimal solution.

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
