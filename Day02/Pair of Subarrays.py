def calculate_pairs(n, arr):
    """
    Counts the number of unique pairs of non-overlapping subarrays 
    with the same sum.
    """
    from collections import defaultdict
    import bisect

    # Map to store the (start, end) indices for every subarray sum found
    # Key: sum, Value: list of tuples (start_index, end_index)
    sum_intervals = defaultdict(list)

    # O(N^2) complexity to find all subarrays.
    # Note: For N=10^6, this is theoretically too slow for a standard time limit.
    # This logic assumes N is smaller or the test cases allow for subarray processing.
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            # Using 1-based indexing as per problem statement
            sum_intervals[current_sum].append((i + 1, j + 1))

    total_count = 0

    # For each unique sum, count non-overlapping pairs
    for s in sum_intervals:
        intervals = sum_intervals[s]
        if len(intervals) < 2:
            continue
        
        # Sort intervals by start index to allow efficient counting
        intervals.sort()
        
        # Extract all end indices and sort them to use binary search
        all_ends = sorted([inter[1] for inter in intervals])
        
        for start, end in intervals:
            # For the current subarray starting at 'start', we want to count
            # how many other subarrays with the same sum ended before 'start'.
            # These are the non-overlapping pairs where the other subarray 
            # comes first.
            
            # Find number of end indices < current start index
            count = bisect.bisect_left(all_ends, start)
            total_count += count

    return total_count

def main():
    import sys
    # Use fast I/O for large N
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    arr = list(map(int, input_data[1:n+1]))
    
    result = calculate_pairs(n, arr)
    sys.stdout.write(str(result) + '\n')

if __name__ == "__main__":
    main()
