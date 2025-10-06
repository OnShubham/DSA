# normal fact number 

def fact_num_loop(n):
    
    fact = 1 
    
    for i in range(1, n + 1):
        
        fact *= i
        
    return print(fact)

fact_num_loop(5)


def fact_num_recursion(n):
    
    if n == 1:
        return 1
    
    return n * fact_num_recursion(n - 1)
n = 5
print(fact_num_recursion(n))


def factorial_recursive(X):
    if X == 1:
        return 1
    return X * factorial_recursive(X - 1)

# Example
X = 5
print("Factorial (Recursive):", factorial_recursive(X))



"""
Explanation:

Base case: 1! = 1

Recursive case: X! = X * (X-1)!

Time Complexity: O(X)
Space Complexity: O(X) — due to recursion call stack

"""