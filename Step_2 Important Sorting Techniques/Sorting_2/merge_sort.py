"""
Merge Sort — Explanation

Merge Sort is a Divide and Conquer algorithm.
It works by:

1. Dividing the array into two halves recursively until each subarray has one element.

2. Merging the subarrays back together in sorted order.

---------------------------------------------------------
🔹 Algorithm Steps

1. If the array has one or zero elements, it’s already sorted.

2. Find the middle index and divide the array into two halves.

3. Recursively sort both halves.

4. Merge the two sorted halves into a single sorted array.

"""

# Function to perform merge sort
def merge_sort(arr):
    # Base case: If the array has 0 or 1 element, it’s already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Find the middle index to divide the array into two halves
    mid = len(arr) // 2

    # Step 2: Recursively sort the left half
    left = merge_sort(arr[:mid])

    # Step 3: Recursively sort the right half
    right = merge_sort(arr[mid:])

    # Step 4: Merge the two sorted halves
    return merge(left, right)


# Function to merge two sorted arrays into one sorted array
def merge(left, right):
    result = []  # temporary list to store merged elements
    i = j = 0    # pointers for left and right subarrays

    # Step 5: Compare elements from left and right and add the smaller one to 'result'
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # add from left if smaller or equal
            i += 1
        else:
            result.append(right[j])  # add from right if smaller
            j += 1

    # Step 6: Add any remaining elements from the left subarray
    result.extend(left[i:])

    # Step 7: Add any remaining elements from the right subarray
    result.extend(right[j:])

    # Step 8: Return the merged and sorted list
    return result


# -------------------------
# Example 1
arr = [3, 2, 8, 5, 1, 4, 23]

# Step 9: Call merge_sort on the full array
sorted_arr = merge_sort(arr)

# Step 10: Print the final sorted array
print("Sorted array:", sorted_arr)
# Output: [1, 2, 3, 4, 5, 8, 23]

# -------------------------
# Example 2
arr = [4, 2, 1, 6, 7]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
# Output: [1, 2, 4, 6, 7]





def calculate_the_left_and_right(arr):
    
    if len(arr) <= 1:
        return arr
    
    
    mid = len(arr) // 2
    
    
    left = calculate_the_left_and_right(arr[mid:])
    
    right = calculate_the_left_and_right(arr[:mid])
    
    
    return calculate_merge(left, right)

def calculate_merge(left,right):
    
    
    result = []
    
    i = j = 0
    
    
    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            
            result.append(left[i])
            
            i += 1
        else:
            
            result.append(right[j])
            
            
            j += 1
            
        
        
        result.extend(left[i:])
        
        result.extend(right[j:])
        
        
        return result
        
    
    
    


arr = [4, 2, 1, 6, 7]
sorted_arr = calculate_the_left_and_right(arr)
print("Sorted :", sorted_arr)