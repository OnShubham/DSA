def decresion_num(n):
    
    if n == 0:
        return
    
    print(n)
    
    decresion_num(n - 1)
decresion_num(5)


def print_n_to_1(n):
    # Base case: stop when n == 0
    if n == 0:
        return
    
    # Print the current number first
    print(n)
    
    # Then recursively print the rest
    print_n_to_1(n - 1)

# Example:
print_n_to_1(5)



"""
🧠 How It Works (for n = 5)
Function Call	What Happens	Output
print_n_to_1(5)	prints 5, calls print_n_to_1(4)	5
print_n_to_1(4)	prints 4, calls print_n_to_1(3)	4
print_n_to_1(3)	prints 3, calls print_n_to_1(2)	3
print_n_to_1(2)	prints 2, calls print_n_to_1(1)	2
print_n_to_1(1)	prints 1, calls print_n_to_1(0)	1
print_n_to_1(0)	base case reached → stop	—

✅ Output:

5
4
3
2
1

🔍 Hint 1 (Conceptual)

In recursion, the position of the print statement determines the order:

Before the recursive call → prints in decreasing order

After the recursive call → prints in increasing order

Would you like me to show a combined version that can print both 1→N and N→1 depending on a flag (like reverse=True)?

"""