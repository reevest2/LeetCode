/* 4. Median of Two Sorted Arrays */
/* https://leetcode.com/problems/median-of-two-sorted-arrays/ */
/* Pattern: Array */
/*
 * Hints:
 *   1. Binary search on the shorter array
 *   2. Partition both arrays so left half has (m+n+1)/2 elements
 *   3. Check if maxLeft1 <= minRight2 and maxLeft2 <= minRight1
 *   4. Handle edge cases with -inf and +inf
 *
 * Brute Force: Merge both arrays and find median. O(m+n) time.
 * Optimal: Binary search on partition. O(log(min(m,n))) time, O(1) space.
 */

#include <stdlib.h>
#include <stdbool.h>

double find_median_sorted_arrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    /* TODO: implement */
    return 0.0;
}
