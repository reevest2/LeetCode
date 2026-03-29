# 347. Top K Frequent Elements

**Difficulty:** Medium | **Category:** Heap  
**Link:** [https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

## Problem Statement

Solve the 'Top K Frequent Elements' problem using heap techniques.

## Key Insight

Identify the core heap pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Heap

Maintain a dynamic collection where you efficiently access the min or max element. Priority queues use heaps internally. Key operations: insert O(log n), extract-min/max O(log n), peek O(1).

### When to Use This Pattern

- Need repeated access to min/max element
- Top-K problems (k-th largest, k most frequent)
- Merge K sorted lists/streams
- Median maintenance (two heaps)
- Dijkstra's shortest path
- Task scheduling by priority

### When NOT to Use This Pattern

- Need to search for arbitrary elements — use BST or hash table
- Only need min/max once — just scan the array
- Data is static — sort once instead

### Alternatives to Consider

- Sorting: when all data is available upfront
- Quickselect: O(n) average for k-th element (one-time)
- BST/balanced BST: when you need both min/max and search
- Bucket sort: for top-K with bounded value range

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply heap technique for optimal solution.

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
