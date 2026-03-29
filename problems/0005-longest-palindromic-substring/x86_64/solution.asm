; 5. Longest Palindromic Substring
; https://leetcode.com/problems/longest-palindromic-substring/
; Pattern: String
;
; Hints:
;   1. Each character can be a center of an odd-length palindrome
;   2. Each pair of adjacent characters can center an even-length palindrome
;   3. Expand outward while characters match
;
; Brute Force: Check all substrings. O(n^3) time.
; Optimal: Expand around center. O(n^2) time, O(1) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global longest_palindrome

longest_palindrome:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
