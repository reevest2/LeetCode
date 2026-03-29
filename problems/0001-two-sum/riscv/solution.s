# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Pattern: Hash Table
#
# Hints:
#   1. For each number, calculate target - num
#   2. Store each number's index in a hash map
#   3. Check if the complement already exists before storing
#
# Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
# Optimal: One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global two_sum
    .type two_sum, @function

# int* two_sum(int* nums, int numsSize, int target, int* returnSize)
# Args: a0=nums, a1=numsSize, a2=target, a3=returnSize
two_sum:
    addi    sp, sp, -48
    sd      ra, 40(sp)
    sd      s0, 32(sp)
    sd      s1, 24(sp)
    sd      s2, 16(sp)
    sd      s3, 8(sp)
    sd      s4, 0(sp)

    mv      s0, a0              # s0 = nums
    mv      s1, a1              # s1 = numsSize
    mv      s2, a2              # s2 = target
    mv      s3, a3              # s3 = returnSize

    # Outer loop: i = 0
    li      t0, 0               # t0 = i
.L_outer:
    bge     t0, s1, .L_not_found

    # Inner loop: j = i + 1
    addi    t1, t0, 1           # t1 = j
.L_inner:
    bge     t1, s1, .L_next_i

    # Check nums[i] + nums[j] == target
    slli    t2, t0, 2
    add     t2, s0, t2
    lw      t3, 0(t2)           # t3 = nums[i]

    slli    t2, t1, 2
    add     t2, s0, t2
    lw      t4, 0(t2)           # t4 = nums[j]

    add     t3, t3, t4          # t3 = nums[i] + nums[j]
    beq     t3, s2, .L_found

    addi    t1, t1, 1
    j       .L_inner

.L_next_i:
    addi    t0, t0, 1
    j       .L_outer

.L_found:
    mv      s4, t0              # s4 = i (save across malloc call)
    mv      s1, t1              # reuse s1 = j (numsSize no longer needed)

    li      a0, 8
    call    malloc

    sw      s4, 0(a0)           # result[0] = i
    sw      s1, 4(a0)           # result[1] = j
    li      t0, 2
    sw      t0, 0(s3)           # *returnSize = 2
    j       .L_done

.L_not_found:
    li      a0, 0               # return NULL
    sw      zero, 0(s3)         # *returnSize = 0

.L_done:
    ld      s4, 0(sp)
    ld      s3, 8(sp)
    ld      s2, 16(sp)
    ld      s1, 24(sp)
    ld      s0, 32(sp)
    ld      ra, 40(sp)
    addi    sp, sp, 48
    ret
