# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Pattern: Linked List
#
# Hints:
#   1. Initialize prev = null, curr = head
#   2. Save next = curr.next before changing pointer
#   3. Set curr.next = prev
#   4. Advance: prev = curr, curr = next
#
# Brute Force: Store all values, create new reversed list. O(n) time, O(n) space.
# Optimal: In-place pointer reversal. O(n) time, O(1) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global reverse_list
    .type reverse_list, @function

reverse_list:
    # TODO: implement
    li a0, 0            # return 0
    ret
