// 442. Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/
// Pattern: Array
//
// Hints:
//   1. Think about what data structure best fits this problem
//   2. Consider the array pattern and its variants
//   3. Start with brute force, then optimize
//   4. Watch for edge cases: empty input, single element, duplicates
//
// Brute Force: Try all possibilities. Likely O(n^2) or worse.
// Optimal: Apply array technique for optimal solution.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global find_all_duplicatesinan_array
    .type find_all_duplicatesinan_array, %function

find_all_duplicatesinan_array:
    // TODO: implement
    mov x0, #0          // return 0
    ret
