def higher_number(arr,n):
    
    calculate = [False] * n
    max_freq = 0
    min_freq = n + 1
    max_elem = None
    min_elem = None

    
    for i in range(n):
        
        if calculate[i] == True:
            continue
        
        count = 1
        
        for j in range(i + 1, n):
            
            if arr[i] == arr[j]:
                
                calculate[j] = True
                
                count += 1
                
          # Compare frequencies to find max and min
          
        #   max value find
        if count > max_freq:
            max_freq = count
            max_elem = arr[i]
            
        # min value find
        if count < min_freq:
            min_freq = count
            min_elem = arr[i]

    print(max_elem, min_elem)

        
       
        
        
    
    



def test(arr,n):
    
    false_arr = [False] * n
    
    max_freq = 0
    min_freq = n + 1
    max_elem = None
    min_elem = None
    
    for i in range(n):
        
        if false_arr[i] == True:
            
            continue
        
        count = 1
        
        for j in range(i + 1, n):
            
            if arr[i] == arr[j]:
                
                false_arr[j] = True
                
                count += 1
        
        # print(arr[i], count)
        
        if count > max_freq:
            max_freq = count
            max_elem = arr[i]
            
            
        print(max_elem)
        

        



if __name__ == '__main__':
    arr = [5, 2, 2,2,2, 3, 3, 3]
    n = len(arr)
    test(arr, n)