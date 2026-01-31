n = int(input())

strings = []
for _ in range(n):
    strings.append(input().strip())

k = int(input())

# Step 1: Count frequency of each string
freq = {}
for s in strings:
    freq[s] = freq.get(s, 0) + 1

# Step 2: Find the kth distinct string
count = 0
for s in strings:
    if freq[s] == 1:
        count += 1
        if count == k:
            print(s)
            break
else:
    print(-1)
