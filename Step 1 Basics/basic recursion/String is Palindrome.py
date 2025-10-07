# easy way 

def is_palindrome(name):
    
    name = name.replace(" ", "").lower()   # remove the space and make lower case
    
    # Compare the string with its reverse
    return name == name[::-1]  # check condition == and ::-1 reverse string


text = input("Enter a string: ")
if is_palindrome(text):
    print("The given string is a palindrome.")
else:
    print("The given string is not a palindrome.")
    
    
    
    
    
    # used recursion
def recursion_palindrome(s):
    
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()  
    
    if len(s) <= 1:      # Base case: if string is empty or has one character, it's a palindrome
        return True
    
    # Recursive case: check first and last characters, then the substring in between
    if s[0] == s[-1]:
        return recursion_palindrome(s[1:-1])
    else:
        return False
    



text = input("enter string")

if recursion_palindrome(text):
    print("palindrome")
else:
    print("not")