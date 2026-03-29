; 2. Add Two Numbers
; https://leetcode.com/problems/add-two-numbers/
; Pattern: Math
;
; Hints:
;   1. Traverse both lists simultaneously
;   2. Track the carry value
;   3. Don't forget the final carry (e.g., 5+5=10)
;
; Brute Force: Convert to numbers, add, convert back. Fails for very large numbers.
; Optimal: Iterate both lists with carry. Create new nodes for each digit sum. O(max(m,n)) time and space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global add_two_numbers

add_two_numbers:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
