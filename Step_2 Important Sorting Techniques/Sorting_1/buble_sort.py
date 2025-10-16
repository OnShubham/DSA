"""

Nice — thanks for sharing your code. I’ll explain **every part**, point out the bugs, give a **corrected version**, and then walk through the corrected algorithm step-by-step on your example `[7, 4, 1, 5, 3]`.

# What's happening in your code (line-by-line)

```python
def bubble_sort(nums):
    n = len(nums)
```

* `n` stores the number of elements. We need this for loop bounds.

```python
    for i in range(n - 1):
```

* Outer loop runs `n-1` passes. After each complete pass the largest remaining unsorted element ends up at its correct place on the right.
* `i` counts how many passes we've completed (0-based). After `i` passes, the last `i` elements are already sorted.

```python
        swapped = False
```

* `swapped` is a boolean flag used to detect if the current pass made any swaps.
* If no swaps happened in a pass, the array is already sorted and we can stop early (optimization).

```python
        for j in range(0, n - 1 - 1):
```

* **This is a bug.** The intent was to limit the inner loop so it doesn't compare already-sorted elements at the end.
* Correct bound should be `range(0, n - i - 1)` so `j` goes from `0` to `n-i-2`.
* Your current `n - 1 - 1` equals `n-2` and **does not** shrink with `i`. Also `range` upper bound is exclusive, so using `n-2` makes inner loop incorrect and too short.

```python
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
```

* Compare adjacent pair `(nums[j], nums[j+1])`. If left is greater, swap them.
* Set `swapped = True` to indicate a swap occurred.

```python
            if not swapped:
                break
```

* **Indentation bug**: This `if not swapped: break` is inside the inner loop in your code, so it checks and possibly breaks out of the inner loop *after the very first comparison* where no swap has yet been made. That prematurely ends the pass.
* The correct behavior is to check `if not swapped: break` **after finishing the inner loop** (i.e., outside the inner loop but inside the outer loop). That means "if the whole pass made no swaps, stop the algorithm."

```python
    return nums
```

* Return the (now sorted) list.

# Corrected implementation

```python
def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        # Compare up to the last unsorted element (n - i - 1)
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        # If no swaps happened in this pass, list is sorted — stop early
        if not swapped:
            break
    return nums

print(bubble_sort([7, 4, 1, 5, 3]))  # -> [1, 3, 4, 5, 7]
```

# Why each part is needed (short summary)

* `n = len(nums)`: know how many elements.
* `for i in range(n-1)`: do up to `n-1` passes; after each pass one more final element is in place.
* `for j in range(0, n-i-1)`: compare adjacent elements only in the unsorted portion (shrink the range as `i` grows).
* `if nums[j] > nums[j+1]: swap`: this is the core bubble step that moves larger elements right.
* `swapped` flag + `if not swapped: break`: optimization to end early if array becomes sorted before all `n-1` passes.

# Step-by-step run on [7, 4, 1, 5, 3]

We use the corrected code. I’ll show each pass and each comparison/swap.

Initial: `[7, 4, 1, 5, 3]`, `n = 5`

**Pass 0 (i = 0)** — inner loop `j` from 0 to `n-i-2 = 3` (j = 0..3)

* j=0: compare 7 and 4 → 7 > 4 → swap → `[4, 7, 1, 5, 3]` (swapped=True)
* j=1: compare 7 and 1 → 7 > 1 → swap → `[4, 1, 7, 5, 3]`
* j=2: compare 7 and 5 → 7 > 5 → swap → `[4, 1, 5, 7, 3]`
* j=3: compare 7 and 3 → 7 > 3 → swap → `[4, 1, 5, 3, 7]`
  End of pass 0: largest element `7` is now at index 4 (correct).

**Pass 1 (i = 1)** — j = 0..2

* j=0: compare 4 and 1 → 4 > 1 → swap → `[1, 4, 5, 3, 7]`
* j=1: compare 4 and 5 → 4 <= 5 → no swap → `[1, 4, 5, 3, 7]`
* j=2: compare 5 and 3 → 5 > 3 → swap → `[1, 4, 3, 5, 7]`
  End of pass 1: element `5` is at index 3 (correct).

**Pass 2 (i = 2)** — j = 0..1

* j=0: compare 1 and 4 → 1 <= 4 → no swap
* j=1: compare 4 and 3 → 4 > 3 → swap → `[1, 3, 4, 5, 7]`
  End of pass 2: element `4` is at index 2 (correct).

**Pass 3 (i = 3)** — j = 0..0

* j=0: compare 1 and 3 → 1 <= 3 → no swap
  End of pass 3: `swapped` remained `False` for the whole pass → the `if not swapped: break` triggers → algorithm stops early.

Final: `[1, 3, 4, 5, 7]`

# Complexity

* Time: worst-case (O(n^2)) (e.g., reverse-sorted).
* Best-case (already sorted) with the `swapped` optimization: (O(n)) — we do one pass, detect no swaps, break.
* Space: (O(1)) in-place.

# Summary of bugs in your original code

1. Inner loop bound was `range(0, n - 1 - 1)` (i.e., `n-2`) — it should depend on `i`: `range(0, n - i - 1)`.
2. `if not swapped: break` was indented inside inner loop — it must be outside the inner loop, checked once per pass.
3. Minor typos in comments (harmless, but fix for clarity).

---

If you want, I can:

* Add more comments inline in the code.
* Show a visualization (table of array states) for a different input.
* Convert this to a version that counts swaps or comparisons for analysis. Which would you like next?




"""



