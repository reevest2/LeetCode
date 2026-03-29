# 2. Add Two Numbers

**Difficulty:** Medium | **Category:** Math  
**Link:** [https://leetcode.com/problems/add-two-numbers/](https://leetcode.com/problems/add-two-numbers/)

## Problem Statement

Add two numbers represented as linked lists where digits are stored in reverse order.

## Key Insight

Process both lists simultaneously, carrying over any value >= 10 to the next digit, just like manual addition.

## Pattern: Math

Apply mathematical properties, number theory, or formulas. Common topics: modular arithmetic, GCD/LCM, prime numbers, combinatorics, and overflow handling.

### When to Use This Pattern

- Problem involves number properties (prime, divisibility, GCD)
- Pattern recognition leads to a formula
- Counting/combinatorics problems
- Geometric problems

### When NOT to Use This Pattern

- Problem is fundamentally about data structure manipulation
- No clear mathematical pattern exists — use algorithmic approach

### Alternatives to Consider

- DP: for counting problems when no closed-form exists
- Simulation: when math is too complex, simulate the process

## Approach

### Brute Force

Convert to numbers, add, convert back. Fails for very large numbers.

### Optimal

Iterate both lists with carry. Create new nodes for each digit sum. O(max(m,n)) time and space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Lists can be different lengths
- Don't forget the final carry
- Handle null nodes gracefully

## Related Problems

- [43. Multiply Strings](../0043-multiply-strings)
- [67. Add Binary](../0067-add-binary)
- [371. Sum of Two Integers](../0371-sum-of-two-integers)
- [445. Add Two Numbers II](../0445-add-two-numbers-ii)

## Interview Tips

- What if digits were in forward order? (Reverse first or use stack)
- Can you do it without extra space?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
