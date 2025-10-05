def num( n):
    
    if n == 0:
        return
    
    num( n - 1)
    print(n)
    
num(4)

print("next")

def print_1_to_n(n):
    # Base case: stop when n == 0
    if n == 0:
        return
    
    # First, recursively print all numbers before n
    print_1_to_n(n - 1)
    
    # Then print n itself
    print(n)

# Example:
print_1_to_n(5)



"""

Explanation (Step-by-step for n = 5)

print_1_to_n(5) calls print_1_to_n(4)

print_1_to_n(4) calls print_1_to_n(3)

print_1_to_n(3) calls print_1_to_n(2)

print_1_to_n(2) calls print_1_to_n(1)

print_1_to_n(1) calls print_1_to_n(0) → base case → returns

Now the call stack unwinds, printing:

1
2
3
4
5

🔍 Key Idea

The recursion first goes down until n == 0.

Then, as the function returns (unwinds), it prints the numbers in increasing order.


"""