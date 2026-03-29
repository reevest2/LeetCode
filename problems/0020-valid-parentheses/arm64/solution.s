// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
// Pattern: Stack/Queue
//
// Hints:
//   1. Push opening brackets onto stack
//   2. For closing brackets, check if stack top matches
//   3. String is valid only if stack is empty at end
//
// Brute Force: Repeatedly remove matching pairs until none remain. O(n^2) time.
// Optimal: Stack-based matching. O(n) time, O(n) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global is_valid
    .type is_valid, %function

is_valid:
    // TODO: implement
    mov x0, #0          // return 0
    ret
