"""
Problem: Number of Divisors

You are given a positive integer n. 
Your task is to return all the divisors of n 
in ascending order.

A divisor of an integer n is any integer 
i such that n % i == 0.

---

Example 1:
Input: n = 12
Output: [1, 2, 3, 4, 6, 12]

Example 2:
Input: n = 25
Output: [1, 5, 25]

---

Constraints:
1 <= n <= 10^4
"""


def divisor_num(n):
    
    arr = []
    
    for i in range(1, n + 1):
        
        if n % i == 0:
            arr.append(i)
            
    return print(arr)
        

            


if __name__ == "__main__":
    print(divisor_num(12))   
    print(divisor_num(25))  
