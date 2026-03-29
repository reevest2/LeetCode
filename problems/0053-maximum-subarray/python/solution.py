# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Pattern: Array
#
# Hints:
#   1. Track current running sum and max sum seen
#   2. If current sum drops below 0, reset to 0 (or current element)
#   3. Update max sum at each step
#
# Brute Force: Check all subarrays. O(n^2) time.
# Optimal: Kadane's algorithm. O(n) time, O(1) space.


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # TODO: implement
        pass
