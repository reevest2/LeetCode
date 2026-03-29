# 1. Two Sum

**Difficulty:** Easy | **Category:** Hash Table
**Link:** [https://leetcode.com/problems/two-sum/](https://leetcode.com/problems/two-sum/)

## Problem Statement

Given an array of integers and a target, return indices of two numbers that add up to target.

**Example:**

```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Reason: nums[0] + nums[1] = 2 + 7 = 9
```

**Constraints:**

- Each input has exactly one solution
- You may not use the same element twice
- Return indices, not the values themselves

## Key Insight

For each number, its complement (`target - num`) is what you need. The entire
problem reduces to: "have I already seen this complement?" A hash map answers
that question in O(1).

## Before You Code

Four observations that guide every approach:

1. **We need indices, not values.** The return type is `int[]`, so any approach
   that loses track of original positions (like sorting) needs extra bookkeeping.
2. **Addition is commutative.** `x + y = y + x`, so you never need to check a
   pair twice. In brute force, the inner loop starts at `i + 1`.
3. **Every number has exactly one complement.** `complement = target - num`.
   That's ALL you're searching for at each step.
4. **Can't reuse the same element.** `nums[i]` and `nums[j]` must be at
   different indices. In the hash map approach, check for the complement
   *before* storing the current number.

## Pattern: Hash Table

Use a hash map/set to achieve O(1) lookups, enabling you to trade space for
time. Store previously seen values and check for complements or duplicates in
constant time.

### When to Use This Pattern

- You need O(1) lookup for previously seen elements
- Finding pairs/groups that satisfy a condition (e.g., two sum, anagrams)
- Counting frequencies of elements
- Detecting duplicates
- Mapping relationships between elements

### When NOT to Use This Pattern

- Data is already sorted -- binary search is more space-efficient
- You need ordered traversal -- use a BST or sorted array instead
- Memory is extremely constrained -- hash maps have overhead
- The key space is small and bounded -- a simple array works better

## Approaches

### Approach 1: Brute Force

Check every possible pair with two nested loops.

```
for i = 0 to n-1:
    for j = i+1 to n-1:
        if nums[i] + nums[j] == target:
            return [i, j]
```

**Time:** O(n^2) -- for each of n elements, scan up to n-1 others.
**Space:** O(1) -- no extra data structures.

**When to use:** When n is very small, or in assembly where building a hash
table is impractical. Also a good starting point in interviews to show you
understand the problem before optimizing.

### Approach 2: Sort + Binary Search

Sort a copy of the array, then for each element, binary search for its
complement.

```
sorted_copy = sort(nums with original indices)
for each (num, original_index):
    complement = target - num
    if binary_search(sorted_copy, complement):
        return [original_index, complement_index]
```

**Time:** O(n log n) -- sorting dominates. Each binary search is O(log n),
done n times = O(n log n).
**Space:** O(n) -- need a copy to preserve original indices.

**Caveat:** Sorting destroys the original index ordering. You must sort pairs
of `(value, original_index)` to recover the answer.

### Approach 3: Sort + Two Pointers

Sort the array, place one pointer at the start and one at the end, then walk
them inward.

```
sort(nums with original indices)
left = 0, right = n - 1
while left < right:
    sum = nums[left] + nums[right]
    if sum == target:  return [left_orig, right_orig]
    if sum < target:   left++     // need a bigger number
    if sum > target:   right--    // need a smaller number
```

**Why it works:** In a sorted array, if the sum is too small, the only way to
increase it is to move the left pointer right (getting a bigger number). If
too big, move the right pointer left. You converge on the answer.

**Time:** O(n log n) -- sorting dominates. The two-pointer scan is O(n).
**Space:** O(n) -- same index-tracking caveat as binary search approach.

**Why learn this:** This exact pattern becomes essential for 3Sum (LeetCode 15)
and 4Sum (LeetCode 18). Two Sum is where you first encounter it.

### Approach 4: Hash Map (Optimal)

One pass through the array. For each number, check if its complement already
exists in the map. If yes, return both indices. If no, store the current
number and its index.

```
seen = {}  // maps value -> index
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

**Walkthrough** with `nums = [2, 7, 11, 15]`, `target = 9`:

| Step | num | complement | In map? | Action          | Map state |
|------|-----|------------|---------|-----------------|-----------|
| i=0  | 2   | 7          | No      | Store {2: 0}    | {2: 0}    |
| i=1  | 7   | 2          | **Yes** | Return [0, 1]   | --        |

Found in just 2 steps. The hash map remembered that 2 was at index 0, so when
we needed it as the complement of 7, the answer was instant.

**Time:** O(n) -- single pass, O(1) lookup per element.
**Space:** O(n) -- hash map stores up to n entries.

**Why check before storing?** If you store first, then a number could match
itself: `nums = [3, 3]`, `target = 6`. Checking first ensures you find the
*other* 3, not the same element.

## Complexity (Optimal Solution)

- **Time:** O(n)
- **Space:** O(n)

## Complexity Comparison

| Approach           | Time       | Space | Preserves Indices? | Best For             |
|--------------------|------------|-------|--------------------|----------------------|
| Brute Force        | O(n^2)     | O(1)  | Yes                | Tiny n, assembly     |
| Sort + Bin Search  | O(n log n) | O(n)  | Extra work needed  | Pre-sorted data      |
| Sort + Two Ptrs    | O(n log n) | O(n)  | Extra work needed  | Foundation for 3Sum  |
| Hash Map           | O(n)       | O(n)  | Yes                | General case (best)  |

The hash map wins because it's the fastest AND naturally preserves indices.

## Common Pitfalls

- **Using the same element twice.** Check the complement BEFORE storing the
  current number. This ensures `nums[i]` can never match itself.
- **Returning values instead of indices.** Store `value -> index` in the map,
  not the reverse. The problem asks for positions, not numbers.
- **Worrying about negative numbers.** Hash maps handle negatives fine.
  `complement = target - (-3)` works as expected.
- **Forgetting sort destroys order.** If using sort-based approaches, you must
  track original indices with pairs of `(value, index)`.

## Language Implementation Notes

| Language | Hash Map Type                | Lookup Idiom                        |
|----------|------------------------------|-------------------------------------|
| Python   | `dict`                       | `if key in seen`                    |
| C#       | `Dictionary<int, int>`       | `seen.TryGetValue(key, out index)`  |
| C++      | `unordered_map<int, int>`    | `seen.find(key) != seen.end()`      |
| C        | Hand-rolled (open addressing)| Linear probing with `occupied` flag |
| Assembly | N/A (use brute force)        | Nested loops, no hash map           |

**C-specific note:** C has no built-in hash map. The solution uses open
addressing with linear probing: hash the key to a slot, if occupied check the
next slot. The hash function scrambles bits to distribute keys evenly. Map
capacity is a power of 2 so `& (CAP - 1)` replaces the slower `% CAP`.

**Assembly note:** All three assembly solutions (x86-64, ARM64, RISC-V) use
brute force O(n^2) because implementing a hash table in assembly would obscure
the real learning: register allocation, calling conventions, and memory access
patterns.

## Related Problems

- [15. 3Sum](../0015-3sum) -- sort + two pointers (builds on approach 3)
- [167. Two Sum II](../0167-two-sum-ii-input-array-is-sorted) -- input is
  sorted, so two pointers directly (no hash map needed)

## Interview Tips

- **Start with brute force** to show understanding, then optimize.
- **"What if the array is sorted?"** -- Two pointers, O(n) time, O(1) space.
  This is LeetCode 167.
- **"What if you need all pairs?"** -- Two pointers or hash set, watch for
  duplicate handling.
- **"What about duplicates?"** -- The hash map naturally handles them because
  you check before storing. For `[3, 3]` with target 6, the second 3 finds
  the first 3 already in the map.

## Study Materials

- [Two_Sum_Study_Guide.pptx](Two_Sum_Study_Guide.pptx) -- 13-slide visual
  study guide covering all 4 approaches, walkthrough, pitfalls, and the hash
  table pattern.

## My Notes

<!-- Write your own notes, observations, and learnings here -->
