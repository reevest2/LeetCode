; 20. Valid Parentheses
; https://leetcode.com/problems/valid-parentheses/
; Pattern: Stack/Queue
;
; Hints:
;   1. Push opening brackets onto stack
;   2. For closing brackets, check if stack top matches
;   3. String is valid only if stack is empty at end
;
; Brute Force: Repeatedly remove matching pairs until none remain. O(n^2) time.
; Optimal: Stack-based matching. O(n) time, O(n) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global is_valid

is_valid:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
