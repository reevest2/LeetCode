# 3. Longest Substring Without Repeating Characters

**Difficulty:** Medium | **Category:** String, Tree  
**Link:** [https://leetcode.com/problems/longest-substring-without-repeating-characters/](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

## Problem Statement

Find the length of the longest substring without repeating characters.

## Key Insight

Use a sliding window with a hash set/map. Expand the right pointer, and when a duplicate is found, shrink from the left until the window is valid again.

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

Check all substrings for uniqueness. O(n^3) time.

### Optimal

Sliding window with hash set. O(n) time, O(min(n, alphabet_size)) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Empty string edge case
- Single character string
- All same characters
- Confusing substring (contiguous) with subsequence (not contiguous)

## Related Problems


## Interview Tips

- What if we need the actual substring, not just length?
- What if we allow at most K repeating characters?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
