# **Functions in Python**

## **What is a Function?**
A function is a block of reusable code that performs a specific task. It helps in organizing the code, improving readability, and reducing redundancy.

### **Advantages of Using Functions**
1. **Code Reusability** – Write once, use multiple times.
2. **Modularity** – Code is divided into smaller, manageable parts.
3. **Improved Readability** – Makes the program structured and easier to understand.
4. **Avoids Redundancy** – Reduces code repetition.
5. **Easy Debugging** – Errors can be fixed in a single function without modifying the entire code.

---

## **Types of Functions in Python**
Python provides two types of functions:

### **1. Built-in Functions**
These are predefined functions available in Python.
- `print()`, `len()`, `type()`, `input()`, `abs()`, `sum()`, `max()`, `min()`, etc.

### **2. User-Defined Functions**
Functions created by users for specific tasks.

#### **Syntax of Function**
```python
def function_name(parameters):  
    """Function Docstring"""  
    # Function body  
    return value  # (optional)
```
#### **Example of a Simple Function**
```python
def greet():
    print("Hello, welcome to Python!")

greet()  # Function call
```

---

## **Types of Arguments in Python Functions**
Python allows different types of arguments in functions:

### **1. Positional Arguments**
Values are assigned to parameters in the order they are passed.
```python
def greet(name, age):
    print(f"Hello {name}, you are {age} years old!")

greet("Alice", 25)  # Correct
# greet(25, "Alice")  # Wrong order, incorrect output
```

### **2. Keyword Arguments**
Arguments are passed using parameter names to avoid order dependency.
```python
greet(age=25, name="Alice")  # Order doesn't matter
```

### **3. Default Arguments**
Default values are used if no argument is provided.
```python
def greet(name="Guest"):
    print(f"Hello {name}!")

greet()  # Output: Hello Guest!
greet("John")  # Output: Hello John!
```

### **4. Variable-Length Arguments**
Python allows functions to accept an arbitrary number of arguments.

#### **A. `*args` (Non-Keyword Arguments)**
Used to pass multiple positional arguments as a tuple.
```python
def add(*numbers):
    print(sum(numbers))

add(1, 2, 3, 4, 5)  # Output: 15
```

#### **B. `**kwargs` (Keyword Arguments)**
Used to pass multiple named arguments as a dictionary.
```python
def info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

info(name="Alice", age=25, city="New York")
```

---

## **Types of Functions in Python**
Python supports different types of user-defined functions:

### **1. Simple Function**
```python
def add(a, b):
    return a + b

print(add(5, 10))  # Output: 15
```

### **2. Recursive Function**
A function that calls itself to solve a problem in smaller instances.

**Example: Factorial Using Recursion**
```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

### **3. Lambda (Anonymous) Functions**
One-liner functions defined using `lambda` keyword.
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

### **4. Higher-Order Functions**
Functions that take other functions as arguments.
```python
def apply_func(func, value):
    return func(value)

print(apply_func(lambda x: x * 2, 5))  # Output: 10
```

### **5. Generator Functions**
Functions using `yield` to return values lazily.
```python
def count():
    for i in range(5):
        yield i

gen = count()
print(next(gen))  # Output: 0
print(next(gen))  # Output: 1
```

---

## **Advanced Function Concepts in Python**

### **1. Function Overloading (Using Default Arguments)**
Python does not support method overloading like other languages, but we can achieve similar behavior using default arguments.
```python
def greet(name, msg="Hello"):
    print(f"{msg}, {name}!")

greet("Alice")  # Uses default msg
greet("Bob", "Good Morning")  # Custom msg
```

### **2. Function Overriding**
Used in **inheritance**, where a child class overrides the function of the parent class.
```python
class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def show(self):
        print("This is Child class")

c = Child()
c.show()  # Output: This is Child class
```

### **3. Closures (Function Inside a Function)**
A function inside another function that remembers the outer function's variables.
```python
def outer_function(msg):
    def inner_function():
        print(msg)  # Accessing outer variable
    return inner_function

closure = outer_function("Hello from Closure!")
closure()  # Output: Hello from Closure!
```

### **4. Decorators**
A function that modifies another function without modifying its structure.
```python
def decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@decorator
def hello():
    print("Hello, World!")

