## Day 01 – Arrays & Strings

This day covers three problems focused on basic string handling, counting logic, and condition-based problem solving.

### Problems Solved
1. [Chessboard Color](#1-chessboard-color)
2. [Exchanging Gifts](#2-exchanging-gifts)
3. [Distinct K](#3-distinct-k)

Each problem has its own explanation below and a corresponding Python solution file.

---

## 1. Chessboard Color  
📄 **Solution:** [`chessboard.py`](./chessboard.py)

### Problem
A standard chessboard has 8 columns labeled **a** to **h** and 8 rows labeled **1** to **8**.

Each square on the board is either **black** or **white**, and the colors alternate across rows and columns.

You are given the position of a square as a two-character string:
- The first character represents the column (a–h)
- The second character represents the row (1–8)

Your task is to determine whether the given square is **Black** or **White**.

**Example:**
- Input: `a1` → Output: `Black`
- Input: `b2` → Output: `Black`
- Input: `a2` → Output: `White`

### Approach
1. Convert the column letter (a–h) into a number.
2. Convert the row character into an integer.
3. Add the row and column values.
   - Even sum → **Black**
   - Odd sum → **White**

---

## 2. Exchanging Gifts  
📄 **Solution:** [`exchanging_gifts.py`](./exchanging_gifts.py)

### Problem Statement
The royal family exchanges gifts at Christmas, where the youngest member receives gifts from everyone but doesn't give any gifts.

Given the data for all exchanged gifts, identify the youngest member.

**Note:** A family member does not give more than one gift to the same member.

### My Understanding
The youngest member:
- does **not give** any gifts
- receives gifts from **all other members**

### Approach
1. Track how many gifts each member gives.
2. Track how many gifts each member receives.
3. The youngest member must:
   - give `0` gifts
   - receive `n - 1` gifts
4. If no such member exists, return `-1`.

---

## 3. Distinct K  
📄 **Solution:** [`distinct_k.py`](./distinct_k.py)

### Problem Statement
Given `N` strings (some may be duplicated), find the `k`th distinct string.

A string is considered **distinct** if it appears exactly once.

If there are fewer than `k` distinct strings, print `-1`.

### My Understanding
- Count how many times each string appears.
- Only strings with frequency `1` are considered distinct.
- Order matters: the original input order must be preserved.

### Approach
1. Count the frequency of each string.
2. Traverse the list again in input order.
3. Count strings that appear exactly once.
4. When the count reaches `k`, return that string.
5. If not found, return `-1`.

---

### Language
Python
