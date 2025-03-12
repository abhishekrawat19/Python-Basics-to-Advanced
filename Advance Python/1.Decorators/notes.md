# **Decorators in Python**

## **What is a Decorator?**
A **decorator** is a function used to add extra functionalities to a main function **without modifying the original function**.

### **Working of a Decorator:**
- Extra functionality is added to the **main function**.
- A decorator performs a **pre-task**, executes the **main function**, and then performs a **post-task**.

### **Structure:**
1. **Pre-task** (Code executed before the main function)
2. **Main function execution**
3. **Post-task** (Code executed after the main function)

---

## **Types of Decorators**
There are two types of decorators:
1. **Inbuilt Decorators**
   - Examples: `@staticmethod`, `@classmethod`, `@property`
2. **User-defined Decorators**
   - Custom decorators created by users to extend functionality.

---

## **How to Create a Decorator?**
A decorator is implemented as a function that takes another function as an argument and returns a new function with added functionality.

### **Syntax:**
```python
    def decorator_name(func):
        def inner(*args, **kwargs):
            # Pre-task
            func(*args, **kwargs)  # Calling the main function
            # Post-task
        return inner
```

### **How to Use a Decorator?**
A decorator is applied using the `@decorator_name` syntax before the function definition.

```python
    @decorator_name
    def function_name():
        # Function statements
```

---

## **Example of a User-defined Decorator:**

```python
# Defining a decorator

def instagram(func):
    def inner(*args):
        print("www.instagram.com")
        print("Login done")
        func(*args)
        print("Logout")
    return inner

# Applying decorator to functions
@instagram
def abhishek():
    print("Message to me")

abhishek()

print("="*100)

@instagram
def amit():
    print("Instagram scrolls")

amit()

print("="*100)

@instagram
def kanish():
    print("Sing songs")

kanish()
```

**Output:**
```
www.instagram.com
Login done
Message to me
Logout
====================================================================================================
www.instagram.com
Login done
Instagram scrolls
Logout
====================================================================================================
www.instagram.com
Login done
Sing songs
Logout
```

---

## **Advanced Concepts of Decorators**

### **1. Chaining Multiple Decorators**
You can apply multiple decorators to a single function, and they will be executed from **bottom to top**.

```python
def decorator1(func):
    def inner():
        print("Decorator 1 before")
        func()
        print("Decorator 1 after")
    return inner

def decorator2(func):
    def inner():
        print("Decorator 2 before")
        func()
        print("Decorator 2 after")
    return inner

@decorator1
@decorator2
def my_function():
    print("Main function execution")

my_function()
```

### **2. Passing Arguments to Decorators**
Decorators can accept arguments by creating a wrapper around them.

```python
def repeat(n):
    def decorator(func):
        def inner():
            for _ in range(n):
                func()
        return inner
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
```

### **3. Class-Based Decorators**
Instead of using functions, you can use classes to define decorators.

```python
class MyDecorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print("Before function execution")
        self.func()
        print("After function execution")

@MyDecorator
def say_hello():
    print("Hello, World!")

say_hello()
```

### **4. Decorators with Return Values**
If a decorated function returns a value, ensure the wrapper function also returns it.

```python
def square_decorator(func):
    def inner(n):
        result = func(n)
        return result ** 2
    return inner

@square_decorator
def get_number(n):
    return n

print(get_number(5))  # Output: 25
```

### **5. Using `functools.wraps` to Preserve Function Metadata**
When using decorators, the metadata of the original function (like its name and docstring) might be lost. `functools.wraps` helps preserve this information.

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper

@my_decorator
def my_function():
    "This is my function."
    print("Executing function")

print(my_function.__name__)  # Output: my_function
print(my_function.__doc__)   # Output: This is my function.
```

### **6. Nesting Decorators Inside Functions**
You can define decorators inside functions to generate dynamic behavior.

```python
def create_decorator(msg):
    def decorator(func):
        def wrapper():
            print(f"{msg} Before execution")
            func()
            print(f"{msg} After execution")
        return wrapper
    return decorator

@create_decorator("Custom Message:")
def my_function():
    print("Hello, World!")

my_function()
```

This concludes the detailed explanation of decorators in Python, including advanced usage!

