// 21. Merge Two Sorted Lists
// https://leetcode.com/problems/merge-two-sorted-lists/
// Pattern: Sorting
//
// Hints:
//   1. Create a dummy head to simplify edge cases
//   2. Compare heads of both lists, pick smaller
//   3. Attach remaining nodes when one list is exhausted
//
// Brute Force: Collect all values, sort, create new list. O((m+n) log(m+n)).
// Optimal: Two-pointer merge. O(m+n) time, O(1) space (iterative).
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global merge_two_lists
    .type merge_two_lists, %function

merge_two_lists:
    // TODO: implement
    mov x0, #0          // return 0
    ret
