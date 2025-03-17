# 📚 Python Functions - Detailed Notes

## 👉 What is a Function?
A function is a block of reusable code designed to perform a specific task. Instead of writing the same code multiple times, functions allow us to **reuse** and **modularize** our code.

### 📝 Advantages of Functions in Python
- ✅ Improves **code readability**  
- ✅ Reduces **redundancy**  
- ✅ Increases **reusability**  
- ✅ Makes debugging **easier**  
- ✅ Supports **modular programming**  

---

## 🌟 Types of Functions in Python
Functions in Python can be categorized into **two main types**:

### 🔹 Built-in Functions (Predefined)
These functions are already available in Python, such as:
- **Mathematical Functions:** `abs()`, `sum()`, `min()`, `max()`
- **Type Conversion Functions:** `int()`, `float()`, `str()`, `list()`, `tuple()`
- **Other Utility Functions:** `print()`, `len()`, `range()`, `type()`

#### Example:
```python
print(len("Python"))  # Output: 6
```

### 🔹 User-defined Functions
These are functions that we create using the `def` keyword.

#### **Syntax of User-defined Function**
```python
def function_name(parameters):  
    # Function body
    return value  # (Optional)
```

---

## 📚 Classification of User-defined Functions Based on Input & Output

| Function Type                          | Accepts Arguments? | Returns Value? |
|----------------------------------------|--------------------|---------------|
| **Without arguments, without return**  | ❌ No              | ❌ No         |
| **Without arguments, with return**     | ❌ No              | ✅ Yes        |
| **With arguments, without return**     | ✅ Yes             | ❌ No         |
| **With arguments, with return**        | ✅ Yes             | ✅ Yes        |

---

## 📘 Explanation with Examples

### 🔹 Function Without Arguments & Without Return Value
A function that neither **accepts parameters** nor **returns a value**.

#### **Example**
```python
def greet():
    print("Hello, welcome to Python!")

greet()  # Function call
```

📌 **Category:** Utility Function

---

### 🔹 Function Without Arguments & With Return Value
A function that **does not accept parameters** but **returns a value**.

#### **Example**
```python
def get_pi():
    return 3.14159

pi_value = get_pi()  
print("Value of Pi:", pi_value)  # Output: 3.14159
```

📌 **Category:** Data Provider Function

---

### 🔹 Function With Arguments & Without Return Value
A function that **accepts parameters** but **does not return a value**.

#### **Example**
```python
def greet_person(name):
    print(f"Hello, {name}! Welcome to Python.")

greet_person("Alice")  # Output: Hello, Alice! Welcome to Python.
```

📌 **Category:** Action-based Function

---

### 🔹 Function With Arguments & With Return Value
A function that **accepts parameters** and **returns a value**.

#### **Example**
```python
def add(a, b):
    return a + b

result = add(5, 7)
print("Sum:", result)  # Output: Sum: 12
```

📌 **Category:** Computational Function

---

## 💪 Advanced Function Concepts

### 🔹 Function with Default Arguments
A function that assigns **default values** to parameters.

#### **Example**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()          # Output: Hello, Guest!
greet("Alice")   # Output: Hello, Alice!
```

---

### 🔹 Function with Keyword Arguments
Allows named arguments for better readability.

#### **Example**
```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Bob")  # Output: My name is Bob and I am 25 years old.
```

---

### 🔹 Function with Arbitrary Arguments (`*args` & `**kwargs`)

#### **Using `*args` (Non-keyword Arguments)**
Used when we don’t know how many arguments will be passed.

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4, 5))  # Output: 15
```

#### **Using `**kwargs` (Keyword Arguments)**
Used to pass named arguments dynamically.

```python
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

display_info(name="Alice", age=30, city="New York")
```

✔️ Output:
```
name: Alice
age: 30
city: New York
```

---

### 🔹 Anonymous (Lambda) Functions
Lambda functions are **small, single-line functions** without a name.

```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

---

### 🔹 Recursive Functions
A function is **recursive** if it calls **itself**.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

📌 *Recursive functions use a **runtime stack mechanism** (LIFO).*  

---

## 🌟 Summary Table

| Function Type                         | Accepts Arguments? | Returns Value? |
|----------------------------------------|--------------------|---------------|
| **Without arguments, without return** | ❌ No              | ❌ No         |
| **Without arguments, with return**    | ❌ No              | ✅ Yes        |
| **With arguments, without return**    | ✅ Yes             | ❌ No         |
| **With arguments, with return**       | ✅ Yes             | ✅ Yes        |

---

### 💪 Key Takeaways
✔️ Functions **make code reusable and modular**  
✔️ Python has **built-in and user-defined functions**  
✔️ Functions can be categorized based on **input-output behavior**  
✔️ Advanced concepts include **lambda, recursion, `*args`, `**kwargs`**  

---
