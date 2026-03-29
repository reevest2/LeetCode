// 53. Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/
// Pattern: Array
//
// Hints:
//   1. Track current running sum and max sum seen
//   2. If current sum drops below 0, reset to 0 (or current element)
//   3. Update max sum at each step
//
// Brute Force: Check all subarrays. O(n^2) time.
// Optimal: Kadane's algorithm. O(n) time, O(1) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global max_sub_array
    .type max_sub_array, %function

max_sub_array:
    // TODO: implement
    mov x0, #0          // return 0
    ret
