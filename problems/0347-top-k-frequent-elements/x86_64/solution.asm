; 347. Top K Frequent Elements
; https://leetcode.com/problems/top-k-frequent-elements/
; Pattern: Heap
;
; Hints:
;   1. Think about what data structure best fits this problem
;   2. Consider the heap pattern and its variants
;   3. Start with brute force, then optimize
;   4. Watch for edge cases: empty input, single element, duplicates
;
; Brute Force: Try all possibilities. Likely O(n^2) or worse.
; Optimal: Apply heap technique for optimal solution.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global top_kfrequent_elements

top_kfrequent_elements:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
