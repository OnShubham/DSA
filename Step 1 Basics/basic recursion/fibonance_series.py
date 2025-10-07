"""
F(0) = 0  
F(1) = 1  
F(n) = F(n-1) + F(n-2)
"""

# easy way 

def fibonance(n):
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonance(n-1) + fibonance(n-2)
    
num = int(input("Enter"))

print(fibonance(num))


# using recursion


def recursion_fibo(n, a = 0, b = 1):
    
    if n <= 0:
        return
    
    print(a, end=" ")
    recursion_fibo(n-1,b,a+b)
    
inp = int(input("Number"))
recursion_fibo(inp)