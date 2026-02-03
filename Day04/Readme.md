## Day 04 – Graphs, Trees & Mathematical Patterns

Day 04 focuses on tree traversal, graph-based reasoning, string manipulation, and mathematical pattern recognition.  
The problems emphasize efficient traversal, pruning using data structure properties, and clean iterative logic.

A total of **4 problems** were solved on this day.

---

## Problems Solved

1. [Find a Way](#1-find-a-way)  
2. [Reverse from Last Occurrence](#2-reverse-from-last-occurrence)  
3. [Sum of Node’s Value in a Given Range](#3-sum-of-nodes-value-in-a-given-range)  
4. [Triangle Game](#4-triangle-game)  

---

## 1. Find a Way

📄 **Solution:** [Find A Way.py](Find%20A%20Way.py)

### Problem Summary
The city is represented as a binary tree where landmarks are nodes and roads are edges.  
The task is to determine the longest possible simple path between any two landmarks.

### Key Idea
The longest path in a tree is known as the **tree diameter**.

### Approach
- Treat the tree as an undirected graph.
- Perform two BFS traversals:
  - First BFS finds the farthest node from an arbitrary node.
  - Second BFS from that node gives the longest distance.
- The distance obtained represents the diameter in terms of **number of edges**.

---

## 2. Reverse from Last Occurrence

📄 **Solution:** [Reverse from Last Occurrence.py](Reverse%20from%20Last%20Occurrence.py)

### Problem Summary
Given a string and a character, reverse the substring starting from the **last occurrence** of the given character till the end of the string.

### Key Idea
Only the suffix of the string needs to be modified.

### Approach
- Find the last index of the given character.
- If the character is not present, return the original string.
- Reverse the suffix and append it to the unchanged prefix.

---

## 3. Sum of Node’s Value in a Given Range

📄 **Solution:** [Sum of Node’s value of a given range.py](Sum%20of%20Node%E2%80%99s%20value%20of%20a%20given%20range.py)

### Problem Summary
Given a Binary Search Tree and a range `[start, end]`, compute the sum of all node values lying within the inclusive range.

### Key Idea
Use the **BST property** to prune unnecessary traversal.

### Approach
- If the node value is smaller than `start`, skip the left subtree.
- If the node value is larger than `end`, skip the right subtree.
- If the node lies within the range, include it and traverse both subtrees.

---

## 4. Triangle Game

📄 **Solution:** [Triangle Game.py](Triangle%20Game.py)

### Problem Summary
Given a row index `n`, print all the values in the `n`th row of the triangular pattern shown (indexing starts from 0).

### Key Idea
The pattern corresponds to **Pascal’s Triangle**.

### Approach
- Each value represents a binomial coefficient.
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
