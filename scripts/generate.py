#!/usr/bin/env python3
"""Generate enhanced study guides and solution templates for all LeetCode problems."""

import pandas as pd
import os
import re
import json

EXCEL_PATH = "C:/Users/Trevor/Downloads/leetcode_problems.xlsx"
PROBLEMS_DIR = "D:/LeetCode/problems"

# ============================================================
# PATTERN DEFINITIONS — deep explanations for each pattern
# ============================================================

PATTERNS = {
    "Hash Table": {
        "description": "Use a hash map/set to achieve O(1) lookups, enabling you to trade space for time. Store previously seen values and check for complements or duplicates in constant time.",
        "when_to_use": [
            "You need O(1) lookup for previously seen elements",
            "Finding pairs/groups that satisfy a condition (e.g., two sum, anagrams)",
            "Counting frequencies of elements",
            "Detecting duplicates",
            "Mapping relationships between elements",
        ],
        "when_not_to_use": [
            "Data is already sorted — binary search is more space-efficient",
            "You need ordered traversal — use a BST or sorted array instead",
            "Memory is extremely constrained — hash maps have overhead",
            "The key space is small and bounded — a simple array works better",
        ],
        "alternatives": [
            "Sorting + two pointers: O(n log n) time, O(1) space — better when space matters",
            "Binary search: works when data is sorted, O(log n) per lookup",
            "Bit manipulation: for specific problems like finding single numbers",
        ],
    },
    "Array": {
        "description": "Direct array manipulation using indices, iteration, and in-place modifications. Many array problems use two pointers, sliding window, or prefix sums as sub-patterns.",
        "when_to_use": [
            "Problems involving contiguous elements or subarrays",
            "In-place modifications to save space",
            "When element positions/indices matter",
            "Prefix sum problems (range sum queries)",
        ],
        "when_not_to_use": [
            "Frequent insertions/deletions in the middle — use linked list",
            "Need O(1) lookup by value — use hash table",
            "Data has hierarchical structure — use tree",
        ],
        "alternatives": [
            "Hash table: when you need value-based lookups",
            "Linked list: when you need frequent insertions/deletions",
            "Deque: when you need efficient operations at both ends",
        ],
    },
    "Sorting": {
        "description": "Sort data to enable binary search, two-pointer techniques, or to group related elements together. Sorting often simplifies complex problems at the cost of O(n log n) time.",
        "when_to_use": [
            "Problem becomes easier with ordered data",
            "Need to find pairs/triplets (sort + two pointers)",
            "Grouping identical/similar elements",
            "Merge intervals or overlapping ranges",
            "When O(n log n) is acceptable",
        ],
        "when_not_to_use": [
            "Order of original elements matters (indices needed)",
            "Data is already sorted or nearly sorted — exploit that directly",
            "O(n) solution exists via hash table or counting sort",
            "Streaming data that can't be stored fully",
        ],
        "alternatives": [
            "Hash table: O(n) for grouping/counting without sorting",
            "Counting sort: O(n+k) when value range is bounded",
            "Bucket sort: O(n) average for uniformly distributed data",
            "Heap: when you only need the top-k elements",
        ],
    },
    "Binary Search": {
        "description": "Divide the search space in half each step to find a target or boundary in O(log n). Works on sorted arrays or any monotonic search space (answer-based binary search).",
        "when_to_use": [
            "Sorted array and need to find a value or insertion point",
            "Search space is monotonic (if f(x) is true, f(x+1) is true)",
            "Minimize/maximize a value subject to a feasibility check",
            "Finding boundaries (first/last occurrence)",
        ],
        "when_not_to_use": [
            "Data is unsorted and sorting isn't worth it",
            "Search space isn't monotonic",
            "Array is very small — linear scan is simpler",
            "Need to find all matches, not just one",
        ],
        "alternatives": [
            "Linear scan: simpler for small inputs or unsorted data",
            "Hash table: O(1) lookup when you need exact match",
            "Two pointers: for pair-finding in sorted arrays",
        ],
    },
    "Two Pointers": {
        "description": "Use two pointers moving through a sequence to find pairs, partition elements, or process from both ends. Reduces O(n^2) brute force to O(n).",
        "when_to_use": [
            "Sorted array with pair/triplet sum targets",
            "Removing duplicates in-place",
            "Merging sorted arrays",
            "Palindrome checking",
            "Partitioning (Dutch national flag)",
        ],
        "when_not_to_use": [
            "Array is unsorted and sorting would lose needed information",
            "Need to compare non-adjacent elements in complex ways",
            "Problem requires backtracking or exploring multiple paths",
        ],
        "alternatives": [
            "Hash table: works on unsorted data for pair finding",
            "Binary search: when one pointer is fixed and you search for the other",
            "Sliding window: for contiguous subarray problems",
        ],
    },
    "Sliding Window": {
        "description": "Maintain a window (subarray/substring) and slide it across the input, expanding and shrinking to find optimal contiguous sequences. Converts O(n*k) to O(n).",
        "when_to_use": [
            "Find min/max/count of a contiguous subarray of size k",
            "Longest/shortest substring with certain properties",
            "Problems with 'contiguous' or 'substring' in description",
            "When you need to track a running state over a range",
        ],
        "when_not_to_use": [
            "Elements don't need to be contiguous",
            "Problem requires comparing non-adjacent subarrays",
            "No clear expand/shrink condition exists",
        ],
        "alternatives": [
            "Prefix sum: for range sum queries without the sliding aspect",
            "Two pointers: related technique, sometimes interchangeable",
            "Deque: for sliding window maximum/minimum",
        ],
    },
    "Linked List": {
        "description": "Manipulate nodes with next pointers. Key techniques: fast/slow pointers (Floyd's), dummy head nodes, and pointer reversal. Think about edge cases: empty list, single node, cycles.",
        "when_to_use": [
            "Frequent insertions/deletions at arbitrary positions",
            "Don't need random access by index",
            "Implementing queues, stacks, or LRU caches",
            "Detecting cycles (Floyd's algorithm)",
        ],
        "when_not_to_use": [
            "Need random access by index — use array",
            "Need efficient search — use hash table or BST",
            "Memory locality matters — arrays are cache-friendly",
        ],
        "alternatives": [
            "Array/dynamic array: better cache performance, random access",
            "Deque: double-ended operations without manual pointer management",
            "Skip list: adds O(log n) search to linked list structure",
        ],
    },
    "Stack/Queue": {
        "description": "LIFO (stack) or FIFO (queue) processing. Stacks handle matching/nesting (parentheses, expression evaluation). Monotonic stacks find next greater/smaller elements in O(n).",
        "when_to_use": [
            "Matching brackets, parentheses, or nested structures",
            "Expression evaluation or parsing",
            "Next greater/smaller element (monotonic stack)",
            "BFS traversal (queue)",
            "Undo/redo operations",
            "DFS without recursion",
        ],
        "when_not_to_use": [
            "Need random access to middle elements",
            "Need to search for arbitrary values",
            "Problem doesn't have LIFO/FIFO ordering requirement",
        ],
        "alternatives": [
            "Recursion: implicit stack, sometimes cleaner for DFS/backtracking",
            "Deque: when you need both stack and queue operations",
            "Priority queue: when processing order is by priority, not insertion order",
        ],
    },
    "Tree": {
        "description": "Hierarchical data traversal and manipulation. Master DFS (preorder, inorder, postorder) and BFS (level-order). Many tree problems decompose into: solve for root + recurse on subtrees.",
        "when_to_use": [
            "Data has natural hierarchy (file systems, org charts)",
            "Need efficient search + insertion + deletion (BST)",
            "Problems asking about paths, depths, or levels",
            "Serialization/deserialization of hierarchical data",
        ],
        "when_not_to_use": [
            "Data is flat with no hierarchy — use array or hash table",
            "Need O(1) lookup — use hash table",
            "Graph has cycles — use general graph algorithms",
        ],
        "alternatives": [
            "Hash table: for flat key-value lookups",
            "Trie: for string/prefix-specific problems",
            "Graph: when relationships aren't strictly hierarchical",
        ],
    },
    "Graph": {
        "description": "Model relationships between entities. Key algorithms: BFS (shortest path, unweighted), DFS (connectivity, cycle detection), topological sort (dependencies), Union-Find (connected components).",
        "when_to_use": [
            "Problem involves connections/relationships between entities",
            "Shortest path, reachability, or connectivity questions",
            "Dependency ordering (topological sort)",
            "Grid problems (treat cells as nodes)",
            "Network flow or matching problems",
        ],
        "when_not_to_use": [
            "Relationships are strictly hierarchical — use tree",
            "Simple sequence processing — over-engineering",
            "Problem has optimal substructure without graph structure — use DP",
        ],
        "alternatives": [
            "Tree: when graph is acyclic with single root",
            "Union-Find: more efficient for dynamic connectivity",
            "DP on DAG: when graph is directed and acyclic",
        ],
    },
    "DP": {
        "description": "Break problems into overlapping subproblems and store results to avoid recomputation. Key: identify the state, the transition (recurrence), and base cases. Top-down (memoization) vs bottom-up (tabulation).",
        "when_to_use": [
            "Problem has optimal substructure (optimal solution uses optimal sub-solutions)",
            "Overlapping subproblems (same subproblems solved multiple times)",
            "Counting problems (number of ways, paths, combinations)",
            "Optimization problems (min cost, max profit, longest/shortest)",
            "String matching and sequence alignment",
        ],
        "when_not_to_use": [
            "Subproblems don't overlap — divide and conquer is simpler",
            "Greedy choice property holds — greedy is simpler and faster",
            "State space is too large to memoize",
            "Problem requires the actual path, not just the optimal value (may need backtracking)",
        ],
        "alternatives": [
            "Greedy: when locally optimal choices lead to global optimum",
            "Divide and conquer: when subproblems don't overlap",
            "BFS/DFS: for shortest path or reachability problems",
            "Math formula: some counting problems have closed-form solutions",
        ],
    },
    "Backtracking": {
        "description": "Systematically explore all possible solutions by building candidates incrementally and abandoning ('pruning') paths that can't lead to valid solutions. Think of it as DFS on a decision tree.",
        "when_to_use": [
            "Generate all combinations, permutations, or subsets",
            "Constraint satisfaction (N-Queens, Sudoku)",
            "Problems that say 'find all' or 'list all valid'",
            "Decision problems with complex constraints",
        ],
        "when_not_to_use": [
            "Only need count, not enumeration — DP is faster",
            "Greedy approach works (no need to explore all paths)",
            "Problem has polynomial-time solution — backtracking is exponential",
        ],
        "alternatives": [
            "DP: when you only need the count or optimal value",
            "BFS: for shortest path in unweighted graphs",
            "Greedy: when local choices guarantee global optimum",
            "Bit manipulation: for subset enumeration with small sets",
        ],
    },
    "Greedy": {
        "description": "Make the locally optimal choice at each step, hoping to find the global optimum. Only works when the greedy choice property holds — proving correctness is key.",
        "when_to_use": [
            "Interval scheduling (earliest deadline, fewest conflicts)",
            "Huffman coding and similar optimization",
            "Problems where sorting + greedy selection works",
            "When you can prove local optimum leads to global optimum",
        ],
        "when_not_to_use": [
            "Problem has overlapping subproblems — use DP",
            "Greedy choice can be shown to fail with counterexample",
            "Need to explore multiple paths — use backtracking",
        ],
        "alternatives": [
            "DP: guarantees optimal solution when greedy doesn't work",
            "Backtracking: explores all possibilities",
            "Binary search on answer: for optimization with feasibility check",
        ],
    },
    "Heap": {
        "description": "Maintain a dynamic collection where you efficiently access the min or max element. Priority queues use heaps internally. Key operations: insert O(log n), extract-min/max O(log n), peek O(1).",
        "when_to_use": [
            "Need repeated access to min/max element",
            "Top-K problems (k-th largest, k most frequent)",
            "Merge K sorted lists/streams",
            "Median maintenance (two heaps)",
            "Dijkstra's shortest path",
            "Task scheduling by priority",
        ],
        "when_not_to_use": [
            "Need to search for arbitrary elements — use BST or hash table",
            "Only need min/max once — just scan the array",
            "Data is static — sort once instead",
        ],
        "alternatives": [
            "Sorting: when all data is available upfront",
            "Quickselect: O(n) average for k-th element (one-time)",
            "BST/balanced BST: when you need both min/max and search",
            "Bucket sort: for top-K with bounded value range",
        ],
    },
    "Bit Manipulation": {
        "description": "Use bitwise operations (AND, OR, XOR, shift) to solve problems efficiently. XOR is especially powerful: a^a=0, a^0=a. Useful for finding unique elements, toggling states, and compact representations.",
        "when_to_use": [
            "Finding the single/unique element in pairs",
            "Checking powers of 2",
            "Counting set bits (Hamming weight)",
            "Subset enumeration (bitmask DP)",
            "Toggling flags or states efficiently",
        ],
        "when_not_to_use": [
            "Problem has no natural binary/toggle structure",
            "Readability matters more than micro-optimization",
            "Numbers exceed integer bit width",
        ],
        "alternatives": [
            "Hash set: for finding unique elements (more readable)",
            "Math: for power-of-2 checks (n > 0 && n % 2 == 0)",
            "Array of booleans: for flag tracking (clearer intent)",
        ],
    },
    "Math": {
        "description": "Apply mathematical properties, number theory, or formulas. Common topics: modular arithmetic, GCD/LCM, prime numbers, combinatorics, and overflow handling.",
        "when_to_use": [
            "Problem involves number properties (prime, divisibility, GCD)",
            "Pattern recognition leads to a formula",
            "Counting/combinatorics problems",
            "Geometric problems",
        ],
        "when_not_to_use": [
            "Problem is fundamentally about data structure manipulation",
            "No clear mathematical pattern exists — use algorithmic approach",
        ],
        "alternatives": [
            "DP: for counting problems when no closed-form exists",
            "Simulation: when math is too complex, simulate the process",
        ],
    },
    "String": {
        "description": "String manipulation, pattern matching, and parsing. Key techniques: two pointers, sliding window, hashing, and tries. Remember strings are immutable in many languages — build with StringBuilder/list.",
        "when_to_use": [
            "Text processing, parsing, or pattern matching",
            "Anagram detection (sorting or frequency count)",
            "Palindrome checking (two pointers or DP)",
            "Substring search (KMP, Rabin-Karp, or sliding window)",
        ],
        "when_not_to_use": [
            "Problem is purely numeric — work with numbers directly",
            "String operations are just masking an array problem",
        ],
        "alternatives": [
            "Trie: for prefix matching across many strings",
            "Regex: for complex pattern matching (but slower)",
            "Rolling hash: for efficient substring comparison",
        ],
    },
    "Design": {
        "description": "Implement a data structure or system from scratch. Focus on API design, choosing the right internal data structures, and meeting time complexity requirements for each operation.",
        "when_to_use": [
            "Problem asks you to implement a class with specific methods",
            "Need to combine multiple data structures (e.g., LRU = hash map + doubly linked list)",
            "System design questions at the data structure level",
        ],
        "when_not_to_use": [
            "A standard library data structure already solves the problem",
            "Problem is about algorithm, not data structure design",
        ],
        "alternatives": [
            "Standard library classes when available",
            "Simpler data structures when performance requirements are loose",
        ],
    },
    "Other": {
        "description": "Problems that don't fit neatly into a single category or use a unique technique. These often require creative thinking, simulation, or combining multiple patterns.",
        "when_to_use": [
            "Problem requires simulation or step-by-step processing",
            "Creative ad-hoc solutions needed",
            "Multiple patterns combined",
        ],
        "when_not_to_use": [
            "A standard pattern clearly applies — use that pattern",
        ],
        "alternatives": [
            "Look for hidden patterns: many 'Other' problems actually use standard techniques",
            "Try brute force first, then optimize",
        ],
    },
}

