import sys

def solve():
    # Read the number of test cases
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    pointer = 1
    
    results = []
    for _ in range(t):
        n = int(input_data[pointer])
        s = input_data[pointer + 1]
        pointer += 2
        
        # Split the string by 'W' to isolate segments of R and B
        segments = s.split('W')
        is_possible = True
        
        for seg in segments:
            if len(seg) == 0:
                continue
            
            # Count the occurrences of 'R' and 'B'
            has_r = 'R' in seg
            has_b = 'B' in seg
            
            # A segment is impossible if it contains only one of the two colors
            if not (has_r and has_b):
                is_possible = False
                break
        
        if is_possible:
            results.append("YES")
        else:
            results.append("NO")
            
    # Print all results separated by newlines
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
