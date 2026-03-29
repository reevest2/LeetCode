// 2. Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/
// Pattern: Math
//
// Hints:
//   1. Traverse both lists simultaneously
//   2. Track the carry value
//   3. Don't forget the final carry (e.g., 5+5=10)
//
// Brute Force: Convert to numbers, add, convert back. Fails for very large numbers.
// Optimal: Iterate both lists with carry. Create new nodes for each digit sum. O(max(m,n)) time and space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global add_two_numbers
    .type add_two_numbers, %function

add_two_numbers:
    // TODO: implement
    mov x0, #0          // return 0
    ret
