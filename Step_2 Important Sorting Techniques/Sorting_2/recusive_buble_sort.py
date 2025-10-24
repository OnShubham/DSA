def recursive_buble_sort(arr, n):
    
    if n == 1:
        return
    
    for i in range( n - 1):
        
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
               
    recursive_buble_sort(arr, n - 1)
    

def recur_buble_sort(arr,n):
    
    if n == 1:
        return
    
    for i in range( n - 1):
        
        if arr[i] > arr [i + 1]:
            
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
    recur_buble_sort(arr , n - 1)











def test_1(arr, n):
    
    if n == 1:
        return
    
    for i in range(n - 1):
        
        if arr[i] > arr[i + 1]:
            
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
    test_1(arr, n - 1)




if __name__ == "__main__":
    arr = [2,3,4,2,1,23,4,5,2,3]
    n = len(arr)
    
    # recursive_buble_sort(arr, n)
    test_1(arr, n)
    
    print(arr)
    
    
