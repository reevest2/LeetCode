# 5. Longest Palindromic Substring

**Difficulty:** Medium | **Category:** String, Tree  
**Link:** [https://leetcode.com/problems/longest-palindromic-substring/](https://leetcode.com/problems/longest-palindromic-substring/)

## Problem Statement

Find the longest palindromic substring in a string.

## Key Insight

Expand around each center (both single character and between characters). A palindrome mirrors around its center.

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

Check all substrings. O(n^3) time.

### Optimal

Expand around center. O(n^2) time, O(1) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Don't forget even-length palindromes
- Return the substring itself, not the length
- Handle single character input

## Related Problems

- [214. Shortest Palindrome](../0214-shortest-palindrome)

## Interview Tips

- What about Manacher's algorithm? (O(n) but complex)
- DP approach? (O(n^2) time and space)

## My Notes

<!-- Write your own notes, observations, and learnings here -->
