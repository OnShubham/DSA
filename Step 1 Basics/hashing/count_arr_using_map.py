def count_arr_using_map(arr,n):
    
    map = {}
    
    for i in range(n):
        
        if arr[i] in map:
            
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
            
    for x in map:
        
        print(x, map[x])



if __name__ == '__main__':
    arr = [10, 5, 10, 15, 10, 5]
    n = len(arr)
    count_arr_using_map(arr, n)
