# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Pattern: Array
#
# Hints:
#   1. Track current running sum and max sum seen
#   2. If current sum drops below 0, reset to 0 (or current element)
#   3. Update max sum at each step
#
# Brute Force: Check all subarrays. O(n^2) time.
# Optimal: Kadane's algorithm. O(n) time, O(1) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global max_sub_array
    .type max_sub_array, @function

max_sub_array:
    # TODO: implement
    li a0, 0            # return 0
    ret
