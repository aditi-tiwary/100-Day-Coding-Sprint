def generate_row(n):
    row = [1]
    val = 1
    
    for k in range(1, n + 1):
        val = val * (n - k + 1) // k
        row.append(val)
    
    return row


if __name__ == "__main__":
    n = int(input().strip())
    result = generate_row(n)
    print(" ".join(map(str, result)))
