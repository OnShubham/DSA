

def last_small(num, n):
    
    if n == 0 or n == 1:
        
        print(-1, -1)
        return
    
    
    num.sort()
    
    small = num[1]
    
    
    large = num[n - 2]


    print("Second smallest is", small)
    print("Second largest is", large)
    
    
def large_small(num,n):
    
    if n == 0 or n == 1:
        
        print(-1, -1)
        
        return
        
    small = float('inf')
    secound_small = float('inf')
    larg = float('-inf')
    secound_larg = float('-inf')


    # Find the smallest and largest 

    for i in range(n):
        
        small = min(small, num[i])
        larg = max(larg, num[i])
        
    # second smallest and second largest elements


    for i in range(n):
        
        if num[i] < secound_small and num[i] != small:
            secound_small = num[i]
            
        if num[i] > secound_larg and num[i] != larg:
            secound_larg = num[i]
            

    print("Second smallest is", secound_small)
    print("Second largest is", secound_larg)

    
    



def large_small_1(num, n):
    
    if n == 0 and n == 1:
        print(-1, -1)
        return
    
    small = float('inf')
    secound_small = float('inf')
    large = float('-inf')
    secound_larg = float('-inf')
    
    for i in range(n):
        
        small = min(small, num[i])
        large = max(large, num[i])
        
    
    for i in range(n):
        
        if num[i] < secound_small and small != num[i]:
            secound_small = num[i]
        if num[i] > secound_larg and large != num[i]:
            secound_larg = num[i]
            
        
    print("Second smallest is", secound_small)
    print("Second largest is", secound_larg)
        



def practice(num, n):
    
    if num == 0 and num == 1:
        print(-1, -1)
        return
    
    
    sm = float('inf')
    ssm = float('inf')
    lg = float('-inf')
    slg = float('-inf')
    
    
    
    # find small and large 
    
    
    for i in range(n):
        
        sm = min(sm, num[i])
        lg = max(lg, num[i])
        
    
    
    #find secound last and small
    for i in range(n):
        
        if num[i] < ssm and sm != num[i]:
            ssm = num[i]
        if num[i] > slg and lg != num[i]:
            slg = num[i]
            
            
    print("small", ssm)
    print("large", slg)
    


if __name__ == "__main__":
    

    num = [0, 2, 4, 7, 7, 5]
    n = len(num)
    large_small_1(num, n)
    




    

    
    # Function to find the second smallest and second largest elements in the array
def getElements(arr, n):
    # Edge case: when the array has less than 2 elements
    if n == 0 or n == 1:
        print(-1, -1)  # Print -1 for both second smallest and second largest
        return

    # Initialize variables to track the smallest, second smallest, largest, and second largest elements
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')

    # Find the smallest and largest elements in the array
    for i in range(n):
        small = min(small, arr[i])  # Update the smallest element
        large = max(large, arr[i])  # Update the largest element

    # Find the second smallest and second largest elements
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]  # Update second smallest if a smaller element is found
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]  # Update second largest if a larger element is found

    # Output the second smallest and second largest elements
    # print("Second smallest is", second_small)
    # print("Second largest is", second_large)

# Driver code
if __name__ == "__main__":
    n = 6
    arr = [1, 2, 4, 6, 7, 5]  # Array of elements
    
    # Call the function to find and print the second smallest and second largest elements
    getElements(arr, n)