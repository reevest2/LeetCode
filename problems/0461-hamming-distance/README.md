# 461. Hamming Distance

**Difficulty:** Easy | **Category:** Bit Manipulation  
**Link:** [https://leetcode.com/problems/hamming-distance/](https://leetcode.com/problems/hamming-distance/)

## Problem Statement

Solve the 'Hamming Distance' problem using bit manipulation techniques.

## Key Insight

Identify the core bit manipulation pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Bit Manipulation

Use bitwise operations (AND, OR, XOR, shift) to solve problems efficiently. XOR is especially powerful: a^a=0, a^0=a. Useful for finding unique elements, toggling states, and compact representations.

### When to Use This Pattern

- Finding the single/unique element in pairs
- Checking powers of 2
- Counting set bits (Hamming weight)
- Subset enumeration (bitmask DP)
- Toggling flags or states efficiently

### When NOT to Use This Pattern

- Problem has no natural binary/toggle structure
- Readability matters more than micro-optimization
- Numbers exceed integer bit width

### Alternatives to Consider

- Hash set: for finding unique elements (more readable)
- Math: for power-of-2 checks (n > 0 && n % 2 == 0)
- Array of booleans: for flag tracking (clearer intent)

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply bit manipulation technique for optimal solution.

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
