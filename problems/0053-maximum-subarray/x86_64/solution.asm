; 53. Maximum Subarray
; https://leetcode.com/problems/maximum-subarray/
; Pattern: Array
;
; Hints:
;   1. Track current running sum and max sum seen
;   2. If current sum drops below 0, reset to 0 (or current element)
;   3. Update max sum at each step
;
; Brute Force: Check all subarrays. O(n^2) time.
; Optimal: Kadane's algorithm. O(n) time, O(1) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global max_sub_array

max_sub_array:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
