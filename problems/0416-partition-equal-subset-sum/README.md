# 416. Partition Equal Subset Sum

**Difficulty:** Medium | **Category:** Hash Table, Backtracking  
**Link:** [https://leetcode.com/problems/partition-equal-subset-sum/](https://leetcode.com/problems/partition-equal-subset-sum/)

## Problem Statement

Solve the 'Partition Equal Subset Sum' problem using hash table techniques.

## Key Insight

Identify the core hash table pattern and apply it efficiently. Consider edge cases and optimize from brute force.

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

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply hash table technique for optimal solution.

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
