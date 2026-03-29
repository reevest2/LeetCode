/* 21. Merge Two Sorted Lists */
/* https://leetcode.com/problems/merge-two-sorted-lists/ */
/* Pattern: Sorting */
/*
 * Hints:
 *   1. Create a dummy head to simplify edge cases
 *   2. Compare heads of both lists, pick smaller
 *   3. Attach remaining nodes when one list is exhausted
 *
 * Brute Force: Collect all values, sort, create new list. O((m+n) log(m+n)).
 * Optimal: Two-pointer merge. O(m+n) time, O(1) space (iterative).
 */

#include <stdlib.h>
#include <stdbool.h>

struct ListNode* merge_two_lists(struct ListNode* list1, struct ListNode* list2) {
    /* TODO: implement */
    return NULL;
}
