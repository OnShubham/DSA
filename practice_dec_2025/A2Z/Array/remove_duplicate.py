def remove_duplicate(arr, n):
    
    if not arr:
        return 0
    
    
    i = 0
    
    for j in range(1, n):
        
        if arr[j] != arr[i]:
            
            i +=1
            
            arr[i] = arr[j]
            
    k = i + 1
    
    print(k)
    print(arr[:k])


def remove_duplicate_1(arr,n):
    
    if not arr:
        return 0
    
    i = 0
    
    for j in range(1,n):
        
        if arr[j] != arr[i]:
            i += 1
            
            arr[i] = arr[j]
    k = i + 1
    
    print(k)
    print(arr[:k])




def remove_duplicate_3(arr,n):
    
    if not arr:
        return 0
    
    i = 0
    
    for j in range(1, n):
        
        if arr[j] != arr[i]:
            
            i += 1
            
            arr[i] = arr[j]
            
        
        
    k = i + 1
        
    print(k)
    print(arr[:k])
            
            

def remove_duplicate_test(arr,n):
    
    if not arr:
        return 0
    
    i = 0 
    
    for j in range(1, n):
        
        if arr[j] != arr[i]:
            
            i += 1
            
            arr[i] = arr[j]
            
    
    
    k = i + 1
    
    print(k)
    
    print(arr[:k])


if __name__ == "__main__":

    arr = [0, 2, 4, 7, 7, 5]
    n = len(arr)
    k = remove_duplicate_test(arr, n)

