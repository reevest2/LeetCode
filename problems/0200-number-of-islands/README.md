# 200. Number of Islands

**Difficulty:** Medium | **Category:** Graph, Math  
**Link:** [https://leetcode.com/problems/number-of-islands/](https://leetcode.com/problems/number-of-islands/)

## Problem Statement

Count the number of islands (connected groups of '1's) in a 2D grid.

## Key Insight

Treat the grid as a graph. For each unvisited '1', do BFS/DFS to mark all connected '1's as visited. Each BFS/DFS start = one island.

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

N/A — BFS/DFS is the standard approach.

### Optimal

BFS or DFS flood fill. O(m*n) time, O(m*n) space worst case.

## Complexity

- **Time:** O(?)
- **Space:** O(?)

## Common Pitfalls

- Modify grid in-place or use visited set
- Check bounds before accessing neighbors
- Grid contains chars '0'/'1', not ints

## Related Problems

- [130. Surrounded Regions](../0130-surrounded-regions)

## Interview Tips

- BFS vs DFS tradeoffs?
- What if the grid is too large for recursion? (BFS)
- Union-Find approach?
- How would you handle a stream of cells?

## My Notes

<!-- Write your own notes, observations, and learnings here -->
