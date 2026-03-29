# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Pattern: Sorting
#
# Hints:
#   1. Create a dummy head to simplify edge cases
#   2. Compare heads of both lists, pick smaller
#   3. Attach remaining nodes when one list is exhausted
#
# Brute Force: Collect all values, sort, create new list. O((m+n) log(m+n)).
# Optimal: Two-pointer merge. O(m+n) time, O(1) space (iterative).
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global merge_two_lists
    .type merge_two_lists, @function

merge_two_lists:
    # TODO: implement
    li a0, 0            # return 0
    ret
