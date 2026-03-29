# 53. Maximum Subarray

**Difficulty:** Easy | **Category:** Array  
**Link:** [https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)

## Problem Statement

Find the contiguous subarray with the largest sum.

## Key Insight

Kadane's algorithm: maintain current sum, reset to current element when sum becomes negative. The maximum sum seen is the answer.

## Pattern: Array

Direct array manipulation using indices, iteration, and in-place modifications. Many array problems use two pointers, sliding window, or prefix sums as sub-patterns.

### When to Use This Pattern

- Problems involving contiguous elements or subarrays
- In-place modifications to save space
- When element positions/indices matter
- Prefix sum problems (range sum queries)

### When NOT to Use This Pattern

- Frequent insertions/deletions in the middle — use linked list
- Need O(1) lookup by value — use hash table
- Data has hierarchical structure — use tree

### Alternatives to Consider

- Hash table: when you need value-based lookups
- Linked list: when you need frequent insertions/deletions
- Deque: when you need efficient operations at both ends

## Approach

### Brute Force

Check all subarrays. O(n^2) time.

### Optimal

Kadane's algorithm. O(n) time, O(1) space.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- All negative numbers: answer is the least negative
- Single element array
- Don't confuse with maximum subarray product

## Related Problems

- [121. Best Time to Buy and Sell Stock](../0121-best-time-to-buy-and-sell-stock)
- [152. Maximum Product Subarray](../0152-maximum-product-subarray)

## Interview Tips

- Can you do it with divide and conquer? (O(n log n))
- What if you need the actual subarray, not just the sum?
- Follow-up: circular subarray?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
