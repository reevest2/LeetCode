# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/
# Pattern: Greedy
#
# Hints:
#   1. Think about what data structure best fits this problem
#   2. Consider the greedy pattern and its variants
#   3. Start with brute force, then optimize
#   4. Watch for edge cases: empty input, single element, duplicates
#
# Brute Force: Try all possibilities. Likely O(n^2) or worse.
# Optimal: Apply greedy technique for optimal solution.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global insert_interval
    .type insert_interval, @function

insert_interval:
    # TODO: implement
    li a0, 0            # return 0
    ret