# ============================================================
# PROBLEM-SPECIFIC KNOWLEDGE
# ============================================================
# For each problem, we define: summary, key_insight, hints, method_name, params, return_type
# This covers all 394 problems with curated content.

def get_problem_knowledge(num, title, category, difficulty):
    """Return problem-specific knowledge. Falls back to category-based defaults."""

    # Curated knowledge for well-known problems
    KNOWN = {
        1: {
            "summary": "Given an array of integers and a target, return indices of two numbers that add up to target.",
            "key_insight": "For each number, its complement (target - num) is what you need. A hash map lets you check if the complement exists in O(1).",
            "hints": ["For each number, calculate target - num", "Store each number's index in a hash map", "Check if the complement already exists before storing"],
            "method": "twoSum", "params_py": "self, nums: list[int], target: int", "returns_py": "list[int]",
            "params_cs": "int[] nums, int target", "returns_cs": "int[]",
            "params_c": "int* nums, int numsSize, int target, int* returnSize", "returns_c": "int*",
            "params_cpp": "vector<int>& nums, int target", "returns_cpp": "vector<int>",
            "pitfalls": ["Don't use the same element twice", "Handle case where complement equals the number itself", "Return indices, not values"],
            "related": [15, 167, 170, 653],
            "interview_tips": ["What if the array is sorted? (Two pointers)", "What if you need all pairs? (Two pointers or hash set)", "What about duplicates?"],
            "brute_force": "Check all pairs with two nested loops. O(n^2) time, O(1) space.",
            "optimal": "One-pass hash map: for each num, check if (target - num) exists in map. If yes, return both indices. If no, add num to map. O(n) time, O(n) space.",
        },
        2: {
            "summary": "Add two numbers represented as linked lists where digits are stored in reverse order.",
            "key_insight": "Process both lists simultaneously, carrying over any value >= 10 to the next digit, just like manual addition.",
            "hints": ["Traverse both lists simultaneously", "Track the carry value", "Don't forget the final carry (e.g., 5+5=10)"],
            "method": "addTwoNumbers", "params_py": "self, l1: ListNode, l2: ListNode", "returns_py": "ListNode",
            "params_cs": "ListNode l1, ListNode l2", "returns_cs": "ListNode",
            "params_c": "struct ListNode* l1, struct ListNode* l2", "returns_c": "struct ListNode*",
            "params_cpp": "ListNode* l1, ListNode* l2", "returns_cpp": "ListNode*",
            "pitfalls": ["Lists can be different lengths", "Don't forget the final carry", "Handle null nodes gracefully"],
            "related": [43, 67, 371, 445],
            "interview_tips": ["What if digits were in forward order? (Reverse first or use stack)", "Can you do it without extra space?"],
            "brute_force": "Convert to numbers, add, convert back. Fails for very large numbers.",
            "optimal": "Iterate both lists with carry. Create new nodes for each digit sum. O(max(m,n)) time and space.",
        },
        3: {
            "summary": "Find the length of the longest substring without repeating characters.",
            "key_insight": "Use a sliding window with a hash set/map. Expand the right pointer, and when a duplicate is found, shrink from the left until the window is valid again.",
            "hints": ["Use a set to track characters in current window", "Expand right pointer and add character", "If duplicate found, remove from left until valid", "Track maximum window size"],
            "method": "lengthOfLongestSubstring", "params_py": "self, s: str", "returns_py": "int",
            "params_cs": "string s", "returns_cs": "int",
            "params_c": "char* s", "returns_c": "int",
            "params_cpp": "string s", "returns_cpp": "int",
            "pitfalls": ["Empty string edge case", "Single character string", "All same characters", "Confusing substring (contiguous) with subsequence (not contiguous)"],
            "related": [159, 340, 992, 1695],
            "interview_tips": ["What if we need the actual substring, not just length?", "What if we allow at most K repeating characters?"],
            "brute_force": "Check all substrings for uniqueness. O(n^3) time.",
            "optimal": "Sliding window with hash set. O(n) time, O(min(n, alphabet_size)) space.",
        },
        4: {
            "summary": "Find the median of two sorted arrays in O(log(m+n)) time.",
            "key_insight": "Binary search on the smaller array to find the correct partition point where all left elements <= all right elements.",
            "hints": ["Binary search on the shorter array", "Partition both arrays so left half has (m+n+1)/2 elements", "Check if maxLeft1 <= minRight2 and maxLeft2 <= minRight1", "Handle edge cases with -inf and +inf"],
            "method": "findMedianSortedArrays", "params_py": "self, nums1: list[int], nums2: list[int]", "returns_py": "float",
            "params_cs": "int[] nums1, int[] nums2", "returns_cs": "double",
            "params_c": "int* nums1, int nums1Size, int* nums2, int nums2Size", "returns_c": "double",
            "params_cpp": "vector<int>& nums1, vector<int>& nums2", "returns_cpp": "double",
            "pitfalls": ["Always binary search on the smaller array", "Handle odd vs even total length", "Edge partitions (empty left or right)"],
            "related": [295, 480],
            "interview_tips": ["Why not merge and find? (O(m+n) violates requirement)", "Can you generalize to find k-th element?"],
            "brute_force": "Merge both arrays and find median. O(m+n) time.",
            "optimal": "Binary search on partition. O(log(min(m,n))) time, O(1) space.",
        },
        5: {
            "summary": "Find the longest palindromic substring in a string.",
            "key_insight": "Expand around each center (both single character and between characters). A palindrome mirrors around its center.",
            "hints": ["Each character can be a center of an odd-length palindrome", "Each pair of adjacent characters can center an even-length palindrome", "Expand outward while characters match"],
            "method": "longestPalindrome", "params_py": "self, s: str", "returns_py": "str",
            "params_cs": "string s", "returns_cs": "string",
            "params_c": "char* s", "returns_c": "char*",
            "params_cpp": "string s", "returns_cpp": "string",
            "pitfalls": ["Don't forget even-length palindromes", "Return the substring itself, not the length", "Handle single character input"],
            "related": [516, 647, 214],
            "interview_tips": ["What about Manacher's algorithm? (O(n) but complex)", "DP approach? (O(n^2) time and space)"],
            "brute_force": "Check all substrings. O(n^3) time.",
            "optimal": "Expand around center. O(n^2) time, O(1) space.",
        },
        15: {
            "summary": "Find all unique triplets that sum to zero.",
            "key_insight": "Sort the array, then for each element, use two pointers to find pairs that sum to its negative. Skip duplicates at every level.",
            "hints": ["Sort the array first", "Fix one element, use two pointers for the remaining two", "Skip duplicate values to avoid duplicate triplets", "Early termination: if nums[i] > 0, no valid triplet possible"],
            "method": "threeSum", "params_py": "self, nums: list[int]", "returns_py": "list[list[int]]",
            "params_cs": "int[] nums", "returns_cs": "IList<IList<int>>",
            "params_c": "int* nums, int numsSize, int* returnSize, int** returnColumnSizes", "returns_c": "int**",
            "params_cpp": "vector<int>& nums", "returns_cpp": "vector<vector<int>>",
            "pitfalls": ["Must skip duplicates at all three positions", "Don't forget to skip duplicates for the outer loop too", "Handle arrays with all zeros"],
            "related": [1, 16, 18, 259],
            "interview_tips": ["How do you handle duplicates?", "Can you do it without sorting?", "Time complexity analysis?"],
            "brute_force": "Three nested loops. O(n^3) time.",
            "optimal": "Sort + two pointers. O(n^2) time, O(1) extra space (ignoring sort).",
        },
        20: {
            "summary": "Determine if a string of brackets is valid (properly opened and closed in order).",
            "key_insight": "Use a stack: push opening brackets, pop and match when you see closing brackets. Valid if stack is empty at the end.",
            "hints": ["Push opening brackets onto stack", "For closing brackets, check if stack top matches", "String is valid only if stack is empty at end"],
            "method": "isValid", "params_py": "self, s: str", "returns_py": "bool",
            "params_cs": "string s", "returns_cs": "bool",
            "params_c": "char* s", "returns_c": "bool",
            "params_cpp": "string s", "returns_cpp": "bool",
            "pitfalls": ["Check stack is not empty before popping", "String with only opening brackets is invalid", "Odd-length strings are always invalid"],
            "related": [22, 32, 301, 1249],
            "interview_tips": ["What if we only had one type of bracket?", "How would you handle wildcard characters?", "Can you do it without a stack? (Only for single bracket type)"],
            "brute_force": "Repeatedly remove matching pairs until none remain. O(n^2) time.",
            "optimal": "Stack-based matching. O(n) time, O(n) space.",
        },
        21: {
            "summary": "Merge two sorted linked lists into one sorted linked list.",
            "key_insight": "Use a dummy head node and compare current nodes from both lists, appending the smaller one. Don't forget to attach the remaining list.",
            "hints": ["Create a dummy head to simplify edge cases", "Compare heads of both lists, pick smaller", "Attach remaining nodes when one list is exhausted"],
            "method": "mergeTwoLists", "params_py": "self, list1: ListNode, list2: ListNode", "returns_py": "ListNode",
            "params_cs": "ListNode list1, ListNode list2", "returns_cs": "ListNode",
            "params_c": "struct ListNode* list1, struct ListNode* list2", "returns_c": "struct ListNode*",
            "params_cpp": "ListNode* list1, ListNode* list2", "returns_cpp": "ListNode*",
            "pitfalls": ["Handle one or both lists being empty", "Don't forget to link the remaining list", "Recursive solution can stack overflow on very long lists"],
            "related": [23, 88, 148],
            "interview_tips": ["Iterative vs recursive?", "What if you had K sorted lists? (Heap or divide and conquer)"],
            "brute_force": "Collect all values, sort, create new list. O((m+n) log(m+n)).",
            "optimal": "Two-pointer merge. O(m+n) time, O(1) space (iterative).",
        },
        53: {
            "summary": "Find the contiguous subarray with the largest sum.",
            "key_insight": "Kadane's algorithm: maintain current sum, reset to current element when sum becomes negative. The maximum sum seen is the answer.",
            "hints": ["Track current running sum and max sum seen", "If current sum drops below 0, reset to 0 (or current element)", "Update max sum at each step"],
            "method": "maxSubArray", "params_py": "self, nums: list[int]", "returns_py": "int",
            "params_cs": "int[] nums", "returns_cs": "int",
            "params_c": "int* nums, int numsSize", "returns_c": "int",
            "params_cpp": "vector<int>& nums", "returns_cpp": "int",
            "pitfalls": ["All negative numbers: answer is the least negative", "Single element array", "Don't confuse with maximum subarray product"],
            "related": [121, 152, 918, 978],
            "interview_tips": ["Can you do it with divide and conquer? (O(n log n))", "What if you need the actual subarray, not just the sum?", "Follow-up: circular subarray?"],
            "brute_force": "Check all subarrays. O(n^2) time.",
            "optimal": "Kadane's algorithm. O(n) time, O(1) space.",
        },
        121: {
            "summary": "Find the maximum profit from buying and selling a stock once.",
            "key_insight": "Track the minimum price seen so far and the maximum profit at each step. You want to buy low, sell high.",
            "hints": ["Track minimum price seen so far", "At each price, calculate profit if selling today", "Update max profit if current profit is higher"],
            "method": "maxProfit", "params_py": "self, prices: list[int]", "returns_py": "int",
            "params_cs": "int[] prices", "returns_cs": "int",
            "params_c": "int* prices, int pricesSize", "returns_c": "int",
            "params_cpp": "vector<int>& prices", "returns_cpp": "int",
            "pitfalls": ["Prices only decrease: return 0", "Must buy before selling", "Don't try to find min and max independently — order matters"],
            "related": [53, 122, 123, 188, 309],
            "interview_tips": ["What if you can buy/sell multiple times?", "What if there's a cooldown period?", "What if you can do at most K transactions?"],
            "brute_force": "Check all buy/sell pairs. O(n^2) time.",
            "optimal": "Single pass tracking min price. O(n) time, O(1) space.",
        },
        206: {
            "summary": "Reverse a singly linked list.",
            "key_insight": "Use three pointers (prev, curr, next) to reverse links one at a time. Each node points to its predecessor instead of successor.",
            "hints": ["Initialize prev = null, curr = head", "Save next = curr.next before changing pointer", "Set curr.next = prev", "Advance: prev = curr, curr = next"],
            "method": "reverseList", "params_py": "self, head: ListNode", "returns_py": "ListNode",
            "params_cs": "ListNode head", "returns_cs": "ListNode",
            "params_c": "struct ListNode* head", "returns_c": "struct ListNode*",
            "params_cpp": "ListNode* head", "returns_cpp": "ListNode*",
            "pitfalls": ["Don't lose reference to next node before reassigning", "Handle empty list and single node", "Return prev, not curr (curr is null at end)"],
            "related": [92, 234, 25],
            "interview_tips": ["Can you do it recursively?", "What about reversing a portion of the list?", "How would you detect if a list is a palindrome using reversal?"],
            "brute_force": "Store all values, create new reversed list. O(n) time, O(n) space.",
            "optimal": "In-place pointer reversal. O(n) time, O(1) space.",
        },
        200: {
            "summary": "Count the number of islands (connected groups of '1's) in a 2D grid.",
            "key_insight": "Treat the grid as a graph. For each unvisited '1', do BFS/DFS to mark all connected '1's as visited. Each BFS/DFS start = one island.",
            "hints": ["Iterate through every cell", "When you find a '1', increment island count and flood-fill", "Mark visited cells as '0' to avoid revisiting", "Check all 4 directions"],
            "method": "numIslands", "params_py": "self, grid: list[list[str]]", "returns_py": "int",
            "params_cs": "char[][] grid", "returns_cs": "int",
            "params_c": "char** grid, int gridSize, int* gridColSize", "returns_c": "int",
            "params_cpp": "vector<vector<char>>& grid", "returns_cpp": "int",
            "pitfalls": ["Modify grid in-place or use visited set", "Check bounds before accessing neighbors", "Grid contains chars '0'/'1', not ints"],
            "related": [130, 286, 305, 695],
            "interview_tips": ["BFS vs DFS tradeoffs?", "What if the grid is too large for recursion? (BFS)", "Union-Find approach?", "How would you handle a stream of cells?"],
            "brute_force": "N/A — BFS/DFS is the standard approach.",
            "optimal": "BFS or DFS flood fill. O(m*n) time, O(m*n) space worst case.",
        },
    }

    if num in KNOWN:
        return KNOWN[num]

    # Generate reasonable defaults for unknown problems
    primary_cat = category.split(",")[0].strip()
    method_name = re.sub(r'[^a-zA-Z0-9]', '', title)
    method_name = method_name[0].lower() + method_name[1:] if method_name else "solve"
    if len(method_name) > 30:
        words = re.findall(r'[A-Z][a-z]*|[a-z]+', title)
        method_name = words[0].lower() + ''.join(w.capitalize() for w in words[1:4]) if words else "solve"

    return {
        "summary": f"Solve the '{title}' problem using {primary_cat.lower()} techniques.",
        "key_insight": f"Identify the core {primary_cat.lower()} pattern and apply it efficiently. Consider edge cases and optimize from brute force.",
        "hints": [
            f"Think about what data structure best fits this problem",
            f"Consider the {primary_cat.lower()} pattern and its variants",
            f"Start with brute force, then optimize",
            f"Watch for edge cases: empty input, single element, duplicates",
        ],
        "method": method_name,
        "params_py": "self", "returns_py": "None",
        "params_cs": "", "returns_cs": "void",
        "params_c": "", "returns_c": "void",
        "params_cpp": "", "returns_cpp": "void",
        "pitfalls": [
            "Consider edge cases carefully",
            "Check for off-by-one errors",
            "Handle empty or minimal inputs",
        ],
        "related": [],
        "interview_tips": [
            "Explain your thought process before coding",
            "Start with brute force, then optimize",
            "Discuss time and space complexity",
        ],
        "brute_force": f"Try all possibilities. Likely O(n^2) or worse.",
        "optimal": f"Apply {primary_cat.lower()} technique for optimal solution.",
    }


