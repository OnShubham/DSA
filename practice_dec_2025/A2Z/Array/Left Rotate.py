def rotation_arr(arr,n):
    
     # Store the first element in a temporary variable
    temp = arr[0]
    # Shift elements to the left
    for i in range(1, n):
        
        arr[i - 1] = arr[i]
        
   # Place the first element at the end 
    arr[-1] = temp
    
    print(arr)
    
    


def rotation_arr_1(arr,n):
    
    data = arr[0]
        
    for i in range(1, n):
        
        arr[i - 1] = arr[i] 
        
        
    arr[-1] = data
    
    print(arr)
    
if __name__ == "__main__":

    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    rotation_arr_1(arr, n)