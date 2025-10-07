# def count_freq(arr,n):
    
#     visited = [False] * n
    
#     for i in range(n):
        
#         if (visited[i] == True):
#             continue
#         count = 1
        
#         for j in range(i + 1, n):
            
#             if(arr[i] == arr[j]):
#                 visited[j] = True
#                 count += 1
                
#         print(arr[i], count)




def count_freq(arr,n):
    
    # Create a list 'total' of size n, initialized with False
    # This keeps track of elements that are already counted
    total = [False] * n
    
    
    # Outer loop to go through each element of the array
    for i in range(n):
        
         # If this element is already counted, skip it
        if (total[i] == True):
            continue
        
        # Start counting frequency for current element
        count = 1
        
        
         # Inner loop to compare current element with remaining elements
        for j in range( i + 1, n):
            
            
            # If a duplicate element is found
            if (arr[i] == arr[j]):
                
                # Mark this duplicate as counted
                total[j] = True
                
                # Increase the count
                count += 1
                
         # Print the element and its frequency
        print(arr[i], count)




  
    



def count_total(arr,n):
    
    total = [False] * n
    
    for i in range(n):
        
        if (total[i] == True):
            continue
        count = 1
        
        for j in range(i + 1, n):
            
            if (arr[i] == arr[j]):
                
                total[j] = True
                
                count += 1
                
        print(arr[i], count)
    






def test(arr,n):
    
    total = [False] * n
    
    for i in range(n):
        
        if total[i] == True:
            continue
        count = 1
        
        
        for j in range(i + 1, n):
            
            if(arr[i] == arr[j]):
                
                total[j] = True
                
                count += 1
                
        print(arr[i], count)








def test_1(arr,n):
    
    calculate = [False] * n
    
    for i in range(n):
        
        if (calculate[i] == True):
            continue
        
        count = 1
        
        for j in range(i + 1, n):
            
            if (arr[i] == arr[j]):
                
                calculate[j] = True
                
                
                count += 1
                
        print(arr[i], count)
            
            
        
        
            
        
        
    
    
    
    







if __name__ == "__main__":
    arr = [10,5,10,15,10,5, 2]
    n = len(arr)
    # count_freq(arr, n)
    # count_total(arr, n)
    test_1(arr,n)