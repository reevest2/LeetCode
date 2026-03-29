; 206. Reverse Linked List
; https://leetcode.com/problems/reverse-linked-list/
; Pattern: Linked List
;
; Hints:
;   1. Initialize prev = null, curr = head
;   2. Save next = curr.next before changing pointer
;   3. Set curr.next = prev
;   4. Advance: prev = curr, curr = next
;
; Brute Force: Store all values, create new reversed list. O(n) time, O(n) space.
; Optimal: In-place pointer reversal. O(n) time, O(1) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global reverse_list

reverse_list:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
