# calculate the arr repeated 
def arr_freq(arr, n):
    
    total = [False] * n 
    
    for i in range(n):
        
        if total[i] == True:
            continue
        count = 1
        
        for j in range(i + 1, n):
            
            if arr[i] == arr[j]:
                
                total[j] = True
                
                count += 1
        print(arr[i], count)


# find highest number 

def find_highest_num(arr,n):
    
    
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
        
        #   max value find
        if count > max_freq:
            max_freq = count
            max_elem = arr[i]
            
        # min value find
        if count < min_freq:
            min_freq = count
            min_elem = arr[i]

    print(max_elem, min_elem)
            


if __name__ == '__main__':
    arr = [5, 2, 2,2,2, 3, 3, 3]
    n = len(arr)
    find_highest_num(arr, n)