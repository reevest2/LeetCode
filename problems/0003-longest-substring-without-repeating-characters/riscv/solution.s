# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Pattern: String
#
# Hints:
#   1. Use a set to track characters in current window
#   2. Expand right pointer and add character
#   3. If duplicate found, remove from left until valid
#   4. Track maximum window size
#
# Brute Force: Check all substrings for uniqueness. O(n^3) time.
# Optimal: Sliding window with hash set. O(n) time, O(min(n, alphabet_size)) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global length_of_longest_substring
    .type length_of_longest_substring, @function

length_of_longest_substring:
    # TODO: implement
    li a0, 0            # return 0
    ret
