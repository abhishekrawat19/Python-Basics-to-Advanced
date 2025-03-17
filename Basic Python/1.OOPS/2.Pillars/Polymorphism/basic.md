# Polymorphism in Python

## Definition
Polymorphism is a phenomenon of performing two or more different operations using the **same method** or **operator**. It allows flexibility and reusability in programming.

### Three Types of Polymorphism in Python:
1. **Method Overloading**
2. **Operator Overloading**
3. **Method Overriding**

---

# 1️⃣ Method Overloading

## Definition
Method overloading is the process of defining multiple methods with the **same name but different parameters** to perform different tasks. 

### 🔴 **Python does not support traditional method overloading**
- In Python, if multiple methods have the same name, only the **latest defined method** is used, and previous ones are overwritten.

## Example:
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

# 🛠 **Restoring Previous Methods Using Monkey Patching**

## 🔹 What is Monkey Patching?
Monkey Patching is a technique where we **store** the reference of a method before it gets overwritten. This allows us to restore or switch back to a previous method.

## Example:
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

🔹 **Monkey patching** allows restoring **previously overwritten methods** by storing their reference before redefining them.

---

## 🔥 Advanced Concepts in Polymorphism

### 1️⃣ **Operator Overloading**
In Python, operators like `+`, `-`, `*`, etc., can be overloaded to work with user-defined objects. This is done using **magic methods (dunder methods)**.

#### Example of Operator Overloading:
```python
class Number:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Number(self.value + other.value)
    
    def __str__(self):
        return str(self.value)

num1 = Number(10)
num2 = Number(20)
num3 = num1 + num2  # Uses __add__ method
print(num3)  # Output: 30
```

🔹 **The `+` operator is overloaded** to work with objects, enabling custom behaviors.

---

### 2️⃣ **Method Overriding (Polymorphism with Inheritance)**
Method overriding allows a child class to **redefine** a method of its parent class.

#### Example:
```python
class Parent:
    def show(self):
        print("Parent class method")

class Child(Parent):
    def show(self):
        print("Child class method")

obj = Child()
obj.show()  # Output: Child class method (Overridden method runs)
```

🔹 The child class **overrides** the `show()` method from the parent class.

---

## 🎯 Summary
✅ **Polymorphism** allows the same function/operator to perform multiple operations.
✅ **Python does not support traditional method overloading**—only the latest method is retained.
✅ **Monkey patching** helps restore overwritten methods.
✅ **Operator overloading** enables custom behavior for operators in user-defined classes.
✅ **Method overriding** allows a child class to redefine a parent class method.

🚀 **Polymorphism is key to writing flexible and reusable code in Python!**

