# 167. Two Sum II - Input array is sorted
# https://leetcode.com/problems/two-sum-ii---input-array-is-sorted/
# Pattern: Array
#
# Hints:
#   1. Think about what data structure best fits this problem
#   2. Consider the array pattern and its variants
#   3. Start with brute force, then optimize
#   4. Watch for edge cases: empty input, single element, duplicates
#
# Brute Force: Try all possibilities. Likely O(n^2) or worse.
# Optimal: Apply array technique for optimal solution.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global two_sum_iiinputarrayissorted
    .type two_sum_iiinputarrayissorted, @function

two_sum_iiinputarrayissorted:
    # TODO: implement
    li a0, 0            # return 0
    ret
