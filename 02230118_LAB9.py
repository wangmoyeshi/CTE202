def selection_sort(arr):
    n = len(arr)
    total_comparisons = 0
    total_swaps = 0 # Counter for Task 2
    
    print(f"Original list: {arr}") 
    
    for i in range(n - 1): # Requires n-1 passes 
        min_idx = i # Variable to store index of minimum element 
        
        for j in range(i + 1, n):
            total_comparisons += 1 # Task 2 comparison counter 
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # To achieve exactly 3 swaps, only swap if a smaller element was found
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i] 
            total_swaps += 1 # Increment only when an actual movement occurs
            
        print(f"Pass {i + 1}: {arr}") 
        
    print(f"Sorted list: {arr}")
    print(f"Total comparisons: {total_comparisons}") 
    print(f"Total swaps: {total_swaps}") 

# Test with Sample Input 
arr = [29, 10, 14, 37, 13]
selection_sort(arr)

# Task 3: Create an Index Table for Indexed Search

def create_index_table(arr, block_size):
    """
    Creates an index table by selecting the first element of each block.
    Input: Sorted list (arr) and block size (block_size).
    """
    index_table = []
    
    # Select the first element of each block and store value and position 
    for i in range(0, len(arr), block_size):
        index_table.append((arr[i], i))
    
    # Display output as per Sample Output
    print("Index table created:")
    for value, position in index_table:
        print(f"{value} -> {position}")
    
    return index_table

# Sample Input [cite: 65-67]
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
block_size = 3

# Execute Function
create_index_table(arr, block_size)

# Task 4: Implement Indexed Search

def indexed_search(arr, index_table, key):
    print(f"Search key: {key}") 
    
    imin = -1
    imax = -1
    
    # 1. Search the index table to determine the possible range 
    for i in range(len(index_table)):
        # Check if the key could be in the block starting at this index
        if index_table[i][0] <= key:
            imin = index_table[i][1] 
            # Set imax to the start of the next block minus 1, or the end of the list
            if i + 1 < len(index_table):
                imax = index_table[i+1][1] - 1
                upper_bound_val = index_table[i+1][0]
            else:
                imax = len(arr) - 1
                upper_bound_val = None
        else:
            break

    # Display the found range 
    if imin != -1:
        if upper_bound_val is not None:
            print(f"Index range found:\n{arr[imin]} <= {key} < {upper_bound_val}") 
        
        print(f"Searching from index {imin} to index {imax}:") 

        # 2. Search sequentially inside the selected range 
        for idx in range(imin, imax + 1):
            print(f"Checking index {idx}: {arr[idx]}") 
            if arr[idx] == key:
                print(f"{key} found at index {idx}") 
                return idx
    
    return -1

# Sample Input [cite: 84-86]
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)] 
key = 45 

# Execute Function
indexed_search(arr, index_table, key)

# Task 5: Test Indexed Search for a Key Not Found

def indexed_search(arr, index_table, key):
    print(f"Search key: {key}")
    
    imin = -1
    imax = -1
    
    # 1. Search the index table to determine the possible range 
    for i in range(len(index_table)):
        if index_table[i][0] <= key:
            imin = index_table[i][1]
            if i + 1 < len(index_table):
                imax = index_table[i+1][1] - 1
                upper_bound_val = index_table[i+1][0]
            else:
                imax = len(arr) - 1
                upper_bound_val = "End"
        else:
            break

    # 2. Set imin and imax and display range 
    if imin != -1:
        print(f"Index range found:\n{arr[imin]} <= {key} < {upper_bound_val}")
        print(f"Searching from index {imin} to index {imax}:") 

        # 3. Search sequentially inside the selected range 
        for idx in range(imin, imax + 1):
            print(f"Checking index {idx}: {arr[idx]}") 
            if arr[idx] == key:
                print(f"{key} found at index {idx}")
                return idx
    
    # 5. Return -1 if key not found 
    print(f"{key} not found")
    return -1

# Sample Input 
arr = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65]
index_table = [(10, 0), (25, 3), (40, 6), (55, 9)]
key = 43

# Execute Function
indexed_search(arr, index_table, key)
