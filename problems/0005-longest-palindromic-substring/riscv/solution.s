# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Pattern: String
#
# Hints:
#   1. Each character can be a center of an odd-length palindrome
#   2. Each pair of adjacent characters can center an even-length palindrome
#   3. Expand outward while characters match
#
# Brute Force: Check all substrings. O(n^3) time.
# Optimal: Expand around center. O(n^2) time, O(1) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global longest_palindrome
    .type longest_palindrome, @function

longest_palindrome:
    # TODO: implement
    li a0, 0            # return 0
    ret
