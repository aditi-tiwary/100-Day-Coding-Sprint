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


### Exchanging Gifts

#### Problem Statement

The royal family exchanges gifts at Christmas, where the youngest member receives gifts from everyone but doesn't give any gifts.  
Given the data for all the exchanged gifts among the family members, identify the youngest member, who is the one receiving gifts from everyone but not giving any.

**Note:** A family member does not give more than one gift to the same member.

#### Input Format
- The first line contains two integers `n` and `m` denoting the number of family members and the number of gifts exchanged.
- The next `m` lines each contain two integers `aᵢ` and `bᵢ`, representing that a gift was given by `aᵢ` to `bᵢ`.

#### Output Format
- Print a single integer representing the youngest member of the family.
- If no such member exists, print `-1`.

#### Constraints
- 1 ≤ n ≤ 10⁴  
- 0 ≤ m ≤ 10⁵  
- 1 ≤ aᵢ, bᵢ ≤ n  

### My Understanding of the Problem

The youngest family member is defined by two clear conditions:

1. They **do not give** any gifts to anyone.
2. They **receive gifts from all other members** of the family.

To solve this:
- I track how many gifts each member **gives**.
- I also track how many gifts each member **receives**.

After processing all gift exchanges:
- The youngest member will have:
  - `0` gifts given, and
  - `n - 1` gifts received (from everyone else).

If no family member satisfies both conditions, the answer is `-1`.

### Code Explanation

1. Read the number of family members (`n`) and the number of gift exchanges (`m`).

2. Create two lists:
   - `given[i]` stores how many gifts member `i` has given.
   - `received[i]` stores how many gifts member `i` has received.

3. For each gift exchange (`a → b`):
   - Increase the gift count of the giver (`a`).
   - Increase the gift count of the receiver (`b`).

4. After processing all exchanges, check each family member:
   - If a member has given `0` gifts and received `n - 1` gifts,
     that member is the youngest.

5. Print the youngest member’s number.
   - If no such member exists, print `-1`.


### Language
Python