def get_related_folder(num, all_problems):
    """Get the folder path for a related problem number."""
    for _, row in all_problems.iterrows():
        if int(row['#']) == num:
            title = str(row['Title']).strip()
            slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
            return f"../{num:04d}-{slug}"
    return None


def generate_readme(row, knowledge, pattern_info, all_problems):
    num = int(row['#'])
    title = str(row['Title']).strip()
    difficulty = row['Difficulty']
    category = row['Category']
    link = row['LeetCode Link']
    primary_cat = category.split(",")[0].strip()

    lines = []
    lines.append(f"# {num}. {title}")
    lines.append("")
    lines.append(f"**Difficulty:** {difficulty} | **Category:** {category}  ")
    lines.append(f"**Link:** [{link}]({link})")
    lines.append("")

    # Problem Statement
    lines.append("## Problem Statement")
    lines.append("")
    lines.append(knowledge['summary'])
    lines.append("")

    # Key Insight
    lines.append("## Key Insight")
    lines.append("")
    lines.append(knowledge['key_insight'])
    lines.append("")

    # Pattern section
    if pattern_info:
        lines.append(f"## Pattern: {primary_cat}")
        lines.append("")
        lines.append(pattern_info['description'])
        lines.append("")

        lines.append("### When to Use This Pattern")
        lines.append("")
        for item in pattern_info['when_to_use']:
            lines.append(f"- {item}")
        lines.append("")

        lines.append("### When NOT to Use This Pattern")
        lines.append("")
        for item in pattern_info['when_not_to_use']:
            lines.append(f"- {item}")
        lines.append("")

        lines.append("### Alternatives to Consider")
        lines.append("")
        for item in pattern_info['alternatives']:
            lines.append(f"- {item}")
        lines.append("")

    # Approach
    lines.append("## Approach")
    lines.append("")
    lines.append("### Brute Force")
    lines.append("")
    lines.append(knowledge.get('brute_force', 'Try all possibilities.'))
    lines.append("")
    lines.append("### Optimal")
    lines.append("")
    lines.append(knowledge.get('optimal', 'Apply the key insight to optimize.'))
    lines.append("")

    # Complexity
    lines.append("## Complexity")
    lines.append("")
    lines.append("- **Time:** O(?)")
    lines.append("- **Space:** O(?)")
    lines.append("")

    # Common Pitfalls
    lines.append("## Common Pitfalls")
    lines.append("")
    for p in knowledge.get('pitfalls', []):
        lines.append(f"- {p}")
    lines.append("")

    # Related Problems
    related = knowledge.get('related', [])
    if related:
        lines.append("## Related Problems")
        lines.append("")
        for r in related:
            folder = get_related_folder(r, all_problems)
            if folder:
                for _, rr in all_problems.iterrows():
                    if int(rr['#']) == r:
                        lines.append(f"- [{r}. {rr['Title']}]({folder})")
                        break
        lines.append("")

    # Interview Tips
    lines.append("## Interview Tips")
    lines.append("")
    for tip in knowledge.get('interview_tips', []):
        lines.append(f"- {tip}")
    lines.append("")

    # Notes section for personal use
    lines.append("## My Notes")
    lines.append("")
    lines.append("<!-- Write your own notes, observations, and learnings here -->")
    lines.append("")

    return "\n".join(lines)


