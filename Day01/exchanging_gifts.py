n, m = map(int, input().split())

# Track gifts given and received
given = [0] * (n + 1)
received = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    given[a] += 1
    received[b] += 1

# Find the youngest member
for person in range(1, n + 1):
    if given[person] == 0 and received[person] == n - 1:
        print(person)
        break
else:
    print(-1)
