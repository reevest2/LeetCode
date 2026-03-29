# 134. Gas Station

**Difficulty:** Medium | **Category:** Greedy  
**Link:** [https://leetcode.com/problems/gas-station/](https://leetcode.com/problems/gas-station/)

## Problem Statement

Solve the 'Gas Station' problem using greedy techniques.

## Key Insight

Identify the core greedy pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Greedy

Make the locally optimal choice at each step, hoping to find the global optimum. Only works when the greedy choice property holds — proving correctness is key.

### When to Use This Pattern

- Interval scheduling (earliest deadline, fewest conflicts)
- Huffman coding and similar optimization
- Problems where sorting + greedy selection works
- When you can prove local optimum leads to global optimum

### When NOT to Use This Pattern

- Problem has overlapping subproblems — use DP
- Greedy choice can be shown to fail with counterexample
- Need to explore multiple paths — use backtracking

### Alternatives to Consider

- DP: guarantees optimal solution when greedy doesn't work
- Backtracking: explores all possibilities
- Binary search on answer: for optimization with feasibility check

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply greedy technique for optimal solution.

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
