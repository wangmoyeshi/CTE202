# part 1:counting sort
def counting_sort(arr):
    if not arr:
        return arr
    
    # Determine the range of the input data
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # 1. Count the frequency of each element
    for num in arr:
        count[num] += 1

    # 2. Update count[i] to store the actual position of this digit in output
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 3. Build the output array by iterating in reverse for stability
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output

# Example Usage
arr = [4, 2, 2, 8, 3, 3, 1]
print(f"Counting Sort Output: {counting_sort(arr)}")

# part2:radix sort
def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Base 10 digits (0-9)

    # Store count of occurrences for the current digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr, so that arr now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max_val = max(arr)
    
    # Do counting sort for every digit. 
    # exp is 10^i where i is current digit number
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

# Example Usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print(f"Radix Sort Output: {radix_sort(arr)}")