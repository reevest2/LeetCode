# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Pattern: Math
#
# Hints:
#   1. Traverse both lists simultaneously
#   2. Track the carry value
#   3. Don't forget the final carry (e.g., 5+5=10)
#
# Brute Force: Convert to numbers, add, convert back. Fails for very large numbers.
# Optimal: Iterate both lists with carry. Create new nodes for each digit sum. O(max(m,n)) time and space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global add_two_numbers
    .type add_two_numbers, @function

add_two_numbers:
    # TODO: implement
    li a0, 0            # return 0
    ret
