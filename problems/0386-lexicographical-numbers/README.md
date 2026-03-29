# 386. Lexicographical Numbers

**Difficulty:** Medium | **Category:** Graph, Math  
**Link:** [https://leetcode.com/problems/lexicographical-numbers/](https://leetcode.com/problems/lexicographical-numbers/)

## Problem Statement

Solve the 'Lexicographical Numbers' problem using graph techniques.

## Key Insight

Identify the core graph pattern and apply it efficiently. Consider edge cases and optimize from brute force.

## Pattern: Graph

Model relationships between entities. Key algorithms: BFS (shortest path, unweighted), DFS (connectivity, cycle detection), topological sort (dependencies), Union-Find (connected components).

### When to Use This Pattern

- Problem involves connections/relationships between entities
- Shortest path, reachability, or connectivity questions
- Dependency ordering (topological sort)
- Grid problems (treat cells as nodes)
- Network flow or matching problems

### When NOT to Use This Pattern

- Relationships are strictly hierarchical — use tree
- Simple sequence processing — over-engineering
- Problem has optimal substructure without graph structure — use DP

### Alternatives to Consider

- Tree: when graph is acyclic with single root
- Union-Find: more efficient for dynamic connectivity
- DP on DAG: when graph is directed and acyclic

## Approach

### Brute Force

Try all possibilities. Likely O(n^2) or worse.

### Optimal

Apply graph technique for optimal solution.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Consider edge cases carefully
- Check for off-by-one errors
- Handle empty or minimal inputs

## Interview Tips

- Explain your thought process before coding
- Start with brute force, then optimize
- Discuss time and space complexity

## My Notes

<!-- Write your own notes, observations, and learnings here -->
