# 239. Sliding Window Maximum

**Difficulty:** Hard | **Category:** Sliding Window  
**Link:** [https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

## Problem Statement

Solve the 'Sliding Window Maximum' problem using sliding window techniques.

## Key Insight

Identify the core sliding window pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Sliding Window

Maintain a window (subarray/substring) and slide it across the input, expanding and shrinking to find optimal contiguous sequences. Converts O(n*k) to O(n).

### When to Use This Pattern

- Find min/max/count of a contiguous subarray of size k
- Longest/shortest substring with certain properties
- Problems with 'contiguous' or 'substring' in description
- When you need to track a running state over a range

### When NOT to Use This Pattern

- Elements don't need to be contiguous
- Problem requires comparing non-adjacent subarrays
- No clear expand/shrink condition exists

### Alternatives to Consider

- Prefix sum: for range sum queries without the sliding aspect
- Two pointers: related technique, sometimes interchangeable
- Deque: for sliding window maximum/minimum

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply sliding window technique for optimal solution.

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
