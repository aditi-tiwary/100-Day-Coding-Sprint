## Day 04 – Graphs, Trees & Mathematical Patterns

This day focuses on solving problems involving tree traversal, graph concepts, string manipulation, and mathematical patterns. The solutions emphasize clear logic, efficient traversal, and using problem constraints effectively.

---

### 1. Find a Way (Longest Marathon Path)

**Problem Summary**  
The city map is represented as a binary tree where landmarks are nodes and roads are edges.  
The task is to determine the longest possible simple path between any two landmarks.

**Approach**  
- The problem reduces to finding the **diameter of a tree**.
- The tree is treated as an undirected graph.
- Two BFS traversals are used:
  1. First BFS finds the farthest node from an arbitrary node.
  2. Second BFS from that farthest node gives the diameter.
- The result is measured in **number of edges**, not nodes.

**Key Concept**  
Tree Diameter using BFS

---

### 2. Reverse from Last Occurrence

**Problem Summary**  
Given a string `s` and a character `ch`, reverse the substring starting from the **last occurrence** of `ch` till the end of the string.

**Approach**  
- Find the last index of the character using string operations.
- If the character is not found, return the string unchanged.
- Otherwise, reverse only the suffix starting from that index.

**Key Concept**  
String slicing and manipulation

---

### 3. Sum of Node’s Value in a Given Range (BST)

**Problem Summary**  
Given a Binary Search Tree and a range `[start, end]`, compute the sum of all node values that lie within the range (inclusive).

**Approach**  
- Use the BST property to prune unnecessary branches:
  - If a node’s value is smaller than `start`, skip its left subtree.
  - If a node’s value is greater than `end`, skip its right subtree.
- Recursively sum only valid nodes.

**Key Concept**  
BST traversal with pruning

---

### 4. Triangle Game

**Problem Summary**  
Given a row index `n`, print all the values in the `n`th row of the triangular pattern shown.  
(Indexing starts from 0.)

**Approach**  
- The pattern corresponds to **Pascal’s Triangle**.
- Each value is a binomial coefficient.
- The row is generated iteratively using the relation:
  
C(n, k) = C(n, k−1) × (n − k + 1) / k


- This avoids factorial computation and keeps the solution efficient.

**Key Concept**  
Pascal’s Triangle (binomial coefficients)

---

### Language Used
Python

---

### Outcome
All problems for Day 04 were solved successfully, focusing on correctness, efficiency, and clarity of implementation.
