// 5. Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/
// Pattern: String
//
// Hints:
//   1. Each character can be a center of an odd-length palindrome
//   2. Each pair of adjacent characters can center an even-length palindrome
//   3. Expand outward while characters match
//
// Brute Force: Check all substrings. O(n^3) time.
// Optimal: Expand around center. O(n^2) time, O(1) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global longest_palindrome
    .type longest_palindrome, %function

longest_palindrome:
    // TODO: implement
    mov x0, #0          // return 0
    ret
