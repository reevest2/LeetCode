# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Pattern: String
#
# Hints:
#   1. Use a set to track characters in current window
#   2. Expand right pointer and add character
#   3. If duplicate found, remove from left until valid
#   4. Track maximum window size
#
# Brute Force: Check all substrings for uniqueness. O(n^3) time.
# Optimal: Sliding window with hash set. O(n) time, O(min(n, alphabet_size)) space.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: implement
        pass
