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
            








def find_count_num(arr,n):
    
    empty = [False] * n
    max_freq = 0
    min_freq = n + 1
    max_ele = None
    min_ele = None
    
    for i in range(n):
        
        if empty[i] == True:
            continue
        
        count = 1
        
        for j in range(i + 1, n):
            
            if arr[j] == arr[i]:
                
                empty[j] = True
                
                count += 1
                
        
        
        if count > max_freq:
            max_freq = count
            max_ele = arr[i]
            
        if count < min_freq:
             
            min_freq = count
            min_ele = arr[i]
            
        
    print(min_ele, max_ele)







if __name__ == '__main__':
    arr = [5, 2, 2,2,2, 3, 3, 3]
    n = len(arr)
    find_count_num(arr, n)
    
    
    
    
    
    
    
    
def count_num(arr, n):
    
    visited = [False] * n
    
    for i in range(n):
        
        if visited[i] == True:
            
            continue
        
        count = 1
        
        for j in range(i + 1, n):
            
            if arr[j] == arr[i]:
                
                visited[j] = True
                
                count += 1
                
        print(arr[i], count)

if __name__ == '__main__':
    
        
    arr = [1,2,3]
    n = len(arr)
    count_num(arr, n)