# 406. Queue Reconstruction by Height

**Difficulty:** Medium | **Category:** Stack/Queue  
**Link:** [https://leetcode.com/problems/queue-reconstruction-by-height/](https://leetcode.com/problems/queue-reconstruction-by-height/)

## Problem Statement

Solve the 'Queue Reconstruction by Height' problem using stack/queue techniques.

## Key Insight

Identify the core stack/queue pattern and apply it efficiently. Consider edge cases and optimize from brute force.

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

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply stack/queue technique for optimal solution.

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
