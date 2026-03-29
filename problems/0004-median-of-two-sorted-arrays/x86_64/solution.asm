; 4. Median of Two Sorted Arrays
; https://leetcode.com/problems/median-of-two-sorted-arrays/
; Pattern: Array
;
; Hints:
;   1. Binary search on the shorter array
;   2. Partition both arrays so left half has (m+n+1)/2 elements
;   3. Check if maxLeft1 <= minRight2 and maxLeft2 <= minRight1
;   4. Handle edge cases with -inf and +inf
;
; Brute Force: Merge both arrays and find median. O(m+n) time.
; Optimal: Binary search on partition. O(log(min(m,n))) time, O(1) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global find_median_sorted_arrays

find_median_sorted_arrays:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
