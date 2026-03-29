/*
 * Tests for Problem 0001: Two Sum (C++)
 *
 * Compile and run:
 *   g++ -std=c++17 -Wall -Wextra -o test_0001 test_0001_two_sum.cpp && ./test_0001
 *
 * This file includes the solution directly to avoid complex build setups.
 * The primary validation is a successful LeetCode submission.
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

/* Include the solution */
#include "../../problems/0001-two-sum/cpp/solution.cpp"

static int tests_passed = 0;
static int tests_failed = 0;

void assert_two_sum(std::vector<int> nums, int target,
                    int expected_a, int expected_b, const std::string &name) {
    Solution sol;
    std::vector<int> result = sol.twoSum(nums, target);

    if (result.size() != 2) {
        std::cout << "  FAIL: " << name << " (returned "
                  << result.size() << " elements, expected 2)" << std::endl;
        tests_failed++;
        return;
    }

    std::vector<int> sorted_result = result;
    std::sort(sorted_result.begin(), sorted_result.end());
    int ea = std::min(expected_a, expected_b);
    int eb = std::max(expected_a, expected_b);

    if (sorted_result[0] == ea && sorted_result[1] == eb) {
        std::cout << "  PASS: " << name << std::endl;
        tests_passed++;
    } else {
        std::cout << "  FAIL: " << name
                  << " (expected [" << ea << "," << eb << "]"
                  << ", got [" << sorted_result[0] << "," << sorted_result[1] << "])"
                  << std::endl;
        tests_failed++;
    }
}

int main() {
    std::cout << "Testing Problem 0001: Two Sum (C++)" << std::endl << std::endl;

    assert_two_sum({2, 7, 11, 15}, 9, 0, 1, "example 1");
    assert_two_sum({3, 2, 4}, 6, 1, 2, "example 2");
    assert_two_sum({3, 3}, 6, 0, 1, "duplicate values");
    assert_two_sum({-1, -2, -3, -4, -5}, -8, 2, 4, "negative numbers");
    assert_two_sum({1, 2}, 3, 0, 1, "minimum input");

    std::cout << std::endl << "Results: " << tests_passed << " passed, "
              << tests_failed << " failed" << std::endl;

    return tests_failed > 0 ? 1 : 0;
}
