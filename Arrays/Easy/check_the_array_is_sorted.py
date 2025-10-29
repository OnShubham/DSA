def check_arr_sorted(arr, n):
    
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                return print("False")
    
    
    return print("true")
  
    



def check_arr_sorted_2(arr,n):
    
    for i in range(n):
        
        for j in range(i + 1, n):
            
            if arr[j] < arr[i]:
                
                return print(arr[j],arr[i],"fasle")
            
    return print("true")

if __name__ == "__main__":
    arr = [1,2]
    x = arr
    n = len(arr)
    # larget_num(arr, n)
    check_arr_sorted_2(arr, n)