# def divsiors(n=36):
#     divisors = []
#     for i in range(1, n + 1):
        
#         if n % i == 0:
#             divisors.append(i)
#     return print(divisors)
    
# divsiors()





def divisors(n=300):   # n value is 300 find this divisors all
    
    
    divisor = [] # all divisor append in list 
    
    for i in range(1, n + 1):   # for loops a used range and inc ++1 ex (1%300=0) append 1 in divisor same repeated 
        
        if n % i == 0: # divsor condition n % i    i always increase 1.,2,3,5,6,    
            
            divisor.append(i) # condition is true then append in list 1,2,3,4....
            
    return print(divisor) # and print

divisors()



# def divisors(self, n):

#         div = []

#         for i in range(1, n + 1):

#             if n % i == 0:
#                 div.append(i)
#         return print(div)
    
    
# divisors(n = 12)
    
class MathOps:
    def divisors(self, n):
        div = []
        for i in range(1, n + 1):
            if n % i == 0:
                div.append(i)
        return div


m = MathOps()
print(m.divisors(12))  # [1, 2, 3, 4, 6, 12]
