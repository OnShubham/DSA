# revers numbre

def arr_num(arr,n):
    
    for i in range(n):
        print(arr[i], end=" ")
    print()
    
def arr_num_1(arr,n):
    
    ans = [0] * n
    
    for i in range(n - 1, -1, -1):
        
        ans[n - i - 1] = arr[i]
        
    arr_num(ans, n)
        
        
arr = [2,3,2,5,2,6,8,3,5]
n = len(arr)
arr_num_1(arr,n)






# swap arr reverse 

def arr_num(arr,n):
    
    for i in range(n):
        print(arr[i], end=" ")
    print()
    
def swap_arr(arr,n):
    
    p1 = 0
    p2 = n - 1
    
    
    while p1 < p2:
        
        p1[arr], p2[arr] = p2[arr], p1[arr]
        
        
        p1 += 1
        p2 -= 1
        
        
    arr_num(arr,n)
    


print("swap")
arr = [2,3,2,5,2,6,8,3,5]
n = len(arr)
arr_num_1(arr,n)