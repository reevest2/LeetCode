# 20. Valid Parentheses

**Difficulty:** Easy | **Category:** Stack/Queue  
**Link:** [https://leetcode.com/problems/valid-parentheses/](https://leetcode.com/problems/valid-parentheses/)

## Problem Statement

Determine if a string of brackets is valid (properly opened and closed in order).

## Key Insight

Use a stack: push opening brackets, pop and match when you see closing brackets. Valid if stack is empty at the end.

## Pattern: Stack/Queue

LIFO (stack) or FIFO (queue) processing. Stacks handle matching/nesting (parentheses, expression evaluation). Monotonic stacks find next greater/smaller elements in O(n).

### When to Use This Pattern

- Matching brackets, parentheses, or nested structures
- Expression evaluation or parsing
- Next greater/smaller element (monotonic stack)
- BFS traversal (queue)
- Undo/redo operations
- DFS without recursion

### When NOT to Use This Pattern

- Need random access to middle elements
- Need to search for arbitrary values
- Problem doesn't have LIFO/FIFO ordering requirement

### Alternatives to Consider

- Recursion: implicit stack, sometimes cleaner for DFS/backtracking
- Deque: when you need both stack and queue operations
- Priority queue: when processing order is by priority, not insertion order

## Approach

### Brute Force

Repeatedly remove matching pairs until none remain. O(n^2) time.

### Optimal

Stack-based matching. O(n) time, O(n) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Check stack is not empty before popping
- String with only opening brackets is invalid
- Odd-length strings are always invalid

## Related Problems

- [22. Generate Parentheses](../0022-generate-parentheses)
- [32. Longest Valid Parentheses](../0032-longest-valid-parentheses)
- [301. Remove Invalid Parentheses](../0301-remove-invalid-parentheses)

## Interview Tips

- What if we only had one type of bracket?
- How would you handle wildcard characters?
- Can you do it without a stack? (Only for single bracket type)

## My Notes

<!-- Write your own notes, observations, and learnings here -->
