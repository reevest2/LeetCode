# 46. Permutations

**Difficulty:** Medium | **Category:** Backtracking  
**Link:** [https://leetcode.com/problems/permutations/](https://leetcode.com/problems/permutations/)

## Problem Statement

Solve the 'Permutations' problem using backtracking techniques.

## Key Insight

Identify the core backtracking pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Backtracking

Systematically explore all possible solutions by building candidates incrementally and abandoning ('pruning') paths that can't lead to valid solutions. Think of it as DFS on a decision tree.

### When to Use This Pattern

- Generate all combinations, permutations, or subsets
- Constraint satisfaction (N-Queens, Sudoku)
- Problems that say 'find all' or 'list all valid'
- Decision problems with complex constraints

### When NOT to Use This Pattern

- Only need count, not enumeration — DP is faster
- Greedy approach works (no need to explore all paths)
- Problem has polynomial-time solution — backtracking is exponential

### Alternatives to Consider

- DP: when you only need the count or optimal value
- BFS: for shortest path in unweighted graphs
- Greedy: when local choices guarantee global optimum
- Bit manipulation: for subset enumeration with small sets

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply backtracking technique for optimal solution.

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
