; 226. Invert Binary Tree
; https://leetcode.com/problems/invert-binary-tree/
; Pattern: Tree
;
; Hints:
;   1. Think about what data structure best fits this problem
;   2. Consider the tree pattern and its variants
;   3. Start with brute force, then optimize
;   4. Watch for edge cases: empty input, single element, duplicates
;
; Brute Force: Try all possibilities. Likely O(n^2) or worse.
; Optimal: Apply tree technique for optimal solution.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global invert_binary_tree

invert_binary_tree:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