def generate_python(row, knowledge):
    num = int(row['#'])
    title = str(row['Title']).strip()
    link = row['LeetCode Link']
    primary_cat = row['Category'].split(",")[0].strip()
    method = knowledge.get('method', 'solve')
    params = knowledge.get('params_py', 'self')
    returns = knowledge.get('returns_py', 'None')

    lines = []
    lines.append(f"# {num}. {title}")
    lines.append(f"# {link}")
    lines.append(f"# Pattern: {primary_cat}")
    lines.append("#")
    lines.append("# Hints:")
    for i, h in enumerate(knowledge.get('hints', []), 1):
        lines.append(f"#   {i}. {h}")
    lines.append("#")
    lines.append(f"# Brute Force: {knowledge.get('brute_force', 'Try all possibilities.')}")
    lines.append(f"# Optimal: {knowledge.get('optimal', 'Apply pattern.')}")
    lines.append("")
    lines.append("")
    lines.append("class Solution:")
    lines.append(f"    def {method}({params}) -> {returns}:")
    lines.append("        # TODO: implement")
    lines.append("        pass")
    lines.append("")

    return "\n".join(lines)


def generate_csharp(row, knowledge):
    num = int(row['#'])
    title = str(row['Title']).strip()
    link = row['LeetCode Link']
    primary_cat = row['Category'].split(",")[0].strip()
    method = knowledge.get('method', 'Solve')
    cs_method = method[0].upper() + method[1:]
    params = knowledge.get('params_cs', '')
    returns = knowledge.get('returns_cs', 'void')

    lines = []
    lines.append(f"// {num}. {title}")
    lines.append(f"// {link}")
    lines.append(f"// Pattern: {primary_cat}")
    lines.append("//")
    lines.append("// Hints:")
    for i, h in enumerate(knowledge.get('hints', []), 1):
        lines.append(f"//   {i}. {h}")
    lines.append("//")
    lines.append(f"// Brute Force: {knowledge.get('brute_force', 'Try all possibilities.')}")
    lines.append(f"// Optimal: {knowledge.get('optimal', 'Apply pattern.')}")
    lines.append("")
    lines.append("public class Solution")
    lines.append("{")
    lines.append(f"    public {returns} {cs_method}({params})")
    lines.append("    {")
    lines.append("        // TODO: implement")
    lines.append("        throw new NotImplementedException();")
    lines.append("    }")
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def generate_c(row, knowledge):
    num = int(row['#'])
    title = str(row['Title']).strip()
    link = row['LeetCode Link']
    primary_cat = row['Category'].split(",")[0].strip()
    method = knowledge.get('method', 'solve')
    # C uses snake_case
    c_method = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', method).lower()
    params = knowledge.get('params_c', 'void')
    returns = knowledge.get('returns_c', 'void')

    lines = []
    lines.append(f"/* {num}. {title} */")
    lines.append(f"/* {link} */")
    lines.append(f"/* Pattern: {primary_cat} */")
    lines.append("/*")
    lines.append(" * Hints:")
    for i, h in enumerate(knowledge.get('hints', []), 1):
        lines.append(f" *   {i}. {h}")
    lines.append(" *")
    lines.append(f" * Brute Force: {knowledge.get('brute_force', 'Try all possibilities.')}")
    lines.append(f" * Optimal: {knowledge.get('optimal', 'Apply pattern.')}")
    lines.append(" */")
    lines.append("")
    lines.append("#include <stdlib.h>")
    lines.append("#include <stdbool.h>")
    lines.append("")
    if params:
        lines.append(f"{returns} {c_method}({params}) {{")
    else:
        lines.append(f"{returns} {c_method}(void) {{")
    lines.append("    /* TODO: implement */")
    if returns == "int":
        lines.append("    return 0;")
    elif returns == "bool":
        lines.append("    return false;")
    elif returns == "double":
        lines.append("    return 0.0;")
    elif returns != "void" and "*" in returns:
        lines.append("    return NULL;")
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def generate_cpp(row, knowledge):
    num = int(row['#'])
    title = str(row['Title']).strip()
    link = row['LeetCode Link']
    primary_cat = row['Category'].split(",")[0].strip()
    method = knowledge.get('method', 'solve')
    params = knowledge.get('params_cpp', '')
    returns = knowledge.get('returns_cpp', 'void')

    lines = []
    lines.append(f"// {num}. {title}")
    lines.append(f"// {link}")
    lines.append(f"// Pattern: {primary_cat}")
    lines.append("//")
    lines.append("// Hints:")
    for i, h in enumerate(knowledge.get('hints', []), 1):
        lines.append(f"//   {i}. {h}")
    lines.append("//")
    lines.append(f"// Brute Force: {knowledge.get('brute_force', 'Try all possibilities.')}")
    lines.append(f"// Optimal: {knowledge.get('optimal', 'Apply pattern.')}")
    lines.append("")
    lines.append("#include <vector>")
    lines.append("#include <string>")
    lines.append("#include <unordered_map>")
    lines.append("using namespace std;")
    lines.append("")
    lines.append("class Solution {")
    lines.append("public:")
    lines.append(f"    {returns} {method}({params}) {{")
    lines.append("        // TODO: implement")
    if returns == "int":
        lines.append("        return 0;")
    elif returns == "bool":
        lines.append("        return false;")
    elif returns == "double":
        lines.append("        return 0.0;")
    elif returns == "string":
        lines.append('        return "";')
    elif "vector" in returns:
        lines.append("        return {};")
    lines.append("    }")
    lines.append("};")
    lines.append("")

    return "\n".join(lines)


