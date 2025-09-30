def revers_number(n):
    
    rev = 0 # start with 0, this will hold the reversed number

    
    while n > 0: # loop until n becomes 0
        
        rev = rev * 10 + n % 10  # take the last digit of n and add it to rev
        
        n = n // 10   # remove the last digit from n
        
    return print(rev)
n = 857
revers_number(n)


"""
    This function reverses the digits of a given integer 'n'.
    
    Logic:
    ------
    1. Start with rev = 0 (this will store the reversed number).
    2. Use a while loop until n becomes 0.
    3. In each iteration:
        - Extract the last digit of n using (n % 10).
        - Append that digit to the reversed number by:
              rev = rev * 10 + (last digit)
          Example: if rev = 75 and last digit = 8 → rev = 75 * 10 + 8 = 758
        - Remove the last digit from n using integer division (n // 10).
    4. Continue until n = 0.
    5. The variable rev now holds the reversed version of the original number.
    
    Example Walkthrough:
    --------------------
    Input: n = 857
    
    Step 1: rev = 0, n = 857
        - last digit = 857 % 10 = 7
        - rev = 0 * 10 + 7 = 7
        - n = 857 // 10 = 85
    
    Step 2: rev = 7, n = 85
        - last digit = 85 % 10 = 5
        - rev = 7 * 10 + 5 = 75
        - n = 85 // 10 = 8
    
    Step 3: rev = 75, n = 8
        - last digit = 8 % 10 = 8
        - rev = 75 * 10 + 8 = 758
        - n = 8 // 10 = 0
    
    Loop ends since n = 0.
    Final reversed number = 758
   
   
    """
    
    
    
def revers_number_1(x):
    
    
    rev = 0 
    
    while x > 0:
        
        last_digit = x % 10  # this gives the last digit of x % 10 = 3
        
        rev = rev * 10 + last_digit # step 2 = 0 * 10 + 3
        
        x = x // 10 # 123 // 10 = 12 ( remove last number)
        
    return print(rev)
    
    
x = 123
revers_number_1(x)



# test


def rev(n = 567):
    
    num = 0
    
    while n > 0:
        
        last_num = n % 10
        
        num = num * 10 + last_num
        
        n = n // 10
        
    return print(num)


rev()