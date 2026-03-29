# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
# Pattern: Graph
#
# Hints:
#   1. Iterate through every cell
#   2. When you find a '1', increment island count and flood-fill
#   3. Mark visited cells as '0' to avoid revisiting
#   4. Check all 4 directions
#
# Brute Force: N/A — BFS/DFS is the standard approach.
# Optimal: BFS or DFS flood fill. O(m*n) time, O(m*n) space worst case.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global num_islands
    .type num_islands, @function

num_islands:
    # TODO: implement
    li a0, 0            # return 0
    ret
