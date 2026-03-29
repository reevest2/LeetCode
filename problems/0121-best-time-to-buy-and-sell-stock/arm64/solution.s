// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Pattern: DP
//
// Hints:
//   1. Track minimum price seen so far
//   2. At each price, calculate profit if selling today
//   3. Update max profit if current profit is higher
//
// Brute Force: Check all buy/sell pairs. O(n^2) time.
// Optimal: Single pass tracking min price. O(n) time, O(1) space.
//
// ARM64 (AArch64) Calling Convention:
//   Args: x0-x7 (integers/pointers), d0-d7 (floats)
//   Return: x0 (integer/pointer), d0 (float/double)
//   Callee-saved: x19-x28, x29 (FP), x30 (LR)
//   Caller-saved: x0-x18

    .text
    .global max_profit
    .type max_profit, %function

max_profit:
    // TODO: implement
    mov x0, #0          // return 0
    ret
