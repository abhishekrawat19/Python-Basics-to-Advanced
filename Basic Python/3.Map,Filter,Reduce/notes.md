# Advanced Python Notes: `map()`, `filter()`, and `reduce()`

## **1. `map()`**

### **Definition**
`map(function, iterable, ...)` applies a function to each item in an iterable (or multiple iterables) and returns an iterator.

### **Key Points**
- Works efficiently with iterators.
- Can take multiple iterables if the function supports multiple arguments.
- Returns a `map` object (iterator) which should be converted to a list or tuple if needed.

### **Basic Example**
```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

### **Advanced Example: Using Multiple Iterables**
```python
a = [1, 2, 3]
b = [4, 5, 6]

sum_ab = list(map(lambda x, y: x + y, a, b))
print(sum_ab)  # [5, 7, 9]
```

### **Performance Consideration**
- `map()` is more memory-efficient than list comprehensions as it returns an iterator.
- Using `map()` with built-in functions is faster than using `lambda`.

```python
# Better performance using built-in function
squared = list(map(pow, numbers, [2]*len(numbers)))
```

---

## **2. `filter()`**

### **Definition**
`filter(function, iterable)` returns an iterator containing only elements where the function returns `True`.

### **Key Points**
- Used for conditional filtering.
- Returns an iterator (convert to `list()` if needed).
- Function must return a boolean value.

### **Basic Example**
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6]
```

### **Advanced Example: Filtering Prime Numbers**
```python
from math import sqrt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(50))
primes = list(filter(is_prime, numbers))
print(primes)  # [2, 3, 5, 7, 11, 13, ...]
```

### **Performance Consideration**
- `filter()` is useful for large datasets as it avoids unnecessary iterations.
- List comprehensions can sometimes be more readable: `[x for x in numbers if x % 2 == 0]`.

---

## **3. `reduce()`**

### **Definition**
`reduce(function, iterable, initial_value)` applies a function cumulatively to items in an iterable, reducing them to a single result.

🔹 **Note:** `reduce()` is in `functools` module.

```python
from functools import reduce
```

### **Key Points**
- Used for aggregation (sum, product, concatenation, etc.).
- Returns a single accumulated value.

### **Basic Example: Sum of a List**
```python
numbers = [1, 2, 3, 4, 5]
sum_all = reduce(lambda x, y: x + y, numbers)
print(sum_all)  # 15
```

### **Advanced Example: Finding Maximum Value**
```python
numbers = [3, 5, 2, 8, 7, 10, 1]
max_num = reduce(lambda x, y: x if x > y else y, numbers)
print(max_num)  # 10
```

### **Advanced Example: Concatenating Strings**
```python
words = ["Python", "is", "a", "powerful", "language"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # "Python is a powerful language"
```

### **Performance Consideration**
- `reduce()` can be replaced by built-in functions like `sum()` or `max()` for better readability.
- Avoid using `reduce()` for operations where explicit loops or `map()`/`filter()` are more readable.

```python
# Better alternative
max_num = max(numbers)
```

---

## **4. Combining `map()`, `filter()`, and `reduce()`**

### **Example: Sum of Squared Even Numbers**
```python
from functools import reduce
numbers = range(1, 11)

# Step 1: Square numbers using map
squared = map(lambda x: x**2, numbers)

# Step 2: Filter even squares
even_squares = filter(lambda x: x % 2 == 0, squared)

# Step 3: Sum even squares using reduce
sum_even_squares = reduce(lambda x, y: x + y, even_squares)

print(sum_even_squares)  # 220 (4+16+36+64+100)
```

---

## **5. Alternative Approaches and Best Practices**

### **List Comprehensions vs `map()` & `filter()`**
- `map()` and `filter()` are **memory-efficient** but less readable than list comprehensions.
- List comprehensions are generally more Pythonic.

```python
# Using map()
squared = list(map(lambda x: x**2, numbers))

# Using list comprehension (Preferred)
squared = [x**2 for x in numbers]
```

```python
# Using filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Using list comprehension (Preferred)
evens = [x for x in numbers if x % 2 == 0]
```

### **When to Use `reduce()`?**
- Use when **no built-in function** like `sum()`, `max()`, `min()` exists.
- If readability is a concern, prefer loops.

```python
# Using reduce()
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])

# Using explicit loop (More readable)
product = 1
for num in [1, 2, 3, 4, 5]:
    product *= num
```

---

## **6. Summary Table**

| Function  | Purpose                              | Returns     | Use Case |
|-----------|--------------------------------------|------------|----------|
| `map()`   | Applies a function to iterable      | Iterator   | Transforming data |
| `filter()`| Filters elements based on condition | Iterator   | Selecting elements |
| `reduce()`| Aggregates elements to single value | Single Value | Cumulative operations |

---

## **7. Final Takeaways**
✅ Use `map()` when transforming data efficiently.  
✅ Use `filter()` when extracting elements based on a condition.  
✅ Use `reduce()` when aggregating multiple elements into one.  
✅ Prefer list comprehensions for better readability when applicable.  
✅ Avoid `reduce()` when built-in alternatives exist.  

---

This document covers advanced use cases, performance considerations, and best practices for `map()`, `filter()`, and `reduce()` in Python. 🚀
