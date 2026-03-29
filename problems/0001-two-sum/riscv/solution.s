# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Pattern: Hash Table
#
# Hints:
#   1. For each number, calculate target - num
#   2. Store each number's index in a hash map
#   3. Check if the complement already exists before storing
#
# Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
# Optimal: One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global two_sum
    .type two_sum, @function

two_sum:
    # TODO: implement
    li a0, 0            # return 0
    ret
