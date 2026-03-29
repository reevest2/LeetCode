/* 1. Two Sum */
/* https://leetcode.com/problems/two-sum/ */
/* Pattern: Hash Table */
/*
 * Hints:
 *   1. For each number, calculate target - num
 *   2. Store each number's index in a hash map
 *   3. Check if the complement already exists before storing
 *
 * Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
 * Optimal: One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.
 */

#include <stdlib.h>
#include <stdbool.h>

#define MAP_CAP 8192

typedef struct {
    int key;
    int value;
    bool occupied;
} Entry;

static unsigned int hash(int key) {
    unsigned int k = (unsigned int)key;
    k ^= k >> 16;
    k *= 0x45d9f3b;
    k ^= k >> 16;
    return k & (MAP_CAP - 1);
}

int* two_sum(int* nums, int numsSize, int target, int* returnSize) {
    Entry map[MAP_CAP];
    for (int i = 0; i < MAP_CAP; i++) {
        map[i].occupied = false;
    }

    for (int i = 0; i < numsSize; i++) {
        int complement = target - nums[i];

        unsigned int idx = hash(complement);
        while (map[idx].occupied) {
            if (map[idx].key == complement) {
                int *result = malloc(2 * sizeof(int));
                result[0] = map[idx].value;
                result[1] = i;
                *returnSize = 2;
                return result;
            }
            idx = (idx + 1) & (MAP_CAP - 1);
        }

        idx = hash(nums[i]);
        while (map[idx].occupied) {
            idx = (idx + 1) & (MAP_CAP - 1);
        }
        map[idx].key = nums[i];
        map[idx].value = i;
        map[idx].occupied = true;
    }

    *returnSize = 0;
    return NULL;
}
