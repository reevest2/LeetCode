"""
Tests for Problem 0001: Two Sum

These tests validate the solution against known inputs and edge cases.
The primary validation is a successful LeetCode submission; these tests
provide a local feedback loop and catch regressions.
"""

import sys
import os

# Add the solution directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../problems/0001-two-sum/python'))

from solution import Solution


class TestTwoSum:
    def setup_method(self):
        self.solution = Solution()

    # --- Basic examples from LeetCode ---

    def test_example_1(self):
        """nums = [2,7,11,15], target = 9 -> [0,1]"""
        result = self.solution.twoSum([2, 7, 11, 15], 9)
        assert sorted(result) == [0, 1]

    def test_example_2(self):
        """nums = [3,2,4], target = 6 -> [1,2]"""
        result = self.solution.twoSum([3, 2, 4], 6)
        assert sorted(result) == [1, 2]

    def test_example_3(self):
        """nums = [3,3], target = 6 -> [0,1]"""
        result = self.solution.twoSum([3, 3], 6)
        assert sorted(result) == [0, 1]

    # --- Edge cases ---

    def test_negative_numbers(self):
        """Target achieved with negative numbers."""
        result = self.solution.twoSum([-1, -2, -3, -4, -5], -8)
        assert sorted(result) == [2, 4]

    def test_mixed_positive_negative(self):
        """One positive and one negative number sum to target."""
        result = self.solution.twoSum([-3, 4, 3, 90], 0)
        assert sorted(result) == [0, 2]

    def test_zero_target(self):
        """Target is zero with complementary elements."""
        result = self.solution.twoSum([0, 4, 3, 0], 0)
        assert sorted(result) == [0, 3]

    def test_large_numbers(self):
        """Numbers near integer boundaries."""
        result = self.solution.twoSum([2**30, 2**30], 2**31)
        assert sorted(result) == [0, 1]

    def test_two_elements(self):
        """Minimum valid input size."""
        result = self.solution.twoSum([1, 2], 3)
        assert sorted(result) == [0, 1]
