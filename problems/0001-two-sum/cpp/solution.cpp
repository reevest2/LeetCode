// 1. Two Sum
// https://leetcode.com/problems/two-sum/
// Pattern: Hash Table
//
// Hints:
//   1. For each number, calculate target - num
//   2. Store each number's index in a hash map
//   3. Check if the complement already exists before storing
//
// Brute Force: Check all pairs with two nested loops. O(n^2) time, O(1) space.
// Optimal: One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.

#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < (int)nums.size(); i++) {
            int complement = target - nums[i];
            auto it = seen.find(complement);
            if (it != seen.end()) {
                return {it->second, i};
            }
            seen[nums[i]] = i;
        }
        return {};
    }
};
