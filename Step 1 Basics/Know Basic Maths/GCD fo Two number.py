def GCD(n1,n2):
    
     # The loop keeps running until n2 becomes 0
    
    while n2 != 0:
        
         # Swap values:
        # - new n1 = old n2
        # - new n2 = old n1 % old n2 (remainder)
        n1, n2 = n2, n1 % n2
        
    # When n2 becomes 0, n1 holds the GCD
    return print(n1)

GCD(2,4)



"""

Step-by-step with comments in execution:

n1 = 2, n2 = 4
while 4 != 0 → True
→ n1, n2 = 4, 2 % 4 = 2

n1 = 4, n2 = 2
while 2 != 0 → True
→ n1, n2 = 2, 4 % 2 = 0

n1 = 2, n2 = 0
while 0 != 0 → False → stop loop

✅ Final Answer = n1 = 2

"""



def gcd_1(n,m):
    
    while m != 0:
        n , m = m , n % m
    return print(n)
gcd_1(2,6)


# m is not 0 
# n , m = 6, 2 % 6
# m is 2
# n, m = 2, 2 % 6
# m is 0
# stop loop

