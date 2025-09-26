
---

# 📌 Functions in Python – Pass by Reference vs Pass by Value

### ⚡ First, the Basics

* **Pass by Value**: A *copy* of the variable is passed to the function. Changes inside the function do **not** affect the original variable.
* **Pass by Reference**: A *reference (memory address)* is passed. Changes inside the function **do affect** the original variable.

👉 But in **Python**, it’s a little different:

* Python uses **Pass by Object Reference** (also called **Call by Sharing**).
* Immutable objects (like `int`, `str`, `tuple`) behave like *pass by value*.
* Mutable objects (like `list`, `dict`, `set`) behave like *pass by reference*.

---

## 📝 Example 1: Immutable (Pass by Value-like behavior)

```python
def change_number(x):
    x = 20
    print("Inside function:", x)

a = 10
change_number(a)
print("Outside function:", a)
```

**Output:**

```
Inside function: 20
Outside function: 10
```

---

### 🔎 Diagram – Immutable

```
a ---> 10
x ---> 10   (copy of reference)

Inside function: x reassigned ---> 20
But 'a' still ---> 10
```

✅ Since `int` is immutable, the function cannot modify the original variable.

---

## 📝 Example 2: Mutable (Pass by Reference-like behavior)

```python
def change_list(mylist):
    mylist.append(4)
    print("Inside function:", mylist)

lst = [1, 2, 3]
change_list(lst)
print("Outside function:", lst)
```

**Output:**

```
Inside function: [1, 2, 3, 4]
Outside function: [1, 2, 3, 4]
```

---

### 🔎 Diagram – Mutable

```
lst ---> [1, 2, 3]
mylist ---> [1, 2, 3]  (points to the same list)

Inside function: mylist.append(4)
lst ---> [1, 2, 3, 4]  (changed for both)
```

✅ Since `list` is mutable, changes inside the function affect the original.

---

# ⚖️ Summary Table

| Type      | Behavior in Python                             | Example               | Acts Like         |
| --------- | ---------------------------------------------- | --------------------- | ----------------- |
| Immutable | Cannot be changed, reassign creates new object | `int`, `str`, `tuple` | Pass by Value     |
| Mutable   | Can be changed inside function, same reference | `list`, `dict`, `set` | Pass by Reference |

---

👉 So, Python is **neither strictly pass-by-value nor strictly pass-by-reference**.
It’s **pass-by-object-reference (call by sharing)**.

