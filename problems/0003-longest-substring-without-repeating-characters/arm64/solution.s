// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Pattern: String
//
// Hints:
//   1. Use a set to track characters in current window
//   2. Expand right pointer and add character
//   3. If duplicate found, remove from left until valid
//   4. Track maximum window size
//
// Brute Force: Check all substrings for uniqueness. O(n^3) time.
// Optimal: Sliding window with hash set. O(n) time, O(min(n, alphabet_size)) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global length_of_longest_substring
    .type length_of_longest_substring, %function

length_of_longest_substring:
    // TODO: implement
    mov x0, #0          // return 0
    ret
