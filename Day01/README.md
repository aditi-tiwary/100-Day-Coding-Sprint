## Day 01 – Arrays & Strings

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

1. Convert the column letter (a–h) into a number  
   For example, a → 1, b → 2, c → 3, and so on.

2. Convert the row character into an integer.

3. Add the column number and row number.
   - If the sum is even, the square is **Black**.
   - If the sum is odd, the square is **White**.


### Language
Python
