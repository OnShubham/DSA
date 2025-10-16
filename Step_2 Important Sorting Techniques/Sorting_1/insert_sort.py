def insert_sort(arr, n):
    
    for i in range(1, n):         # 1) take each element from index 1..n-1
        
        key = arr[i]              # 2) save the element to insert
        
        j = i - 1                 # 3) start comparing with the element just before i

        while j >= 0 and arr[j] > key:  # 4) while left element is larger than key
            
            arr[j + 1] = arr[j]         #    shift that larger element one position to the right
            
            j -= 1                      #    move left (continue comparing)
            
        arr[j + 1] = key                # 5) insert key into the vacated spot
        
    return print(arr)



def insert_sort_re(arr, n):
    
    for i in range(1, n):
        
        key = arr[i]
        
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            
            arr[j + 1 ] = arr[j]
            
            j -= 1
            
        arr[j + 1] = key
    return print(arr)
            




def insert_sort_test(arr, n):
    
    for i in range(1, n):
        
        key = arr[i]
        
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            
            arr[j + 1] = arr[j]
            
            j -= 1
            
        arr[j + 1] = key
    
    return print(arr)




def insert(num,n):
    
    for i in range(1, n):
        
        key = num[i]
        
        j = i -1
        
        while j >= 0 and num[j] > key:
            
            num[j + 1] = num[j]
            
            num -= 1
            
        num[j + 1] = key
    
    return print(num)

if __name__ == "__main__":
    
    arr = [13, 46, 24, 52, 20, 9]
    n = len(arr)
    insert_sort(arr, n)
    insert_sort_re(arr, n)
    insert_sort_test(arr, n)
    insert(arr, n)
    