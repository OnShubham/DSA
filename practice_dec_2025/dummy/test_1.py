def larger_elemtn(arr, n):
    
    for i in range(n):
        
        last = i
        
        for j in range(i + 1, n):
            
            if arr[j] <= arr[last]:
                
                last = j
                
        
        arr[i], arr[last] = arr[last], arr[i]
        
        
    return print("last number :", arr[-1])



def find_larget_small_number(arr,n):
    
    if arr == 0 and arr == 1:
        print(-1,-1)
        return 

    small = float('inf')
    small_secound = float('inf')
    larger = float('-inf')
    larger_elemtn = float('-inf')
    
    
    for i in range(n):
        
        small = min(small, arr[i])
        larger = max(larger, arr[i])
        
    
    for i in range(n):
        
        if arr[i] < small_secound and arr[i] != small:
            small_secound = arr[i]
        if arr[i] > larger_elemtn and arr[i] != larger:
            larger_elemtn = arr[i]
        
        
    print("secound_larger :", small_secound)
    print("larger_elemtn :", larger_elemtn)
    
    
    

def find_larget_num(arr,n):
    
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[i] < arr[j]:
                
                return print(arr[i], arr[j], "false")
            
    
    return print("true")



if __name__ == "__main__":
    
    # Example array
    arr = [1,2,5,4]
    n = len(arr)
    
    # Call the function to check if the array is sorted
    larger_elemtn(arr, n)
    find_larget_small_number(arr,n)
    find_larget_num(arr,n)