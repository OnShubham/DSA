def palindrome(n):
    
    num = 0
    orignal = n
    
    while n > 0:
        
        
        num = num * 10 +  n % 10
        
        n = n // 10
        
    if orignal == num:
        return print("Palindrome Num :", num)
    else:
        return print("Not Palindrome Num :", num)
        

n = int(input())
palindrome(n)


"""
Input: 121

Reverse = 121 → matches original → prints y

Input: 123

Reverse = 321 → doesn’t match original → prints n

"""




# test


def palindrome_test(n = 55):
    
    rev = 0
    ori = n
    
    while n > 0:
        
        rev = rev * 10 + n % 10
        
        n = n // 10
        
    if ori == rev:
        print("true")
    else:
        print("false")
        
palindrome_test()