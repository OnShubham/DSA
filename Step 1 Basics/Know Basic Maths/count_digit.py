def count_digit(n):
    
    count = 0
    
    while n > 0 :
        
        n = n // 10    # remove the last digit from n
        
        count += 1
        
    print(count)
    
n = 151655
count_digit(n)



"""
    This function counts how many digits are in a given integer 'n'.
    
    Logic:
    ------
    1. Start with a counter (count = 0).
    2. Use a while loop that continues until 'n' becomes 0.
    3. In each loop iteration:
        - Remove the last digit of 'n' using integer division (// 10).
          Example: 151655 // 10 = 15165
        - Increase the counter by 1.
    4. When 'n' finally becomes 0, the loop stops.
    5. The counter now represents the total number of digits in the original number.
    
    Example Walkthrough:
    --------------------
    Let’s take n = 151655
    
    - First loop:
        n = 151655 // 10 = 15165
        count = 1
    - Second loop:
        n = 15165 // 10 = 1516
        count = 2
    - Third loop:
        n = 1516 // 10 = 151
        count = 3
    - Fourth loop:
        n = 151 // 10 = 15
        count = 4
    - Fifth loop:
        n = 15 // 10 = 1
        count = 5
    - Sixth loop:
        n = 1 // 10 = 0
        count = 6
    
    Loop ends since n = 0.
    Final count = 6 → which means the number 151655 has 6 digits.

"""