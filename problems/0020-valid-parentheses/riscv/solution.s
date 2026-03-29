# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Pattern: Stack/Queue
#
# Hints:
#   1. Push opening brackets onto stack
#   2. For closing brackets, check if stack top matches
#   3. String is valid only if stack is empty at end
#
# Brute Force: Repeatedly remove matching pairs until none remain. O(n^2) time.
# Optimal: Stack-based matching. O(n) time, O(n) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global is_valid
    .type is_valid, @function

is_valid:
    # TODO: implement
    li a0, 0            # return 0
    ret
