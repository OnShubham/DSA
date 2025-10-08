

def sort_freq(nums,n):
    
    # index = []
  
    
    # for i in range(n):
    #     print(nums[i], end=" " )
    # print()
    #     count = 1

    #     for j in range(i + 1, n):
    
    
    index = [False] * n 
    
    for i in range(n):
        
        if index[i] == True:
            continue
        
        count = 1
        
        for j in range(i + 1, n):
            
            if nums[i] == nums[j]:
                
                index[j] = True
                
                count += 1
                
                
        # print(nums[i])
        
        for i in range( n - 1):
            
            
            
            
            
    
    
    


if __name__ == "__main__":
    nums = [5,6,8,7,5,8,9]
    n = len(nums)
    sort_freq(nums,n)