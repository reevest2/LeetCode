// 1. Two Sum
// https://leetcode.com/problems/two-sum/
// Pattern: Hash Table
//
// Hints:
//   1. For each number, calculate target - num
//   2. Store each number's index in a hash map
//   3. Check if the complement already exists before storing
//
// Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
// Optimal: One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global two_sum
    .type two_sum, %function

two_sum:
    // TODO: implement
    mov x0, #0          // return 0
    ret
