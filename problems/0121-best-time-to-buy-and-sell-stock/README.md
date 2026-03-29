# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy | **Category:** DP  
**Link:** [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Problem Statement

Find the maximum profit from buying and selling a stock once.

## Key Insight

Track the minimum price seen so far and the maximum profit at each step. You want to buy low, sell high.

## Pattern: DP

Break problems into overlapping subproblems and store results to avoid recomputation. Key: identify the state, the transition (recurrence), and base cases. Top-down (memoization) vs bottom-up (tabulation).

### When to Use This Pattern

- Problem has optimal substructure (optimal solution uses optimal sub-solutions)
- Overlapping subproblems (same subproblems solved multiple times)
- Counting problems (number of ways, paths, combinations)
- Optimization problems (min cost, max profit, longest/shortest)
- String matching and sequence alignment

### When NOT to Use This Pattern

- Subproblems don't overlap — divide and conquer is simpler
- Greedy choice property holds — greedy is simpler and faster
- State space is too large to memoize
- Problem requires the actual path, not just the optimal value (may need backtracking)

### Alternatives to Consider

- Greedy: when locally optimal choices lead to global optimum
- Divide and conquer: when subproblems don't overlap
- BFS/DFS: for shortest path or reachability problems
- Math formula: some counting problems have closed-form solutions

## Approach

### Brute Force

Check all buy/sell pairs. O(n^2) time.

### Optimal

Single pass tracking min price. O(n) time, O(1) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Prices only decrease: return 0
- Must buy before selling
- Don't try to find min and max independently — order matters

## Related Problems

- [53. Maximum Subarray](../0053-maximum-subarray)
- [122. Best Time to Buy and Sell Stock II](../0122-best-time-to-buy-and-sell-stock-ii)
- [123. Best Time to Buy and Sell Stock III](../0123-best-time-to-buy-and-sell-stock-iii)
- [188. Best Time to Buy and Sell Stock IV](../0188-best-time-to-buy-and-sell-stock-iv)
- [309. Best Time to Buy and Sell Stock with Cooldown](../0309-best-time-to-buy-and-sell-stock-with-cooldown)

## Interview Tips

- What if you can buy/sell multiple times?
- What if there's a cooldown period?
- What if you can do at most K transactions?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
