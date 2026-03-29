; 121. Best Time to Buy and Sell Stock
; https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
; Pattern: DP
;
; Hints:
;   1. Track minimum price seen so far
;   2. At each price, calculate profit if selling today
;   3. Update max profit if current profit is higher
;
; Brute Force: Check all buy/sell pairs. O(n^2) time.
; Optimal: Single pass tracking min price. O(n) time, O(1) space.
;
; x86-64 System V ABI:
;   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)
;   Return: rax (integer/pointer), xmm0 (float/double)
;   Callee-saved: rbx, rbp, r12-r15
;   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11

section .text
global max_profit

max_profit:
    ; TODO: implement
    xor eax, eax       ; return 0
    ret
