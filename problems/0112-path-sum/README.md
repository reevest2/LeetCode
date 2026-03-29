# 112. Path Sum

**Difficulty:** Easy | **Category:** DP  
**Link:** [https://leetcode.com/problems/path-sum/](https://leetcode.com/problems/path-sum/)

## Problem Statement

Solve the 'Path Sum' problem using dp techniques.

## Key Insight

Identify the core dp pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: DP

Break problems into overlapping subproblems and store results to avoid recomputation. Key: identify the state, the transition (recurrence), and base cases. Top-down (memoization) vs bottom-up (tabulation).

### When to Use This Pattern

- Problem has optimal substructure (optimal solution uses optimal sub-solutions)
- Overlapping subproblems (same subproblems solved multiple times)
- Counting problems (number of ways, paths, combinations)
- Optimization problems (min cost, max profit, longest/shortest)
- String matching and sequence alignment

### When NOT to Use This Pattern

- Subproblems don't overlap — divide and conquer is simpler
- Greedy choice property holds — greedy is simpler and faster
- State space is too large to memoize
- Problem requires the actual path, not just the optimal value (may need backtracking)

### Alternatives to Consider

- Greedy: when locally optimal choices lead to global optimum
- Divide and conquer: when subproblems don't overlap
- BFS/DFS: for shortest path or reachability problems
- Math formula: some counting problems have closed-form solutions

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply dp technique for optimal solution.

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
