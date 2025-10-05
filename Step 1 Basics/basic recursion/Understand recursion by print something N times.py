def print_n_times(message, n):
    # Base case: stop when n == 0
    if n == 0:
        return
    
    # Print the message
    print(message)
    
    # Recursive call with n-1
    print_n_times(message, n - 1)

# Example use:
print_n_times("Hello, recursion!", 5)


"""
print_n_times("Hi", 3)
→ prints "Hi"
→ calls print_n_times("Hi", 2)
    → prints "Hi"
    → calls print_n_times("Hi", 1)
        → prints "Hi"
        → calls print_n_times("Hi", 0)
            → stops (base case)
            
            🧠 Concept

To print something 
𝑁
N times recursively:

If 
𝑁
=
0
N=0, stop — that’s our base case.

Otherwise:

Print the message once.

Then call the same function again with 
𝑁
−
1
N−1.

"""
