// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// Pattern: DP
//
// Hints:
//   1. Track minimum price seen so far
//   2. At each price, calculate profit if selling today
//   3. Update max profit if current profit is higher
//
// Brute Force: Check all buy/sell pairs. O(n^2) time.
// Optimal: Single pass tracking min price. O(n) time, O(1) space.

#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        // TODO: implement
        return 0;
    }
};
