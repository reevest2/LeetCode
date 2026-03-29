# 15. 3Sum

**Difficulty:** Medium | **Category:** Other  
**Link:** [https://leetcode.com/problems/3sum/](https://leetcode.com/problems/3sum/)

## Problem Statement

Find all unique triplets that sum to zero.

## Key Insight

Sort the array, then for each element, use two pointers to find pairs that sum to its negative. Skip duplicates at every level.

## Pattern: Other

Problems that don't fit neatly into a single category or use a unique technique. These often require creative thinking, simulation, or combining multiple patterns.

### When to Use This Pattern

- Problem requires simulation or step-by-step processing
- Creative ad-hoc solutions needed
- Multiple patterns combined

### When NOT to Use This Pattern

- A standard pattern clearly applies — use that pattern

### Alternatives to Consider

- Look for hidden patterns: many 'Other' problems actually use standard techniques
- Try brute force first, then optimize

## Approach

### Brute Force

Three nested loops. O(n^3) time.

### Optimal

Sort + two pointers. O(n^2) time, O(1) extra space (ignoring sort).

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Must skip duplicates at all three positions
- Don't forget to skip duplicates for the outer loop too
- Handle arrays with all zeros

## Related Problems

- [1. Two Sum](../0001-two-sum)
- [16. 3Sum Closest](../0016-3sum-closest)
- [18. 4Sum](../0018-4sum)

## Interview Tips

- How do you handle duplicates?
- Can you do it without sorting?
- Time complexity analysis?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
