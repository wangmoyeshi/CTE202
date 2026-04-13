# Part 1: Sequential Search Implementation
def sequential_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Implementation for Expected Output
test_list = [23, 45, 12, 67, 89, 34, 56] 
target_val = 67 

print(f"List: {test_list}") 
print(f"Searching for {target_val} using Sequential Search") 

index, num_comparisons = sequential_search(test_list, target_val)

if index != -1:
    print(f"Found at index {index}")
else:
    print("Not found")

print(f"Number of comparisons: {num_comparisons}")

# Part 2: Binary Search Implementation
def binary_search(arr, target):
    comparisons = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        # Comparison 1: Check if it's the target
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
            
        # Comparison 2: Check if target is greater (only if not found yet)
        comparisons += 1
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons

# Matching the lab manual's example data
sorted_list = [12, 23, 34, 45, 56, 67, 89] 
target_val = 67 

print(f"Sorted List: {sorted_list}")
print(f"Searching for {target_val} using Binary Search")

index, num_comparisons = binary_search(sorted_list, target_val)

if index != -1:
    print(f"Found at index {index}") # Expected: 5 
else:
    print("Not found")

print(f"Number of comparisons: {num_comparisons}") # Expected: 3