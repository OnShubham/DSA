
def merger(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merger(arr[mid:])
    right = merger(arr[:mid])
    
    return merer_2(left, right)

def merer_2(left, right):
    
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



def buble_sort(arr,n):
    
    if n == 1:
        return
    
    for i in range( n - 1):
        
        if arr[i] > arr[i + 1]:
            
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    
    buble_sort(arr,n - 1)




def merger(arr):
    
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    
    left = merger(arr[mid:])
    right = merger(arr[:mid])
    
    return merg(left, right)

def merg(left, right):
    
    result = []
    
    i = j = 0
    
    for i in range(n - 1):
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                
                result.append(left[i])
                
                i += 1
                
            else:
                result.append(right[j])
                
                i += 1
                
    
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
    
    


if __name__ == "__main__":
    
    arr = [2,3,2,1,4,5,2,1,2,3,3,4]
    n = len(arr)
    buble_sort(arr,n)
    print("buble", arr)
    a = merger(arr)
    print("test :", a)
    
    
    
    
    
    