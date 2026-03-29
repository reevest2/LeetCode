# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Pattern: Hash Table
#
# Hints:
#   1. For each number, calculate target - num
#   2. Store each number's index in a hash map
#   3. Check if the complement already exists before storing
#
# Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
# Optimal: One-pass hash map: for each num, check if (target - num)
#   exists in map. If yes, return indices. If no, store num. O(n)/O(n).


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
