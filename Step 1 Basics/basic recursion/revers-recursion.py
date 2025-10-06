"""
Solution 1: Using an extra array.

Approach: Declare an array,ans[] of the same size as the input array. Iterate from the back of the input array while storing the elements in ans[]  in opposite direction.

"""

def printArray(arr, n):
    
    for i in range(n):
        print(arr[i], end=" ")
    print()
    
def reverseArray(arr, n):
    
    ans = [0] * n
    
    for i in range(n - 1, -1,-1):
        ans[n -i -1] == arr[i]
    printArray(arr, n)
    
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)
    
    
"""
the for loop

for i in range(n - 1, -1, -1):


Let’s unpack this:

range(start, stop, step) → generates numbers starting from start, stopping before stop, with a step of step.

Here:

start = n - 1 → last index of the array (for n = 5, that’s 4)

stop = -1 → go until just before -1 (so it includes 0)

step = -1 → count backward


"""

# [n - i - 1] convert backward index to forward position

# ans[n - i - 1] = arr[i] copy in reverse order

# arr[i] take element from the end of the original list


def Array(arr, n):
    
    for i in range(n):
        print(arr[i], end=" ")
    print()


def Array_2(arr,n):
    
    ans = [0] * n
    
    for i in range(n - 1, -1, -1):
        ans[n - i - 1] == arr[i]
        
    print("helllo",Array(ans, n))


arr = [2,3,1,4]
n = len(arr)
Array_2(arr, n)






# practice 

def practice(arr,n):
    
    for i in range(n):
        
        print(arr[i], end=" ")
        
    print()
    
def practice_1(arr, n):
    
    ans = [0] * n
    
    for i in range(n - 1, -1, -1):
        
        ans[n - i - 1] = arr[i]  # 
        
    practice(ans,n)



if __name__ == "__main__":
    arr = [3,1,4]
    n = len(arr)
    practice_1(arr, n)