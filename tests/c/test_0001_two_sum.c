/*
 * Tests for Problem 0001: Two Sum (C)
 *
 * Compile and run:
 *   gcc -Wall -Wextra -o test_0001 test_0001_two_sum.c && ./test_0001
 *
 * This file includes the solution directly to avoid complex build setups.
 * The primary validation is a successful LeetCode submission.
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

/* Include the solution */
#include "../../problems/0001-two-sum/c/solution.c"

static int tests_passed = 0;
static int tests_failed = 0;

static void assert_two_sum(int *nums, int nums_size, int target,
                           int expected_a, int expected_b, const char *name) {
    int return_size;
    int *result = twoSum(nums, nums_size, target, &return_size);

    if (result == NULL) {
        printf("  FAIL: %s (returned NULL)\n", name);
        tests_failed++;
        return;
    }

    /* Sort the result pair for comparison */
    int ra = result[0] < result[1] ? result[0] : result[1];
    int rb = result[0] < result[1] ? result[1] : result[0];
    int ea = expected_a < expected_b ? expected_a : expected_b;
    int eb = expected_a < expected_b ? expected_b : expected_a;

    if (ra == ea && rb == eb) {
        printf("  PASS: %s\n", name);
        tests_passed++;
    } else {
        printf("  FAIL: %s (expected [%d,%d], got [%d,%d])\n",
               name, ea, eb, ra, rb);
        tests_failed++;
    }

    free(result);
}

int main(void) {
    printf("Testing Problem 0001: Two Sum (C)\n\n");

    /* Example 1 */
    {
        int nums[] = {2, 7, 11, 15};
        assert_two_sum(nums, 4, 9, 0, 1, "example 1");
    }

    /* Example 2 */
    {
        int nums[] = {3, 2, 4};
        assert_two_sum(nums, 3, 6, 1, 2, "example 2");
    }

    /* Duplicate values */
    {
        int nums[] = {3, 3};
        assert_two_sum(nums, 2, 6, 0, 1, "duplicate values");
    }

    /* Negative numbers */
    {
        int nums[] = {-1, -2, -3, -4, -5};
        assert_two_sum(nums, 5, -8, 2, 4, "negative numbers");
    }

    /* Minimum input */
    {
        int nums[] = {1, 2};
        assert_two_sum(nums, 2, 3, 0, 1, "minimum input");
    }

    printf("\nResults: %d passed, %d failed\n", tests_passed, tests_failed);
    return tests_failed > 0 ? 1 : 0;
}
