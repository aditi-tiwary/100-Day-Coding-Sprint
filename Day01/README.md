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

### Distinct K

#### Problem Statement

You wish to help Ashish, who possesses a collection of N strings, some of which may be duplicated, and has been assigned the task of finding the kth unique string.

If the number of unique strings is less than k, he needs to display `-1`. Considering you are Ashish's best friend, can you assist him with this challenge?

#### Input Format
- The first line contains an integer `N` denoting the number of strings.
- The next `N` lines contain strings.
- The next line contains an integer `k`.

#### Output Format
- Print the `k`th distinct string.
- If there are fewer than `k` unique strings, print `-1`.

#### Constraints
- 1 ≤ N ≤ 10³  
- 1 ≤ length of each string ≤ 10³  

### My Understanding of the Problem

We are given a list of strings where some strings may appear more than once.

A string is considered **distinct** if it appears exactly once in the list.

The task is to find the `k`th such distinct string while maintaining the original order of the input.

If the total number of distinct strings is less than `k`, the output should be `-1`.

### Approach

1. First, count how many times each string appears in the list.
2. Then, iterate through the list again in the original order.
3. Each time a string appears exactly once, consider it a distinct string.
4. Keep a count of such distinct strings.
5. When the count reaches `k`, return that string.
6. If the end of the list is reached and fewer than `k` distinct strings are found, return `-1`.


### Language
Python
