# Operator Overloading in Python

## 🔹 **What is Operator Overloading?**
Operator overloading is the process of **defining how operators (like `+`, `-`, `*`, etc.) work with user-defined objects**. Python allows us to customize operator behavior by **overriding special magic methods (dunder methods)**.

✅ This means that instead of using built-in operations, we can define how these operators should behave when used on custom objects.
It is the phenomenon of using the operator to work on the user defined class or user defined data
types by envoking the magic methods.
---

## ✅ **Example of Operator Overloading**
By default, Python does not know how to handle `+`, `-`, `*`, etc., for user-defined classes. We define these operations using special methods like `__add__`, `__sub__`, etc.

### 🔹 Implementing Operator Overloading
```python
class Arithmetic:
    def __init__(self, a):
        self.a = a
    
    def __add__(self, other):
        return self.a * other.a  # Overloading + to perform multiplication
    
    def __sub__(self, other):
        return self.a - other.a  # Overloading - to perform subtraction

ob1 = Arithmetic(12)
ob2 = Arithmetic(15)

print(ob1 + ob2)  # Output: 180 (Instead of addition, multiplication is performed)
print(abs(ob1 - ob2))  # Output: 3 (Absolute difference)
```

✔ Here, the `+` operator is overloaded to perform multiplication instead of addition.
✔ The `-` operator works as subtraction but returns the absolute value.

---

## ✅ **Common Magic Methods for Operator Overloading**
Python provides several magic methods to overload different operators.

| Operator | Magic Method  | Example |
|----------|--------------|---------|
| `+` | `__add__(self, other)` | `a + b` |
| `-` | `__sub__(self, other)` | `a - b` |
| `*` | `__mul__(self, other)` | `a * b` |
| `/` | `__truediv__(self, other)` | `a / b` |
| `//` | `__floordiv__(self, other)` | `a // b` |
| `%` | `__mod__(self, other)` | `a % b` |
| `**` | `__pow__(self, other)` | `a ** b` |
| `==` | `__eq__(self, other)` | `a == b` |
| `!=` | `__ne__(self, other)` | `a != b` |
| `>` | `__gt__(self, other)` | `a > b` |
| `<` | `__lt__(self, other)` | `a < b` |
| `>=` | `__ge__(self, other)` | `a >= b` |
| `<=` | `__le__(self, other)` | `a <= b` |

✅ **By implementing these methods, we can define how our class objects interact with operators.**

---

## ✅ **Advanced Operator Overloading**

### 🔹 **Overloading `*` for Custom Multiplication**
```python
class Multiply:
    def __init__(self, value):
        self.value = value
    
    def __mul__(self, other):
        return Multiply(self.value ** other.value)  # Raising power instead of multiplication
    
    def __str__(self):
        return str(self.value)

num1 = Multiply(2)
num2 = Multiply(3)
result = num1 * num2
print(result)  # Output: 8 (2^3 instead of 2 * 3)
```
✔ Here, we redefined the `*` operator to **compute power** instead of multiplication.

---

### 🔹 **Overloading `==` for Custom Comparison**
```python
class Compare:
    def __init__(self, value):
        self.value = value
    
    def __eq__(self, other):
        return self.value % 10 == other.value % 10  # Compare last digits

c1 = Compare(27)
c2 = Compare(37)
print(c1 == c2)  # Output: True (Because 27 and 37 have the same last digit)
```
✔ This allows `==` to compare objects in a **custom way**.

---

## ✅ **Custom String Representation with `__str__` and `__repr__`**
Operator overloading also helps in controlling how objects are displayed.

```python
class CustomPrint:
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return f"Value: {self.value}"
    
    def __repr__(self):
        return f"CustomPrint({self.value})"

obj = CustomPrint(42)
print(obj)   # Calls __str__
print(repr(obj))  # Calls __repr__
```
✔ `__str__` is for user-friendly display, while `__repr__` is for debugging.

---

## 🎯 **Final Summary**
✅ **Operator overloading allows Python operators to work on user-defined classes.**  
✅ **We use special magic methods like `__add__`, `__sub__`, and `__mul__` to define custom behavior.**  
✅ **Advanced usage includes overloading comparison, multiplication, and custom string representations.**  

🚀 **By leveraging operator overloading, we can make our custom classes behave like built-in types!**

