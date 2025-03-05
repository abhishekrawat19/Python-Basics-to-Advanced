# Lambda Functions in Python

## 1. Introduction
Lambda functions in Python are **anonymous functions** that are defined using the `lambda` keyword. Unlike normal functions defined with `def`, lambda functions have no name and are used for short, simple operations.

### **Syntax:**
```python
lambda arguments: expression
```
- `lambda` is the keyword.
- `arguments` are the input parameters.
- `expression` is a single operation that is evaluated and returned.

Example:
```python
add = lambda x, y: x + y
print(add(3, 4))  # Output: 7
```

---

## 2. Features of Lambda Functions
- Can have **multiple arguments** but only **one expression**.
- Implicitly **returns** the result of the expression.
- Used in **higher-order functions** like `map()`, `filter()`, and `reduce()`.
- Improves code readability when used in **small operations**.

Example:
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

---

## 3. Using Lambda with Built-in Functions
### **3.1 Using `map()`**
The `map()` function applies a function to every item in an iterable.

Example:
```python
nums = [1, 2, 3, 4]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # Output: [1, 4, 9, 16]
```

### **3.2 Using `filter()`**
The `filter()` function filters items based on a condition.

Example:
```python
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4, 6]
```

### **3.3 Using `reduce()`**
The `reduce()` function, from `functools`, applies a function **cumulatively** to reduce an iterable to a single value.

Example:
```python
from functools import reduce
nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  # Output: 24
```

---

## 4. Advanced Lambda Function Examples
### **4.1 Sorting a List of Tuples**
```python
tuples_list = [(1, 4), (3, 1), (5, 2), (2, 6)]
sorted_tuples = sorted(tuples_list, key=lambda x: x[1])
print(sorted_tuples)  # Output: [(3, 1), (5, 2), (1, 4), (2, 6)]
```

### **4.2 Finding the Intersection of Two Lists**
```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersection = list(filter(lambda x: x in list2, list1))
print(intersection)  # Output: [3, 4, 5]
```

### **4.3 Checking if a String Contains Only Vowels**
```python
is_vowel_string = lambda s: len([ch for ch in s if ch not in 'aeiouAEIOU']) == 0
print(is_vowel_string("aeiou"))  # Output: True
print(is_vowel_string("hello"))  # Output: False
```

### **4.4 Finding the Word with the Highest Vowel Count**
```python
from functools import reduce
words = ["apple", "banana", "education", "queue"]
vowel_count = lambda word: sum(1 for ch in word if ch in "aeiouAEIOU")
highest_vowel_word = reduce(lambda w1, w2: w1 if vowel_count(w1) > vowel_count(w2) else w2, words)
print(highest_vowel_word)  # Output: "education"
```

---

## 5. Limitations of Lambda Functions
- **Cannot contain multiple statements**.
- **No explicit return statement** (implicitly returns the evaluated expression).
- **Limited readability** for complex operations.

Example of an **incorrect** lambda function:
```python
# This is invalid because of multiple expressions
lambda x: (print(x), x + 2)  # ❌ Error
```

---

## 6. Conclusion
Lambda functions are **powerful for concise** and **small-scale** operations. They are best suited for **one-liners** in functional programming and when used with `map()`, `filter()`, and `reduce()`. However, for complex operations, a `def` function is preferred for better readability.

Example Comparison:
```python
# Using lambda
sum_lambda = lambda x, y: x + y
print(sum_lambda(3, 4))  # Output: 7

# Using def
def sum_func(x, y):
    return x + y
print(sum_func(3, 4))  # Output: 7
```

---

**🔥 Quick Summary:**
✅ Lambda functions are short, anonymous functions.
✅ Used with `map()`, `filter()`, `reduce()`.
✅ Good for concise expressions, but limited in complexity.

🚀 Use lambdas for quick operations, but prefer `def` for complex logic!

