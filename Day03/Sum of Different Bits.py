def compareBits(a, b):
    m, n = len(a), len(b)

    # Prefix sum for count of '1's in b
    prefix_ones = [0] * (n + 1)
    for i in range(n):
        prefix_ones[i + 1] = prefix_ones[i] + (b[i] == '1')

    total_diff = 0
    window_count = n - m + 1

    for i in range(m):
        # Range in b that aligns with a[i]
        left = i
        right = i + window_count  # exclusive

        ones = prefix_ones[right] - prefix_ones[left]
        zeros = window_count - ones

        if a[i] == '0':
            total_diff += ones
        else:
            total_diff += zeros

    return total_diff


if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    print(compareBits(a, b))
