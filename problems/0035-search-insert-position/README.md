# 35. Search Insert Position

**Difficulty:** Easy | **Category:** Binary Search  
**Link:** [https://leetcode.com/problems/search-insert-position/](https://leetcode.com/problems/search-insert-position/)

## Problem Statement

Solve the 'Search Insert Position' problem using binary search techniques.

## Key Insight

Identify the core binary search pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Binary Search

Divide the search space in half each step to find a target or boundary in O(log n). Works on sorted arrays or any monotonic search space (answer-based binary search).

### When to Use This Pattern

- Sorted array and need to find a value or insertion point
- Search space is monotonic (if f(x) is true, f(x+1) is true)
- Minimize/maximize a value subject to a feasibility check
- Finding boundaries (first/last occurrence)

### When NOT to Use This Pattern

- Data is unsorted and sorting isn't worth it
- Search space isn't monotonic
- Array is very small — linear scan is simpler
- Need to find all matches, not just one

### Alternatives to Consider

- Linear scan: simpler for small inputs or unsorted data
- Hash table: O(1) lookup when you need exact match
- Two pointers: for pair-finding in sorted arrays

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply binary search technique for optimal solution.

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
