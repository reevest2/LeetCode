// 15. 3Sum
// https://leetcode.com/problems/3sum/
// Pattern: Other
//
// Hints:
//   1. Sort the array first
//   2. Fix one element, use two pointers for the remaining two
//   3. Skip duplicate values to avoid duplicate triplets
//   4. Early termination: if nums[i] > 0, no valid triplet possible
//
// Brute Force: Three nested loops. O(n^3) time.
// Optimal: Sort + two pointers. O(n^2) time, O(1) extra space (ignoring sort).
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global three_sum
    .type three_sum, %function

three_sum:
    // TODO: implement
    mov x0, #0          // return 0
    ret
