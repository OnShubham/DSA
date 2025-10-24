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
# sorted_arr = calculate_the_left_and_right(arr)
print("Sorted :", sorted_arr)




def calculate_the_left_and_right(arr):
    
    
    if len(arr) <= 1 :
        return arr
    
    
    mid = len(arr) // 2
    
    
    left = calculate_the_left_and_right(arr[mid:])
    right = calculate_the_left_and_right(arr[:mid])
    
    
    return sort_merge(left,right)


def sort_merge(left,right):
    
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






def test(arr):
    
    # check the arr not in 0 
    
    if len(arr) <= 1:
        return arr
    
    
    # divided a arry in subarry mid
    
    
    mid = len(arr) // 2
    
    
    # make a left and right arr
    
    left = test(arr[mid:])
    right = test(arr[:mid])
    
    
    # return in the next func to sort
    
    
    return test_sort(left,right)


def test_sort(left,right):
    
    
    # empty arr
    
    final_arr = []
    
    # i and j intlize 
    
    i = j = 0
    
    
    # calculate the arr and conver in subarry one buy one 
    
    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            
            final_arr.append(left[i])
            
            i += 1
            
        else:
            
            final_arr.append(right[j])
            
            j += 1
            
            
    
    
    final_arr.extend(left[i:])
    
    final_arr.extend(right[j:])
    
    
    return final_arr
    

    
    
def test_1(arr):
    
    # check the arr is not 0 
    
    if len(arr) <= 1:
        return arr
    
    
    # divided a arr in 2 arr
    
    
    mid = len(arr) // 2
    
    
    # left and  right arr
    
    left = test_1(arr[mid:])
    right = test_1(arr[:mid])
    
    
    return test_sort_2(left, right)


def test_sort_2(left, right):
    
    # empty arr
    
    empty_arr = []
    
    # i and j intinlize 
    
    i = j = 0
    
    
    # Compare the arr and subarry
    
    while i < len(left) and j < len(right):
        
        # check the left and right arr
        
        if left[i] <= right[j]:
            
            empty_arr.append(left[i])
            
            i += 1
            
        else:
            
            empty_arr.append(right[j])
            
            j += 1
            
    
    
    empty_arr.extend(left[i:])
    empty_arr.extend(right[j:])
    
    
    return empty_arr
    
    




    






if __name__ == "__main__":    

    arr = [5,6,3,1,4,2,2,1,2,]
    sorted_arr = test_1(arr)
    print(" test:", sorted_arr)
    
    
    
def final(arr):
    
    # check the arr is not < 0
    
    if len(arr) <= 1:
        
        return arr
    
    
    # divided arr
    
    
    mid = len(arr) // 2   # divided a 2 arry
    
    # left and right arr
    
    
    left = final(arr[mid:])
    right = final(arr[:mid])
    
    # return the left and right arr to comapre  fucntion
    return final_compar(left, right)
    

def final_compar(left, right):
    
    
    # make a empty arr
    
    final_arr = []
    
    # i and j intlize left and right
    
    i = j = 0
    
    
    # compare the arr and subarry 
    
    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            
            final_arr.append(left[i])
            
            i += 1
        else:
            final_arr.append(right[j])
            
            j += 1
            
            
    final_arr.extend(left[i:])
    final_arr.extend(right[j:])
    
    
    return final_arr
    
    
    
    
if __name__ == "__main__":    

    arr = [5,6,3,1,4,2,2,1,2,]
    sorted_arr = final(arr)
    print(" Final Test:", sorted_arr)
    
    
    





def merger(arr):
    
    
    # check not in less then 1 
    
    if len(arr) <= 1:
        return arr
    
    
    mid = len(arr) // 2
    
    
    left = merger(arr[mid:])
    right = merger(arr[:mid])
    
    
    return merger_2(left, right)


def merger_2(left, right):
    
    final = []
    
    i = j = 0
    
    
    while i < len(left) and j < len(right):
        
        if left[i] <= right[j]:
            
            final.append(left[i])
            
            i += 1
            
        else:
            
            final.append(right[j])
            
            j += 1
            
    final.extend(left[i:])
    final.extend(right[j:])
    
    return final
    
    


if __name__ == "__main__":    

    arr = [5,6,3,1,4,2,2,1,2,]
    sorted_arr = merger(arr)
    print(" 1 Test:", sorted_arr)
    