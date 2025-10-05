def print_name_n(name, n):
    
    for i in range(1, n + 1):
        print(name)
        
print_name_n("shubham", 5)


# recursion

def print_name(name, n):
    # Base case: stop when n == 0
    if n == 0:
        return
    
    # Print the name
    print(name)
    
    # Recursive call with n-1
    print_name(name, n - 1)

# Example:
print_name("Alice", 5)
