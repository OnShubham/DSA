def left_rotate(nums,k):
    
    n = len(nums)
    k = k % n
    
    def reverse(arr, start, end):
        while start < end:
            
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
            
            
    
    
    reverse(nums, 0, k - 1)
    
    reverse(nums, k , n - 1)
    
    reverse(nums, 0, n - 1)
    
nums = [1, 2, 3, 4, 5]
k = 4
left_rotate(nums, k)
print(nums)