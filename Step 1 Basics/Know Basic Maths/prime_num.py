def prime_num(n = 2):
    
    length = len(str(n))
    cnt = 0
    
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            
            cnt += 1
            
    if cnt == 2:
            print("t")
    else:
            print("n")
            
prime_num()
        
    
    