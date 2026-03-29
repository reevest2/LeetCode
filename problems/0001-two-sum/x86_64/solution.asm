; 1. Two Sum
; https://leetcode.com/problems/two-sum/
; Pattern: Hash Table
;
; Hints:
;   1. For each number, calculate target - num
;   2. Store each number's index in a hash map
;   3. Check if the complement already exists before storing
;
; Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
; Optimal: One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global two_sum

two_sum:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
