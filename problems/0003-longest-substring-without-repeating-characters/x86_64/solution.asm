; 3. Longest Substring Without Repeating Characters
; https://leetcode.com/problems/longest-substring-without-repeating-characters/
; Pattern: String
;
; Hints:
;   1. Use a set to track characters in current window
;   2. Expand right pointer and add character
;   3. If duplicate found, remove from left until valid
;   4. Track maximum window size
;
; Brute Force: Check all substrings for uniqueness. O(n^3) time.
; Optimal: Sliding window with hash set. O(n) time, O(min(n, alphabet_size)) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global length_of_longest_substring

length_of_longest_substring:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
