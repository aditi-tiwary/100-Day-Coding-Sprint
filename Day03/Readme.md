## Day 03 – Arrays, Strings & Bit Manipulation

Day 03 focuses on array manipulation, stack-based simulations,
string validation, and efficient bit comparison using prefix sums.

A total of **4 problems** were solved on this day.

---

### Problems Solved
1. [Basketball Game](#1-basketball-game)
2. [Push the Zeroes](#2-push-the-zeroes)
3. [Consistent Car Models](#3-consistent-car-models)
4. [Sum of Different Bits](#4-sum-of-different-bits)

---

## 1. Basketball Game  
📄 **Solution:** [`Basketball Game.py`](./Basketball%20Game.py)

### Problem Summary
Simulate a basketball scoring system where each operation either adds,
modifies, or removes scores based on previous rounds.

### Key Idea
All operations depend on the most recent scores, making a **stack**
the natural data structure.

### Approach
- Use a stack to maintain valid scores.
- Process each operation:
  - Integer → push to stack
  - `+` → push sum of last two scores
  - `D` → push double of last score
  - `C` → remove last score
- Return the sum of remaining scores.

---

## 2. Push the Zeroes  
📄 **Solution:** [`Push the Zeroes.py`](./Push%20the%20Zeroes.py)

### Problem Summary
Rearrange an array by pushing all zeroes to the end while maintaining
the relative order of non-zero elements.

### Key Idea
Preserve order by separating non-zero elements and appending zeroes.

### Approach
- Traverse the array and collect all non-zero elements.
- Count the number of zeroes.
- Append zeroes at the end of the result array.

---

## 3. Consistent Car Models  
📄 **Solution:** [`Consistent Car Models.py`](./Consistent%20Car%20Models.py)

### Problem Summary
Determine how many car models are built using only a given set
of allowed components.

### Key Idea
A model is valid if **every character** in it belongs to the allowed set.

### Approach
- Convert allowed components into a set for fast lookup.
- For each model:
  - Check if all characters exist in the allowed set.
- Count all valid models.

---

## 4. Sum of Different Bits  
📄 **Solution:** [`Sum of Different Bits.py`](./Sum%20of%20Different%20Bits.py)

### Problem Summary
Given two binary strings `a` and `b`, compute the total number of
differing bits when `a` is compared against every substring of `b`
of equal length.

### Key Idea
Instead of comparing each substring explicitly, count mismatches
**position-wise** using prefix sums.

### Approach
- Build a prefix sum array for the count of `'1'`s in `b`.
- For each position in `a`:
  - Determine how many times it aligns with `0` or `1` in `b`.
- Accumulate total differing bits efficiently.

---

### Language
Python
