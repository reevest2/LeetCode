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

// int* two_sum(int* nums, int numsSize, int target, int* returnSize)
// Args: x0=nums, w1=numsSize, w2=target, x3=returnSize
two_sum:
    stp     x29, x30, [sp, #-64]!
    mov     x29, sp
    stp     x19, x20, [sp, #16]
    stp     x21, x22, [sp, #32]
    str     x23, [sp, #48]

    mov     x19, x0             // x19 = nums
    mov     w20, w1             // w20 = numsSize
    mov     w21, w2             // w21 = target
    mov     x22, x3             // x22 = returnSize

    // Outer loop: i = 0
    mov     w8, #0              // w8 = i
.L_outer:
    cmp     w8, w20
    b.ge    .L_not_found

    // Inner loop: j = i + 1
    add     w9, w8, #1          // w9 = j
.L_inner:
    cmp     w9, w20
    b.ge    .L_next_i

    // Check nums[i] + nums[j] == target
    sxtw    x10, w8
    ldr     w11, [x19, x10, lsl #2]    // w11 = nums[i]
    sxtw    x10, w9
    ldr     w12, [x19, x10, lsl #2]    // w12 = nums[j]
    add     w11, w11, w12
    cmp     w11, w21
    b.eq    .L_found

    add     w9, w9, #1
    b       .L_inner

.L_next_i:
    add     w8, w8, #1
    b       .L_outer

.L_found:
    // Save i and j
    mov     w23, w9             // save j in w23
    stp     w8, w9, [sp, #-16]!  // also push to stack for safety
    mov     x0, #8
    bl      malloc
    ldp     w8, w9, [sp], #16   // restore i, j

    str     w8, [x0]            // result[0] = i
    str     w23, [x0, #4]       // result[1] = j
    mov     w10, #2
    str     w10, [x22]          // *returnSize = 2
    b       .L_done

.L_not_found:
    mov     x0, #0              // return NULL
    str     wzr, [x22]          // *returnSize = 0

.L_done:
    ldr     x23, [sp, #48]
    ldp     x21, x22, [sp, #32]
    ldp     x19, x20, [sp, #16]
    ldp     x29, x30, [sp], #64
    ret
