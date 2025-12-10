def larget_num(num, n):
    
    for i in range(n - 1):
        
        last = i
        
        for j in range(i + 1, n):
            
            if num[j] < num[last]:
                
                last = j
                
        
        
        
        num[i], num[last] = num[last], num[i]
        
    
    print("last", num[-1])
    
    
    
    
    
def larget_num_2(num, n):
    
    
    for i in range(n - 1):
        
        last_num = i
        
        
        for j in range(i + 1 , n):
            
            
            if num[j] < num[last_num]:
                
                last_num = j
                
            
            
        num[i], num[last_num] = num[last_num], num[i]
        
        
    
    print("num", num[-2])
            
    
    
    
if __name__ == "__main__":
    

    num = [1,2,4,2,1,5,6,3]
    n = len(num)
    larget_num_2(num, n)
    
    
    
