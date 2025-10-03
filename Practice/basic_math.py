def count(n = 12342):
    
    count = 0
    
    while n > 0:
        
        n = n // 10 
        
        count += 1
        
    return print(count)

count()

def reverse_num(n = 123):
    
    rev = 0
    
    while n > 0:
        
        last_digit = n % 10 
        
        rev = rev * 10 + last_digit
        
        n = n // 10 
        
    return print(rev)
        
reverse_num()


def check_palindrome(n = 1):
    
    rev = 0
    orignal = n
    
    while n > 0:
        
        last_digit = n % 10 
        
        rev = rev * 10 + last_digit
        
        n = n // 10 
        
    if orignal == rev:
        print("true")
    else:
        print("false")
        
check_palindrome()


def gcd(n1,n2):
    
    while n2 != 0:
        
        n1,n2 = n2, n1 % n2
        
    return print(n1)

n1 = 12
n2 = 22
gcd(n1,n2)


def Armstrong_number(n = 153):
    
    leng = len(str(n))
    total = 0
    orignal = n
    
    for i in range(1, n + 1):
        
        last_digit = n % 10
        
        total += last_digit ** leng
        
        n = n // 10
        
    if orignal == total:
        print("true")
    else:
        print("false")
        
Armstrong_number()


def divisor_num(n = 200):
    
    div = []
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            
            div.append(i)
    return print(div)
        
divisor_num()


def check_prime(n = 123):
    
    cnt = 0
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            
            cnt += 1
            
    if cnt == 2 :
        
        print("true")
        
    else:
        print("false")
        
check_prime()