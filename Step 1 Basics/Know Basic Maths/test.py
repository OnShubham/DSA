#  Divisors of a Number
def Divisors(n = 555):
    
    num = []
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            num.append(i)
    return print(num)
Divisors()

# Check if a number is Armstrong Number or not

def Armstrong(n = 55):
    
    lenght = len(str(n))
    total = 0
    ori = n
    
    while n > 0:
        
        last_digit = n % 10
        
        total += last_digit ** lenght
        
        n = n // 10 
        
    if ori == total:
        print("t")
    else:
        print("f")
        
Armstrong()
        
        
        
# Check if a number is prime or not

def prime_num(n = 1483):
    

    cnt = 0
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            
            cnt += 1
            
    if cnt == 2:
        
        print("True")
        
    else:
        
        print("False")
        
prime_num()

# def prime_num(n=1483):
#     # Prime numbers are greater than 1
#     if n < 2:
#         print("False")
#         return

#     cnt = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             cnt += 1

#     # A prime number has exactly 2 divisors: 1 and itself
#     if cnt == 2:
#         print("True")
#     else:
#         print("False")


# prime_num()

        