# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

data = sys.stdin.read().split()
n = int(data[0])
arr = list(map(int, data[1:]))

non_zero = []
zero_count = 0

for x in arr:
    if x == 0:
        zero_count += 1
    else:
        non_zero.append(x)

# Append zeroes at the end
result = non_zero + [0] * zero_count

print(*result)