hello()
```

### **5. Memoization (Caching Results)**
Using recursion with caching to improve performance.
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))  # Output: 55
```

### **6. Partial Functions**
Allows fixing some function parameters in advance.
```python
from functools import partial

def power(base, exp):
    return base ** exp

square = partial(power, exp=2)  # Fix exponent as 2
print(square(5))  # Output: 25
```

---

## **Summary**
| **Concept**       | **Description** |
|------------------|----------------|
| Function | Block of reusable code |
| Built-in Functions | Predefined functions in Python |
| User-Defined Functions | Functions created by the user |
| Recursive Functions | Functions that call themselves |
| Lambda Functions | Anonymous one-liner functions |
| Decorators | Modifies functions without altering structure |
| Memoization | Optimization using caching |
| Partial Functions | Fixing function parameters |

---

This is a **comprehensive guide** covering all **basic to advanced** function concepts in Python! 🚀

# Understanding the Code: `who = writer()`

## 1. Function Definition (`writer()`)
- The function `writer()` is defined and does the following:
  - Creates a local variable `title = 'Sir'`.
  - Defines a **lambda function** (`name`) that:
    ```python
    lambda x: title + ' ' + x
    ```
    - Takes `x` as input.
    - Returns `'Sir ' + x`.
  - Instead of executing the lambda function, `writer()` **returns** it.

### Example Code:
```python
def writer():
    title = 'Sir'
    name = (lambda x: title + ' ' + x)  # Lambda function
    return name  # Returning the function itself
```

- The function does **not** return a string.
- Instead, it returns a **function** that can be used later.

---

## 2. Assigning `who = writer()`
- When `writer()` is called, it **returns the lambda function**, and we store it in `who`:
  ```python
  who = writer()
  ```
- `who` is **not** a string; it is a **function variable** that holds the lambda function.

---

## 3. Calling `who('Arthur')`
- When we call `who('Arthur')`, it executes the lambda function:
  ```python
  who('Arthur')
  ```
- This is equivalent to:
  ```python
  'Sir ' + 'Arthur'  # → 'Sir Arthur'
  ```
- The output is:
  ```
  Sir Arthur
  ```

### Example Code with Execution:
```python
who = writer()
print(who('Arthur'))  # Output: Sir Arthur
```

---

## 4. Why Use `who`?
- `who` allows us to **reuse the function** multiple times:
  ```python
  print(who('Lancelot'))  # Output: Sir Lancelot
  print(who('Gawain'))    # Output: Sir Gawain
  ```
- This demonstrates **closures** in Python:
  - The lambda function **remembers** the `title` variable from `writer()`, even after `writer()` has finished executing.
  - `title` remains accessible inside `who`.

---

## 5. What is a Closure?
- A **closure** in Python occurs when:
  1. A function (`writer()`) **returns another function** (`lambda`).
  2. The returned function **remembers** variables from its parent function (`title`).
- Even though `writer()` finishes execution, the returned lambda function still has access to `title`.

### Example of a Simple Closure:
```python
def outer_function():
    message = "Hello"
    def inner_function(name):
        return message + ', ' + name
    return inner_function  # Returning the inner function

say_hello = outer_function()  # say_hello now holds inner_function
print(say_hello("Alice"))  # Output: Hello, Alice
```
- Here, `message = "Hello"` is **remembered** by `inner_function()` even after `outer_function()` has finished execution.

---

## 6. Key Takeaways
✅ `writer()` **returns a function**, not a string.  
✅ `who = writer()` stores that function.  
✅ `who('Arthur')` **calls** the function, generating `'Sir Arthur'`.  
✅ Demonstrates **closures** in Python.  
✅ Allows function reuse with different inputs (`who('Lancelot')`, `who('Gawain')`).

---

## 7. Complete Working Code
```python
def writer():
    title = 'Sir'
    name = (lambda x: title + ' ' + x)
    return name

who = writer()
print(who('Arthur'))  # Output: Sir Arthur
print(who('Lancelot'))  # Output: Sir Lancelot
print(who('Gawain'))  # Output: Sir Gawain
```

