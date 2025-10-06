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
    
    
    
    """
    
    Solution 2: Space-optimized iterative method

Approach: Unlike the previous method we use the same array to obtain the result. Follow the steps below.

Keep a pointer p1  at the first index and another p2 at the last index of the array. 
Swap the elements pointed by p1 and p2, Post swapping increment p1 and decrement p2.
This process is repeated for only the first n/2 elements where n is the length of array.


Note: Swapping all the n elements instead of n/2 elements leaves the array unaltered.


"""


def swap_reverse(arr, n):
    
    for i in range(n):
        print(arr[i], end=" ")
    print
    
    
"""
Step-by-Step Explanation

- Initialize Two Pointers
p1 = 0          # points to the start of the array
p2 = n - 1      # points to the end of the array

These two variables are called pointers or indexes.
They will “move” toward each other while swapping elements.

If:

arr = [5, 4, 3, 2, 1]

then initially:

p1 → 0 (value = 5)
p2 → 4 (value = 1)

- Loop Until They Meet
while p1 < p2:

This means:
“Keep swapping elements while the left pointer (p1) is before the right pointer (p2).”

As soon as they meet or cross, the array is completely reversed.

- Swap the Elements

[p1], arr[p2] = arr[p2], arr[p1]
This is Python’s tuple swapping shorthand.


- Move the Pointers

p1 += 1
p2 -= 1

Example Dry Run

Let’s trace with:

arr = [5, 4, 3, 2, 1]

Step	p1	p2	arr[p1]	arr[p2]	After swap → arr	Action
1	0	4	5	1	[1, 4, 3, 2, 5]	p1=1, p2=3
2	1	3	4	2	[1, 2, 3, 4, 5]	p1=2, p2=2
3	2	2	(same)	(same)	Stop (p1 == p2)	—

ummary
Line	                                Meaning

p1 = 0; p2 = n - 1	                    Start at both ends
while p1 < p2:	                        Keep swapping until they meet
arr[p1], arr[p2] = arr[p2], arr[p1]	    Swap front ↔ back
p1 += 1; p2 -= 1	                    Move inward
printArray(arr, n)	                    Print reversed array


"""
def swap_reverse_1(arr, n):
    
    
    p1 = 0 # strt start
    p2 = n -1 # start end
    
    while p1 < p2: 
        arr[p1], arr[p2] = arr[p2], arr[p1]
        
        p1 += 1
        p2 -=1
    swap_reverse(arr, n)



if __name__ == "__main__":
    print("Swapt________")
    arr = [9,1,4,5]
    n = len(arr)
    swap_reverse_1(arr, n)
    
    
    
    
def swap_reverse(arr, n):
    
    for i in range(n):
        print(arr[i], end=" ")
    print
    
    
def lib_reverse(arr,n):
    arr.reverse()


if __name__ == "__main__":
    print("Swapt______w__")
    arr = [9,1,4,5,1]
    n = len(arr)
    swap_reverse(arr, n)
    lib_reverse(arr, n)

    

    
     #function to print array
def printArray(arr, n):
    print("The reversed array is:- ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    arr.reverse()


# Driver Code
if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)
    printArray(arr, n)

    



# library method
