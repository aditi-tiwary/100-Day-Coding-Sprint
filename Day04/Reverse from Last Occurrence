def transform_string(s, ch):
    # Find last occurrence of ch
    idx = s.rfind(ch)
    
    # If ch not found, return string as is
    if idx == -1:
        return s
    
    # Reverse substring from last occurrence to end
    return s[:idx] + s[idx:][::-1]


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    s = data[0]
    ch = data[1]
    
    transformed_string = transform_string(s, ch)
    print(transformed_string)

if __name__ == "__main__":
    main()
