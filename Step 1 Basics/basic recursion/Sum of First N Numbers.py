# def sum(n):
    
#     cal = 0
    
#     if n == 0:
#         return
    
#     sum(n - 1)
    
#     print(n)
    
# sum(5)


def sum_of_n(n):
    # Base case: when n == 0, the sum is 0
    if n == 0:
        return 0
    
    # Recursive case:
    # sum of first n numbers = n + sum of first (n-1) numbers
    return n + sum_of_n(n - 1)

# Example:
print(sum_of_n(4))  # Output: 10

    
    

"""
Perfect — this is another classic recursion exercise!
Let’s find the **sum of the first N natural numbers** using recursion.

---

### ✅ **Python Solution**

```python
def sum_of_n(n):
    # Base case: when n == 0, the sum is 0
    if n == 0:
        return 0
    
    # Recursive case:
    # sum of first n numbers = n + sum of first (n-1) numbers
    return n + sum_of_n(n - 1)

# Example:
print(sum_of_n(4))  # Output: 10
```

---

### 🧠 **Step-by-Step Example (N = 4)**

```
sum_of_n(4)
= 4 + sum_of_n(3)
= 4 + (3 + sum_of_n(2))
= 4 + (3 + (2 + sum_of_n(1)))
= 4 + (3 + (2 + (1 + sum_of_n(0))))
= 4 + (3 + (2 + (1 + 0)))
= 10
```

✅ **Output:** `10`

---

### ⚙️ **Explanation**

| Step | Function Call | Returns      |
| ---- | ------------- | ------------ |
| 1    | `sum_of_n(1)` | `1`          |
| 2    | `sum_of_n(2)` | `2 + 1 = 3`  |
| 3    | `sum_of_n(3)` | `3 + 3 = 6`  |
| 4    | `sum_of_n(4)` | `4 + 6 = 10` |

---

### 🧩 **Formula Check**

The formula for the sum of first N natural numbers is:

[
\text{Sum} = \frac{N \times (N + 1)}{2}
]

For `N = 4` → `4 * 5 / 2 = 10`, which matches our recursive result ✅

---

Would you like me to show the **trace of recursive calls** (how the call stack expands and collapses)?


"""
    