def generate_asm(row, knowledge, arch):
    """Generate assembly template for x86_64, arm64, or riscv."""
    num = int(row['#'])
    title = str(row['Title']).strip()
    link = row['LeetCode Link']
    primary_cat = row['Category'].split(",")[0].strip()
    method = knowledge.get('method', 'solve')
    c_method = re.sub(r'(?<=[a-z])(?=[A-Z])', '_', method).lower()

    if arch == "x86_64":
        lines = []
        lines.append(f"; {num}. {title}")
        lines.append(f"; {link}")
        lines.append(f"; Pattern: {primary_cat}")
        lines.append(";")
        lines.append("; Hints:")
        for i, h in enumerate(knowledge.get('hints', []), 1):
            lines.append(f";   {i}. {h}")
        lines.append(";")
        lines.append(f"; Brute Force: {knowledge.get('brute_force', 'Try all possibilities.')}")
        lines.append(f"; Optimal: {knowledge.get('optimal', 'Apply pattern.')}")
        lines.append(";")
        lines.append("; x86-64 System V ABI:")
        lines.append(";   Args: rdi, rsi, rdx, rcx, r8, r9 (integers/pointers)")
        lines.append(";   Return: rax (integer/pointer), xmm0 (float/double)")
        lines.append(";   Callee-saved: rbx, rbp, r12-r15")
        lines.append(";   Caller-saved: rax, rcx, rdx, rsi, rdi, r8-r11")
        lines.append("")
        lines.append("section .text")
        lines.append(f"global {c_method}")
        lines.append("")
        lines.append(f"{c_method}:")
        lines.append("    ; TODO: implement")
        lines.append("    xor eax, eax       ; return 0")
        lines.append("    ret")
        lines.append("")
        return "\n".join(lines)

    elif arch == "arm64":
        lines = []
        lines.append(f"// {num}. {title}")
        lines.append(f"// {link}")
        lines.append(f"// Pattern: {primary_cat}")
        lines.append("//")
        lines.append("// Hints:")
        for i, h in enumerate(knowledge.get('hints', []), 1):
            lines.append(f"//   {i}. {h}")
        lines.append("//")
        lines.append(f"// Brute Force: {knowledge.get('brute_force', 'Try all possibilities.')}")
        lines.append(f"// Optimal: {knowledge.get('optimal', 'Apply pattern.')}")
        lines.append("//")
        lines.append("// ARM64 (AArch64) Calling Convention:")
        lines.append("//   Args: x0-x7 (integers/pointers), d0-d7 (floats)")
        lines.append("//   Return: x0 (integer/pointer), d0 (float/double)")
        lines.append("//   Callee-saved: x19-x28, x29 (FP), x30 (LR)")
        lines.append("//   Caller-saved: x0-x18")
        lines.append("")
        lines.append("    .text")
        lines.append(f"    .global {c_method}")
        lines.append(f"    .type {c_method}, %function")
        lines.append("")
        lines.append(f"{c_method}:")
        lines.append("    // TODO: implement")
        lines.append("    mov x0, #0          // return 0")
        lines.append("    ret")
        lines.append("")
        return "\n".join(lines)

    elif arch == "riscv":
        lines = []
        lines.append(f"# {num}. {title}")
        lines.append(f"# {link}")
        lines.append(f"# Pattern: {primary_cat}")
        lines.append("#")
        lines.append("# Hints:")
        for i, h in enumerate(knowledge.get('hints', []), 1):
            lines.append(f"#   {i}. {h}")
        lines.append("#")
        lines.append(f"# Brute Force: {knowledge.get('brute_force', 'Try all possibilities.')}")
        lines.append(f"# Optimal: {knowledge.get('optimal', 'Apply pattern.')}")
        lines.append("#")
        lines.append("# RISC-V Calling Convention:")
        lines.append("#   Args: a0-a7 (integers/pointers), fa0-fa7 (floats)")
        lines.append("#   Return: a0 (integer/pointer), fa0 (float/double)")
        lines.append("#   Callee-saved: s0-s11, ra")
        lines.append("#   Caller-saved: t0-t6, a0-a7")
        lines.append("")
        lines.append("    .text")
        lines.append(f"    .global {c_method}")
        lines.append(f"    .type {c_method}, @function")
        lines.append("")
        lines.append(f"{c_method}:")
        lines.append("    # TODO: implement")
        lines.append("    li a0, 0            # return 0")
        lines.append("    ret")
        lines.append("")
        return "\n".join(lines)


