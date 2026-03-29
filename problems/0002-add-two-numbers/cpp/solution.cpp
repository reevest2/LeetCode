// 2. Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/
// Pattern: Math
//
// Hints:
//   1. Traverse both lists simultaneously
//   2. Track the carry value
//   3. Don't forget the final carry (e.g., 5+5=10)
//
// Brute Force: Convert to numbers, add, convert back. Fails for very large numbers.
// Optimal: Iterate both lists with carry. Create new nodes for each digit sum. O(max(m,n)) time and space.

#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // TODO: implement
    }
};
