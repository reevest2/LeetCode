; 21. Merge Two Sorted Lists
; https://leetcode.com/problems/merge-two-sorted-lists/
; Pattern: Sorting
;
; Hints:
;   1. Create a dummy head to simplify edge cases
;   2. Compare heads of both lists, pick smaller
;   3. Attach remaining nodes when one list is exhausted
;
; Brute Force: Collect all values, sort, create new list. O((m+n) log(m+n)).
; Optimal: Two-pointer merge. O(m+n) time, O(1) space (iterative).
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global merge_two_lists

merge_two_lists:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