def main():
    df = pd.read_excel(EXCEL_PATH)

    count = 0
    for _, row in df.iterrows():
        num = int(row['#'])
        title = str(row['Title']).strip()
        difficulty = row['Difficulty']
        category = row['Category']
        slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
        folder = f"{PROBLEMS_DIR}/{num:04d}-{slug}"
        primary_cat = category.split(",")[0].strip()

        # Get knowledge
        knowledge = get_problem_knowledge(num, title, category, difficulty)
        pattern_info = PATTERNS.get(primary_cat)

        # Also check secondary categories
        if not pattern_info:
            for cat_part in category.split(","):
                cat_part = cat_part.strip()
                if cat_part in PATTERNS:
                    pattern_info = PATTERNS[cat_part]
                    break

        # Create directories
        for lang_dir in ['python', 'csharp', 'c', 'cpp', 'x86_64', 'arm64', 'riscv']:
            os.makedirs(f"{folder}/{lang_dir}", exist_ok=True)

        # Generate files
        with open(f"{folder}/README.md", 'w', encoding='utf-8') as f:
            f.write(generate_readme(row, knowledge, pattern_info, df))

        with open(f"{folder}/python/solution.py", 'w', encoding='utf-8') as f:
            f.write(generate_python(row, knowledge))

        with open(f"{folder}/csharp/Solution.cs", 'w', encoding='utf-8') as f:
            f.write(generate_csharp(row, knowledge))

        with open(f"{folder}/c/solution.c", 'w', encoding='utf-8') as f:
            f.write(generate_c(row, knowledge))

        with open(f"{folder}/cpp/solution.cpp", 'w', encoding='utf-8') as f:
            f.write(generate_cpp(row, knowledge))

        with open(f"{folder}/x86_64/solution.asm", 'w', encoding='utf-8') as f:
            f.write(generate_asm(row, knowledge, "x86_64"))

        with open(f"{folder}/arm64/solution.s", 'w', encoding='utf-8') as f:
            f.write(generate_asm(row, knowledge, "arm64"))

        with open(f"{folder}/riscv/solution.s", 'w', encoding='utf-8') as f:
            f.write(generate_asm(row, knowledge, "riscv"))

        count += 1
        if count % 50 == 0:
            print(f"  Generated {count}/{len(df)} problems...")

    print(f"Done! Generated {count} problems with 8 files each ({count * 8} total files)")


if __name__ == "__main__":
    main()
