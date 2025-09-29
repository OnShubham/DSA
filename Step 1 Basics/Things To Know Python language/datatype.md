
````markdown

# 📘 Python Data Types

Python is **dynamically typed**, meaning you don’t need to explicitly declare the type of a variable — the interpreter determines it at runtime.  
This flexibility makes coding faster, but it can also introduce subtle bugs if data types are misused.

---

## 🔢 Numeric Types
- **`int`** → Integers (arbitrary precision, no size limit).  
  Example: `x = 42`
- **`float`** → Floating-point numbers (double precision).  
  Example: `pi = 3.14159`
- **`complex`** → Complex numbers with real and imaginary parts.  
  Example: `z = 3 + 5j`

---

## 🔠 Text Type
- **`str`** → Immutable sequence of Unicode characters.  
  Example: `name = "Python"`

---

## 📚 Sequence Types
- **`list`** → Mutable ordered collection.  
  Example: `fruits = ["apple", "banana", "cherry"]`
- **`tuple`** → Immutable ordered collection.  
  Example: `point = (10, 20)`
- **`range`** → Immutable sequence, often used in loops.  
  Example: `r = range(5)` → `[0, 1, 2, 3, 4]`

---

## 🔑 Mapping Type
- **`dict`** → Collection of key-value pairs.  
  Example:  
  ```python
  student = {"name": "Alice", "age": 22}
````

---

## 🌀 Set Types

* **`set`** → Unordered collection of unique elements (mutable).
  Example: `unique_nums = {1, 2, 3, 3}` → `{1, 2, 3}`
* **`frozenset`** → Immutable version of a set.
  Example: `fs = frozenset([1, 2, 3])`

---

## ✅ Boolean Type

* **`bool`** → Logical values, either `True` or `False`.
  Example:

  ```python
  is_active = True
  result = (5 > 3)  # True
  ```

---

## 🟦 Special Type

* **`NoneType`** → Represents absence of a value.
  Example: `x = None`

---

## 🎭 Advanced Types

* **Classes & Objects** → Everything in Python is an object.
* **Dataclasses** → Lightweight classes for structured data (`@dataclass`).
* **Enums** → Symbolic names bound to unique, constant values.
* **Typing Hints** → Introduced via `typing` module for better clarity in large codebases.

---

## ⚡ Key Notes

* **Dynamic Typing**: Variable type decided at runtime.
* **Mutable vs Immutable**:

  * Mutable → `list`, `dict`, `set`
  * Immutable → `tuple`, `str`, `frozenset`, `range`
* **Integers** in Python are **unbounded**, unlike many other languages.

---

## ✅ Quick Reference Table

| Category | Types                                     |
| -------- | ----------------------------------------- |
| Numeric  | `int`, `float`, `complex`                 |
| Text     | `str`                                     |
| Sequence | `list`, `tuple`, `range`                  |
| Mapping  | `dict`                                    |
| Set      | `set`, `frozenset`                        |
| Boolean  | `bool`                                    |
| Special  | `NoneType`                                |
| Advanced | Classes, Dataclasses, Enums, Typing Hints |

-