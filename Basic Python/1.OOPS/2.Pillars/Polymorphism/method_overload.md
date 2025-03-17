# Method Overloading in Python

## Definition
Method overloading is the process of defining multiple methods with the **same name but different parameters** to perform different tasks. However, **Python does not support traditional method overloading** like other languages (Java, C++). Instead, Python allows only the latest defined method to be executed.

---

## 🔴 Python Does Not Support Traditional Method Overloading
In Python, if multiple methods have the same name, **only the last defined method is retained**, and previous ones are overwritten.

### Example:
```python
class Overload:
    @staticmethod
    def add(a, b):
        return a + b
    
    prev = add  # Storing the previous method
    
    @staticmethod
    def add(a, b):  # Overwrites previous method
        return a - b
    
    @staticmethod
    def add(a, b):  # Overwrites again
        return a * b

ob1 = Overload()
print(ob1.add(3, 4))  # Output: 12 (Multiplication runs)
```

🔹 The last defined `add()` method **overwrites** the previous versions, causing **earlier methods to be lost**.

---

## 🛠 **Workarounds for Method Overloading in Python**
Since Python does not support method overloading **directly**, we can achieve similar behavior using:
1. **Default Arguments**
2. **Variable-Length Arguments (`*args` and `**kwargs`)**
3. **Function Overloading Using `@singledispatch`**
4. **Monkey Patching**

---

## ✅ 1. Method Overloading Using Default Arguments
We can simulate overloading by using **default parameters**, allowing different behaviors based on the number of arguments passed.

```python
class Overload:
    @staticmethod
    def add(a, b=0, c=0):  # Default parameters
        return a + b + c

print(Overload.add(5))        # Output: 5
print(Overload.add(5, 10))    # Output: 15
print(Overload.add(5, 10, 15))  # Output: 30
```
🔹 The method works with different numbers of parameters, **mimicking** method overloading.

---

## ✅ 2. Method Overloading Using `*args` and `**kwargs`
We can use `*args` (for positional arguments) and `**kwargs` (for keyword arguments) to accept **multiple parameters dynamically**.

```python
class Overload:
    @staticmethod
    def add(*args):
        return sum(args)

print(Overload.add(5))            # Output: 5
print(Overload.add(5, 10))        # Output: 15
print(Overload.add(5, 10, 15))    # Output: 30
```
🔹 `*args` allows handling **any number of arguments**, making it flexible.

---

## ✅ 3. Method Overloading Using `@singledispatch`
Python’s `functools.singledispatch` decorator allows method overloading **based on argument type**.

```python
from functools import singledispatch

@singledispatch
def show(value):
    print("Default implementation: ", value)

@show.register
def _(value: int):
    print("Integer implementation: ", value)

@show.register
def _(value: str):
    print("String implementation: ", value)

show(10)      # Output: Integer implementation: 10
show("Hello") # Output: String implementation: Hello
show(5.5)     # Output: Default implementation: 5.5
```
🔹 This allows overloading functions based on **data types**.

---

## ✅ 4. Restoring Overwritten Methods Using **Monkey Patching**
### 🔹 What is Monkey Patching?
Monkey patching is a technique used in Python to **dynamically modify or extend classes and methods at runtime**. It allows us to restore or modify methods **without altering the original class definition**.Monkey Patching helps retain old methods by storing their reference before redefinition.

### 🔹 Why Use Monkey Patching in Method Overloading?
Since Python **overwrites** methods with the same name, we can use **monkey patching** to retain previous methods by storing their references before redefining them.

### 🔹 Example:
```python
class Overload:
    @staticmethod
    def add(a, b):
        return a + b  # First method
    
    prev = add  # Store reference of this method
    
    @staticmethod
    def add(a, b):
        return a - b  # Second method (overwrites first)

ob1 = Overload()
print(ob1.add(3, 4))   # Output: -1 (latest method runs)
print(ob1.prev(3, 4))  # Output: 7 (restored previous method using monkey patching)
```

🔹 **How It Works?**
1. We define an `add()` method that performs addition.
2. Before redefining it, we **store the reference** of the first `add()` in `prev`.
3. The new `add()` method **overwrites** the previous one.
4. Now, `ob1.add(3,4)` calls the latest method (subtraction), while `ob1.prev(3,4)` calls the previous method (addition).

---

## 🔥 **Advanced Use Case of Monkey Patching**
Monkey patching can be used **dynamically at runtime** to modify existing classes.

### Example: Modifying an Existing Library Class
```python
import datetime

# Original method
print(datetime.datetime.now())

# Monkey patching the now() method to return a fixed date
def fixed_now():
    return datetime.datetime(2023, 1, 1)

datetime.datetime.now = fixed_now

# Now it always returns the fixed date
print(datetime.datetime.now())  # Output: 2023-01-01 00:00:00
```

🔹 **Real-World Uses of Monkey Patching:**
- **Debugging & Testing:** Replacing methods temporarily for testing purposes.
- **Extending Libraries:** Modifying third-party modules dynamically.
- **Hotfixes & Patches:** Applying quick fixes without modifying source code.

---

## 🎯 Summary
✅ **Python does not support traditional method overloading**—only the latest method is retained.
✅ **Default arguments** allow different behaviors based on parameter count.
✅ **`*args` and `**kwargs`** allow handling variable arguments dynamically.
✅ **`@singledispatch`** enables overloading based on data type.
✅ **Monkey patching** helps retain overwritten methods and modify classes dynamically.
✅ **Monkey patching is useful for debugging, extending libraries, and hotfixes.**

🚀 **Even though Python lacks true method overloading, we can achieve similar behavior using these techniques!**

