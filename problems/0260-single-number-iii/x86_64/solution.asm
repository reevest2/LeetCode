; 260. Single Number III
; https://leetcode.com/problems/single-number-iii/
; Pattern: Math
;
; Hints:
;   1. Think about what data structure best fits this problem
;   2. Consider the math pattern and its variants
;   3. Start with brute force, then optimize
;   4. Watch for edge cases: empty input, single element, duplicates
;
; Brute Force: Try all possibilities. Likely O(n^2) or worse.
; Optimal: Apply math technique for optimal solution.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global single_number_iii

single_number_iii:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