def bubble_sort(nums):
    
    n = len(nums)
    
    
    for i in range(n - 1):
        
        swapped = False
        
        for j in range(0, n - i - 1):
            
            # swap if eleements are is wrong order 
            
            if nums[j] > nums[j + 1]:
                
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                
                swapped = True
            
        if not swapped:
            break
            
    return nums
            




def bubble_sort_2(nums, n):
    
    
    for i in range(n - 1):
        
        swapped = False
        
        for j in range(0, n - i - 1):
            
            if nums[j] > nums[j + 1]:
                
                nums[j] , nums[j+1] = nums[j+1], nums[j]
                
                swapped = True
                
        
        
        if not swapped:
            break
        
        
    return print(nums)




def bubble_sort_3(num,n):
    
    for i in range(n - 1):
        
        Swap = False
        
        for j in range(0, n - i - 1):            
        
            if num[j] > num[j + 1]:
                
                num[j], num[j + 1] = num[j + 1],num[j]
                
                Swap = True
                
            
        if not Swap:
            break
    
    
    return print(num, "test_3")
            
            
    
    
# test for know
def back_arr(num):
    
    n = len(num)
    
    for i in range(n):
        
        print(num[i], end=" ")
    print()




def bubble_sort_last_practice(num,n):
    
    for i in range(n - 1):
        
        swap = False
        
        for j in range(0, n - i - 1):
            
            if num[j] > num[j + 1]:
                
                num[j], num[j + 1] = num[j + 1], num[j]
                
                swap = True
                
        if not swap:
            break
        
    return print(num, "last")




def buble_sort_next_day(num,n):
    
    for i in range(n - 1):
        
        swap = False
        
        
        for j in range(0, n - i - 1):
            
            if num[j] > num[j + 1]:
                
                num[j] , num[j + 1] = num[j + 1], num[j]
                
                swap = True
                
        
        if not swap:
            break
        
    return print(num)
                
                
                
                







if __name__ == "__main__":
    nums = [3,4,2,4,1,5,2]
    n = len(nums)
    num = [3,4,2,4,1,5,2]
    n = len(num)
    
    
    # back_arr([2,3,1,2,3])
    buble_sort_next_day(num,n)
    # bubble_sort_last_practice(num,n)
    # bubble_sort_2(nums, n)
    # bubble_sort_3(num,n)
    # print(bubble_sort([7, 4, 1, 5, 3]))  