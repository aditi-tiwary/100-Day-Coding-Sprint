def user_logic(ops):
    '''
    Processes basketball scoring operations using a stack.
    
    Parameters:
        ops (list of str): List of operations as strings
    Returns:
        int: The sum of all scores remaining in the record
    '''
    record = []
    
    for op in ops:
        if op == '+':
            # Sum of the previous two scores
            new_score = record[-1] + record[-2]
            record.append(new_score)
        elif op == 'D':
            # Double the previous score
            new_score = record[-1] * 2
            record.append(new_score)
        elif op == 'C':
            # Invalidate/remove the previous score
            record.pop()
        else:
            # It's an integer, record it
            record.append(int(op))
            
    return sum(record)

if __name__ == "__main__":
    import sys
    # Using sys.stdin.read().split() to handle cases where 
    # operations might be on the same line or multiple lines.
    input_data = sys.stdin.read().split()
    
    if input_data:
        n = int(input_data[0])
        # Extract exactly n operations from the input stream
        ops = input_data[1:n+1]
        
        # Call user logic function and print the output
        result = user_logic(ops)
        print(result)
