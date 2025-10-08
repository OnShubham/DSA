def sort_the_peopale(name,height,n):
    
    for i in range(n - 1):
        index = i 
        
        
        for j in range(i + 1, n):
            
            if height[j] > height[index]:
                index = j 
                
        
        height[i] , height[index] = height[index], height[i]
        
        
        

    
    

name = ["om", "renuka", "shubham"]
height = [185, 180, 190 ]
n = len(height)
sort_the_peopale(name,height,n)