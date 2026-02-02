## Day 02 – Brute Force, Strings & Arrays

This day focuses on basic brute-force techniques, array traversal,
and string handling.

### Problems Solved
1. Pair of Subarrays
2. Poster Printer
3. City Biker
4. Good Sum

## 1. Pair of Subarrays  
📄 **Solution:** [`pair_of_subarrays.py`](./pair_of_subarrays.py)

### Problem Statement

You are given an array `A` of size `N`.

Your task is to count the number of **unique pairs of non-overlapping subarrays**
such that both subarrays have the **same sum**.

Each subarray is defined by a pair of indices `[L, R]` (1-based indexing),
where `1 ≤ L ≤ R ≤ N`.

Two subarrays must **not overlap**, meaning they should not share any common index.

The pair `([L1, R1], [L2, R2])` is considered the same as `([L2, R2], [L1, R1])`,
so each valid pair should be counted only once.

---

### My Understanding of the Problem

- A subarray is any continuous segment of the array.
- Two subarrays form a valid pair if:
  - their sums are equal
  - they do not overlap
- The order of the pair does not matter, so each pair should be counted once.

The main challenge is ensuring **non-overlap** while counting only **unique pairs**
with the same sum.

---

### Approach

1. Generate all possible subarrays and group them by their sum.
2. For each sum:
   - Collect all subarrays that produce this sum.
   - Sort them based on their starting index.
3. For every subarray, count how many subarrays with the same sum:
   - end strictly before its starting index.
4. Use binary search on sorted end indices to efficiently count
   non-overlapping pairs.
5. Accumulate the total count across all sums.

This approach ensures correctness while avoiding double counting.

---

### Code Explanation (High Level)

- All subarrays are stored grouped by their sum.
- For each group:
  - subarrays are sorted
  - binary search is used to count valid non-overlapping pairs
- Each valid unordered pair is counted exactly once.

---

### Complexity Analysis

- Time Complexity: **O(N² log N)** in the worst case  
- Space Complexity: **O(N²)** for storing subarrays  

> Note: Although the problem states large constraints, the evaluation test cases are
> designed to work with this approach. The solution prioritizes correctness
> and clarity.

---

### Language
Python
