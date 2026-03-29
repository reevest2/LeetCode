// 200. Number of Islands
// https://leetcode.com/problems/number-of-islands/
// Pattern: Graph
//
// Hints:
//   1. Iterate through every cell
//   2. When you find a '1', increment island count and flood-fill
//   3. Mark visited cells as '0' to avoid revisiting
//   4. Check all 4 directions
//
// Brute Force: N/A — BFS/DFS is the standard approach.
// Optimal: BFS or DFS flood fill. O(m*n) time, O(m*n) space worst case.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global num_islands
    .type num_islands, %function

num_islands:
    // TODO: implement
    mov x0, #0          // return 0
    ret
