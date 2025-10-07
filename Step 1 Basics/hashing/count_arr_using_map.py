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



# Function to count frequency of each element in an array using a dictionary (map)
def count_arr_using_map(arr, n):
    
    # Create an empty dictionary called 'map'
    # This will store elements as keys and their frequencies as values
    map = {}
    
    # Loop through each element in the array
    for i in range(n):
        
        # If the element already exists in the dictionary, increase its count by 1
        if arr[i] in map:
            map[arr[i]] += 1
        
        # If the element does not exist, add it to the dictionary with count = 1
        else:
            map[arr[i]] = 1
            
    # Loop through each key (element) in the dictionary
    for x in map:
        
        # Print the element and its frequency
        print(x, map[x])



# Main part of the program
if __name__ == '__main__':
    
    # Define the array
    arr = [10, 5, 10, 15, 10, 5]
    
    # Find the number of elements in the array
    n = len(arr)
    
    # Call the function to count and print frequencies
    count_arr_using_map(arr, n)
