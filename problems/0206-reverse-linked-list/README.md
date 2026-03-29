# 206. Reverse Linked List

**Difficulty:** Easy | **Category:** Linked List  
**Link:** [https://leetcode.com/problems/reverse-linked-list/](https://leetcode.com/problems/reverse-linked-list/)

## Problem Statement

Reverse a singly linked list.

## Key Insight

Use three pointers (prev, curr, next) to reverse links one at a time. Each node points to its predecessor instead of successor.

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

Store all values, create new reversed list. O(n) time, O(n) space.

### Optimal

In-place pointer reversal. O(n) time, O(1) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Don't lose reference to next node before reassigning
- Handle empty list and single node
- Return prev, not curr (curr is null at end)

## Related Problems

- [92. Reverse Linked List II](../0092-reverse-linked-list-ii)
- [234. Palindrome Linked List](../0234-palindrome-linked-list)
- [25. Reverse Nodes in k-Group](../0025-reverse-nodes-in-k-group)

## Interview Tips

- Can you do it recursively?
- What about reversing a portion of the list?
- How would you detect if a list is a palindrome using reversal?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
