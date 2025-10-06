# function to print array
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] = arr[i]
    printArray(ans, n)


# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)


  


def rever_num (n = 123):
    
    cnt = 0 
    
    while n > 0:
        
        last_digit = n % 10 
        
        cnt = cnt * 10 + last_digit
        
        n = n // 10 
        
    return print("number :", cnt)
rever_num()



def fact_num(n):
    
    if n == 1:
        return 1
    return n * fact_num(n - 1)

n = 5

print(fact_num(n))



