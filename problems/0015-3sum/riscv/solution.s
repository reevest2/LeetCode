# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Pattern: Other
#
# Hints:
#   1. Sort the array first
#   2. Fix one element, use two pointers for the remaining two
#   3. Skip duplicate values to avoid duplicate triplets
#   4. Early termination: if nums[i] > 0, no valid triplet possible
#
# Brute Force: Three nested loops. O(n^3) time.
# Optimal: Sort + two pointers. O(n^2) time, O(1) extra space (ignoring sort).
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global three_sum
    .type three_sum, @function

three_sum:
    # TODO: implement
    li a0, 0            # return 0
    ret
