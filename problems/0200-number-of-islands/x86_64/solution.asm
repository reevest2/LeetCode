; 200. Number of Islands
; https://leetcode.com/problems/number-of-islands/
; Pattern: Graph
;
; Hints:
;   1. Iterate through every cell
;   2. When you find a '1', increment island count and flood-fill
;   3. Mark visited cells as '0' to avoid revisiting
;   4. Check all 4 directions
;
; Brute Force: N/A — BFS/DFS is the standard approach.
; Optimal: BFS or DFS flood fill. O(m*n) time, O(m*n) space worst case.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global num_islands

num_islands:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
