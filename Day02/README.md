## Day 02 – Brute Force, Strings & Arrays

This day focuses on solving problems using basic brute-force techniques, stack-based logic,
prefix-style reasoning, and careful handling of arrays and strings.

A total of **4 problems** were solved on this day.

---

### Problems Solved
1. [Pair of Subarrays](#1-pair-of-subarrays)
2. [Poster Printer](#2-poster-printer)
3. [City Biker](#3-city-biker)
4. [Good Sum](#4-good-sum)

---

## 1. Pair of Subarrays  
📄 **Solution:** [`Pair of Subarrays.py`](./Pair%20of%20Subarrays.py)

### Problem Summary
Count the number of **unique pairs of non-overlapping subarrays** such that both subarrays
have the **same sum**.

Each unordered pair should be counted only once.

### Key Idea
- Generate all subarrays and group them by sum.
- For each sum, count pairs of subarrays that do **not overlap**.
- Use sorting and binary search on end indices to avoid double counting.

### Approach
1. Generate all subarrays and store them grouped by their sum.
2. For each group:
   - Sort subarrays by starting index.
   - Count how many subarrays end before the current subarray starts.
3. Accumulate the count across all sums.

---

## 2. Poster Printer  
📄 **Solution:** [`Poster Print.py`](./Poster%20Print.py)

### Problem Summary
Starting from all white sheets (`W`), determine if a target sequence of `R`, `B`, and `W`
can be printed using only the operations `"RB"` and `"BR"` on adjacent sheets.

### Key Insight
- Each operation always produces **one `R` and one `B` together**.
- Therefore, any contiguous segment of non-`W` characters must contain **at least one `R`
  and one `B`**.

### Approach
1. Split the string by `W` to isolate colored segments.
2. For each segment:
   - Check if it contains both `R` and `B`.
3. If all segments satisfy the condition, printing is possible.

---

## 3. City Biker  
📄 **Solution:** [`City Biker.py`](./City%20Biker.py)

### Problem Summary
Given altitude gains between consecutive points, determine the **highest altitude**
reached during the journey.

### Key Idea
- Start at altitude `0`.
- Track cumulative altitude after each step.
- Maintain the maximum altitude encountered.

### Approach
1. Initialize current altitude and maximum altitude to `0`.
2. Iterate through the gains:
   - Update the current altitude.
   - Update the maximum altitude if needed.
3. Return the maximum altitude.

---

## 4. Good Sum  
📄 **Solution:** [`Good Sum.py`](./Good%20Sum.py)

### Problem Summary
For each negative element in the array, remove the **minimum number of previous elements**
whose sum is at least the absolute value of the negative element.
Then replace the negative value with its absolute value.

Return the final sum of the array after all operations.

### Key Idea
- The array is modified dynamically.
- Elements must be removed from **just before** the negative element.

### Approach
1. Use a stack to represent the current state of the array.
2. Traverse the array:
   - Push positive elements directly.
   - For negative elements:
     - Pop elements from the stack until their sum is ≥ absolute value.
     - Push the absolute value of the negative element.
3. Return the sum of elements remaining in the stack.

---

### Language
Python
