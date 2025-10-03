# def armstrong_num(n = 1634):
    
#     sum = 0
    
#     while n > 0:
        
    
#         last_digit = n % 10
        
#         sum = sum + (last_digit * last_digit * last_digit)
        
#         n = n // 10
        
#     return print(n)
    
# armstrong_num()


def armstrong_num(n = 55):
    
    total = 0
    num_digit = len(str(n))
    original = n
    
    while n > 0:
        
    
        last_digit = n % 10
        
        total += last_digit ** num_digit
        
        n = n // 10
        
    if total == original:
        print(f"{original} is an Armstrong Number")
    else:
        print(f"{original} is an Armstrong Not Number")
        
        
   
    
armstrong_num()



def Armstrong(n = 1634):
    
    number = 0
    lenght = len(str(n))
    orign = n
    
    while n > 0:
        
        last_digit = n % 10
        
        number += last_digit ** lenght
        
        n = n // 10
        
    if orign == number:
        print(True)
    else: 
        print(False)
   
Armstrong()