def check_the_arr(arr , n):
    
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                
                return print(arr[j], arr[i], "False")
            
            
    return print("True")
        
        
    



if __name__ == "__main__":
    

    arr = [1,2,4,2,1,5,6,3]
    n = len(arr)
    # check_the_arr(arr, n)
    
    
    
def check_the_arr(arr, n):
    # Loop through each element in the array
    for i in range(n):
        
        # Compare arr[i] with every element that comes after it
        for j in range(i + 1, n):
            
            # If a later element is smaller than a previous one,
            # the array is not sorted in non-decreasing order
            if arr[j] < arr[i]:
                
                
                
                
                # Print the two elements that break the sorted order and return False
                return print(arr[j], arr[i], "False")
            
    # If the entire array is checked and no issue found, print True
    return print("True")



if __name__ == "__main__":
    
    # Example array
    arr = [1,2,5,4]
    
    # Length of the array
    n = len(arr)
    
    # Call the function to check if the array is sorted
    check_the_arr(arr, n)
