def good_sum(N, A):
    stack = []

    for x in A:
        if x >= 0:
            # Positive elements are directly added
            stack.append(x)
        else:
            # Negative element: we need to remove elements before it
            need = abs(x)

            # Remove elements until sum >= abs(x)
            while stack and need > 0:
                need -= stack.pop()

            # Push the absolute value of x
            stack.append(abs(x))

    return sum(stack)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    A = list(map(int, data[1:]))

    result = good_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()
