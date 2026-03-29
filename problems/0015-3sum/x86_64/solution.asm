; 15. 3Sum
; https://leetcode.com/problems/3sum/
; Pattern: Other
;
; Hints:
;   1. Sort the array first
;   2. Fix one element, use two pointers for the remaining two
;   3. Skip duplicate values to avoid duplicate triplets
;   4. Early termination: if nums[i] > 0, no valid triplet possible
;
; Brute Force: Three nested loops. O(n^3) time.
; Optimal: Sort + two pointers. O(n^2) time, O(1) extra space (ignoring sort).
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global three_sum

three_sum:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
