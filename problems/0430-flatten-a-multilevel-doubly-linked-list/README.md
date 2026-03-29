# 430. Flatten a Multilevel Doubly Linked List

**Difficulty:** Medium | **Category:** Linked List  
**Link:** [https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)

## Problem Statement

Solve the 'Flatten a Multilevel Doubly Linked List' problem using linked list techniques.

## Key Insight

Identify the core linked list pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Linked List

Manipulate nodes with next pointers. Key techniques: fast/slow pointers (Floyd's), dummy head nodes, and pointer reversal. Think about edge cases: empty list, single node, cycles.

### When to Use This Pattern

- Frequent insertions/deletions at arbitrary positions
- Don't need random access by index
- Implementing queues, stacks, or LRU caches
- Detecting cycles (Floyd's algorithm)

### When NOT to Use This Pattern

- Need random access by index — use array
- Need efficient search — use hash table or BST
- Memory locality matters — arrays are cache-friendly

### Alternatives to Consider

- Array/dynamic array: better cache performance, random access
- Deque: double-ended operations without manual pointer management
- Skip list: adds O(log n) search to linked list structure

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply linked list technique for optimal solution.

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
