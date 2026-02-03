import sys

# Increase recursion depth just in case the tree is very skewed
sys.setrecursionlimit(2000)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val: # Unique values, so < is safer
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def sum_of_values_in_range(root, start, end):
    if not root:
        return 0
    
    # Case 1: Node is too small, check only the right subtree
    if root.val < start:
        return sum_of_values_in_range(root.right, start, end)
    
    # Case 2: Node is too large, check only the left subtree
    if root.val > end:
        return sum_of_values_in_range(root.left, start, end)
    
    # Case 3: Node is in range [start, end]
    # Add its value and search both children
    return root.val + sum_of_values_in_range(root.left, start, end) + \
                      sum_of_values_in_range(root.right, start, end)

def main():
    # Reading all input and splitting by any whitespace
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    
    # The next n items are the tree node values
    values = list(map(int, input_data[1 : n + 1]))
    
    # The two items after the node values are start and end
    start = int(input_data[n + 1])
    end = int(input_data[n + 2])
    
    root = None
    for val in values:
        root = insert_into_bst(root, val)
    
    result = sum_of_values_in_range(root, start, end)
    print(result)

if __name__ == "__main__":
    main()
