def larget_num(arr,n):
    
    for i in range( n - 1):
        
        last = i 
        
        for j in range(i + 1 , n):
            
            if arr[j] < arr[last]:
                
                
                last = j
        
        arr[i] , arr[last] = arr[last], arr[i]
        
    
    print("last", arr[-1])
        
        
    
    
    
    
    
    
def larget_num_2(arr):
    
    
    for i in range(n - 1):
        
        last = i
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[last]:
                
                last = j
                
        
        
        arr[i], arr[last] = arr[last], arr[i]
        
    
    print("Largest Number", arr[-1])
    


def last_num(arr,n):
    
    
    
    for i in range(n - 1):
        
        last = i
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[last]:
                
                last = j
                
        
        
        arr[i], arr[last] = arr[last], arr[i]
        
        
    return print(arr[-1])






def lart_num(arr,n):
    
    for i in range(n - 1):
        
        last = i 
        
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[last]:
                
                last = j
                
        
        
        arr[i] , arr[last] = arr[last] , arr[i]
        
    
    
    return print(arr[-1])



if __name__ == "__main__":
    arr = [2,5,1,3,0]
    n = len(arr)
    larget_num(arr, n)
    larget_num_2(arr)
    last_num(arr,n)
    lart_num(arr,n)
    
    

