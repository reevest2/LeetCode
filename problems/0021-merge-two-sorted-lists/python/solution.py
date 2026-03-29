# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Pattern: Sorting
#
# Hints:
#   1. Create a dummy head to simplify edge cases
#   2. Compare heads of both lists, pick smaller
#   3. Attach remaining nodes when one list is exhausted
#
# Brute Force: Collect all values, sort, create new list. O((m+n) log(m+n)).
# Optimal: Two-pointer merge. O(m+n) time, O(1) space (iterative).


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # TODO: implement
        pass
