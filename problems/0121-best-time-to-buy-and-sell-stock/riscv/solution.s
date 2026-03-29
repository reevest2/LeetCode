# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Pattern: DP
#
# Hints:
#   1. Track minimum price seen so far
#   2. At each price, calculate profit if selling today
#   3. Update max profit if current profit is higher
#
# Brute Force: Check all buy/sell pairs. O(n^2) time.
# Optimal: Single pass tracking min price. O(n) time, O(1) space.
#
# RISC-V Calling Convention:
#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)
#   Return: a0 (integer/pointer), fa0 (float/double)
#   Callee-saved: s0-s11, ra
#   Caller-saved: t0-t6, a0-a7

    .text
    .global max_profit
    .type max_profit, @function

max_profit:
    # TODO: implement
    li a0, 0            # return 0
    ret
