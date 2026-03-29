// 4. Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/
// Pattern: Array
//
// Hints:
//   1. Binary search on the shorter array
//   2. Partition both arrays so left half has (m+n+1)/2 elements
//   3. Check if maxLeft1 <= minRight2 and maxLeft2 <= minRight1
//   4. Handle edge cases with -inf and +inf
//
// Brute Force: Merge both arrays and find median. O(m+n) time.
// Optimal: Binary search on partition. O(log(min(m,n))) time, O(1) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global find_median_sorted_arrays
    .type find_median_sorted_arrays, %function

find_median_sorted_arrays:
    // TODO: implement
    mov x0, #0          // return 0
    ret
