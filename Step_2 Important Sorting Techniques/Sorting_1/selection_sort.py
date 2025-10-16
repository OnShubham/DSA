def selection_sort(arr,n):
    
    for i in range(n - 1):
        
        min_index = i 
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap 
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
    return print(arr)



arr = [4,2,5,1,6,3]
n = len(arr)
# selection_sort(arr,n)

# Function to perform Selection Sort
def selection_sort(arr):
    n = len(arr)  # Get the length of the array
    
    # Loop through all array elements except the last one
    for i in range(n - 1):
        # Assume the current element is the smallest
        min_index = i
        
        # Check the rest of the array to find the actual smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if a smaller element is found
        
        # Swap the found smallest element with the first unsorted element
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        # Print the array after each pass (optional for understanding)
        print(f"After pass {i + 1}: {arr}")
    
    return arr


# Example usage
if __name__ == "__main__":
    arr = [4,2,5,1,6,3]  # Example array
    print("Original array:", arr)
    
    sorted_arr = selection_sort(arr)  # Call the sorting function
    
    print("Sorted array:", sorted_arr)



"""

Step 1:

Find the smallest element in the array → 11

Swap it with the first element (64)

Array becomes: [11, 25, 12, 22, 64]

Step 2:

Now look at the remaining (unsorted) part → [25, 12, 22, 64]

Smallest element is 12

Swap it with 25

Array becomes: [11, 12, 25, 22, 64]

Step 3:

Remaining part → [25, 22, 64]

Smallest element is 22

Swap it with 25

Array becomes: [11, 12, 22, 25, 64]

Step 4:

Remaining part → [25, 64]

Already in order, no swap needed.

Array is now fully sorted:
✅ [11, 12, 22, 25, 64]

"""



def test(arr, n):
    
    
    for i in range(n - 1):
        
        index = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[index]:
                index = j
                
        arr[i] , arr[index] = arr[index], arr[i]
    return print(arr)
    
    
arr = [4,3,1,5,2,8]
n = len(arr)
test(arr, n)


def test_1(arr, n):
    
    for i in range(n - 1):
        
        min_index = i
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[min_index]:
                
                min_index = j
                
        arr[i], arr[min_index] = arr[min_index] , arr[i]
        
    return print(arr)



arr = [4,3,1,5]
n = len(arr)
test_1(arr, n)



def test_2(arr, n):
    

    
    for i in range(n - 1):
        
        min_index = i
        
        for j in range(i + 1, n):
            
            
            if arr[j] < arr[min_index]:
                
                min_index = j
                
                
                
        arr[i] , arr[min_index] = arr[min_index], arr[i]
    
    
    print(arr)




arr = [42, 17, 93, 8, 65, 31, 77, 23, 56, 12]
n = len(arr)
# test_2(arr, n)


def test_3(arr, n):
    
    for i in range(n - 1):
        
        index = i
        
        for j in range(i + 1, n):
            
            if arr[j] > arr[index]:
                
                index = j
                
        arr[i] , arr[index] = arr[index], arr[i]
        
    print(arr) 




arr = [42, 17, 93, 8, 65, 31, 77, 23, 56, 12]
n = len(arr)
test_3(arr, n)



def last(arr,n):
    
    for i in range(n - 1):
        
        
        last = i 
        
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[last]:
                
                last = j 
                
        arr[i], arr[last] = arr[last] , arr[i]
    
    
    print( "Last",arr)



arr = [42, 17, 93, 8, 65, 31, 77, 23, 56, 12]
n = len(arr)
last(arr, n)


def sort(num, n):
    
    for i in range( n - 1):
        
        index = i 
        
        for j in range(i + 1, n):
            
            if num[j] < num[index]:
                index = j 
                
        num[i], num[index] = num[index],num[i]
        
    return print("latest",num)
        
       
        
    
    
num = [42, 17, 93, 8, 65, 31, 77, 23, 56, 12]
n = len(arr)
sort(num, n)




def sort_test(num, n):
    
    for i in range(n - 1):
        
        index = i 
        
        for j in range(i + 1 , n):
            
            if num[j] < num[index]:
                
                index = j
                
                
        num[i] , num[index] = num[index], num[i]
    
    return print(num, "practice")
    
    

num = [42, 17, 93, 8, 65, 31, 77, 23, 56, 12]
n = len(arr)
sort_test(num, n)