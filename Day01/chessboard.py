# Day 01 - Chessboard Color Problem
# Determines whether a given chessboard cell is Black or White

s = input().strip()

col = ord(s[0]) - ord('a') + 1
row = int(s[1])

if (col + row) % 2 == 0:
    print("Black")
else:
    print("White")
