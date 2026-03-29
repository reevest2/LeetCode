# 132. Palindrome Partitioning II

**Difficulty:** Hard | **Category:** String  
**Link:** [https://leetcode.com/problems/palindrome-partitioning-ii/](https://leetcode.com/problems/palindrome-partitioning-ii/)

## Problem Statement

Solve the 'Palindrome Partitioning II' problem using string techniques.

## Key Insight

Identify the core string pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: String

String manipulation, pattern matching, and parsing. Key techniques: two pointers, sliding window, hashing, and tries. Remember strings are immutable in many languages — build with StringBuilder/list.

### When to Use This Pattern

- Text processing, parsing, or pattern matching
- Anagram detection (sorting or frequency count)
- Palindrome checking (two pointers or DP)
- Substring search (KMP, Rabin-Karp, or sliding window)

### When NOT to Use This Pattern

- Problem is purely numeric — work with numbers directly
- String operations are just masking an array problem

### Alternatives to Consider

- Trie: for prefix matching across many strings
- Regex: for complex pattern matching (but slower)
- Rolling hash: for efficient substring comparison

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply string technique for optimal solution.

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
