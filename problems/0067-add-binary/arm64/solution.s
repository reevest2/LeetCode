// 67. Add Binary
// https://leetcode.com/problems/add-binary/
// Pattern: Other
//
// Hints:
//   1. Think about what data structure best fits this problem
//   2. Consider the other pattern and its variants
//   3. Start with brute force, then optimize
//   4. Watch for edge cases: empty input, single element, duplicates
//
// Brute Force: Try all possibilities. Likely O(n^2) or worse.
// Optimal: Apply other technique for optimal solution.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global add_binary
    .type add_binary, %function

add_binary:
    // TODO: implement
    mov x0, #0          // return 0
    ret
