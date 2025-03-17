# Python Numeric Data Types - Detailed Notes

## 📌 Introduction to Numeric Data Types
Python provides several built-in **numeric data types** to handle different kinds of numerical values:
- **`int`**: Integer type for whole numbers.
- **`float`**: Floating point numbers (decimal values).
- **`bool`**: Boolean values (True/False) derived from integers.
- **`complex`**: Complex numbers with real and imaginary parts.

---
## 🔢 Integer (`int`)
### ✅ Characteristics:
- Represents **whole numbers** (positive, negative, or zero).
- Arbitrary precision (No limit on the size of an integer, only constrained by memory).
- Supports **binary (`0b`), octal (`0o`), and hexadecimal (`0x`)** representations.

### 📌 Creating Integers
```python
x = 100       # Decimal integer
y = 0b1010    # Binary representation (10 in decimal)
z = 0o12      # Octal representation (10 in decimal)
w = 0xA       # Hexadecimal representation (10 in decimal)
```

### 🔹 Integer Methods
```python
num = 12345
print(num.bit_length())   # Number of bits required to represent num in binary
print(num.to_bytes(4, 'big'))  # Convert int to bytes (4 bytes, big-endian)
```

### 🔹 Advanced Integer Operations
```python
print(pow(2, 3, 5))  # Power with modulus: (2^3) % 5 = 3
print(bin(10))       # Convert integer to binary
print(oct(10))       # Convert integer to octal
print(hex(10))       # Convert integer to hexadecimal
```

---
## 🔢 Floating Point (`float`)
### ✅ Characteristics:
- Represents **decimal numbers**.
- Stored as **double precision floating point numbers (64-bit IEEE 754 standard)**.
- Has limited precision due to binary representation.

### 📌 Creating Floats
```python
x = 10.5
y = float(10)  # Convert integer to float
```

### 🔹 Float Methods
```python
print(x.is_integer())   # Check if float is a whole number
print(float.fromhex('0x1.999999999999ap-4'))  # Convert hexadecimal to float
```

### 🔹 Advanced Float Operations
```python
import math
print(math.isnan(float('nan')))  # Check if value is NaN
print(math.isinf(float('inf')))  # Check if value is infinity
```

---
## 🔢 Boolean (`bool`)
### ✅ Characteristics:
- Represents **True or False** values.
- Internally stored as `1` (True) and `0` (False).
- Boolean values arise from comparisons and logical operations.

### 📌 Creating Boolean Values
```python
x = True
y = False
z = bool(1)  # True
w = bool(0)  # False
```

### 🔹 Boolean Operations
```python
print(True + True)    # 2 (Since True is 1)
print(False + True)   # 1
print(True * 10)      # 10 (1 * 10)
```

### 🔹 Boolean Methods
```python
print(bool([]))  # False (Empty list is treated as False)
print(bool(' ')) # True (Non-empty string is True)
```

---
## 🔢 Complex Numbers (`complex`)
### ✅ Characteristics:
- Represented as `a + bj` where `a` is the real part and `b` is the imaginary part.
- `j` is used instead of `i` (as in mathematics) to represent the imaginary unit.

### 📌 Creating Complex Numbers
```python
c1 = 3 + 4j
c2 = complex(2, -5)
```

### 🔹 Complex Number Methods
```python
print(c1.real)  # Get real part
print(c1.imag)  # Get imaginary part
print(abs(c1))  # Magnitude of complex number
```

### 🔹 Advanced Complex Operations
```python
import cmath
print(cmath.phase(c1))  # Get phase angle (in radians)
print(cmath.polar(c1))  # Convert to polar coordinates
print(cmath.exp(c1))    # Exponential of complex number
```

---
## 🔹 Summary
| Data Type | Description | Example |
|-----------|-------------|---------|
| `int` | Whole numbers | `10, -5, 0b1010` |
| `float` | Decimal numbers | `3.14, -2.7` |
| `bool` | Boolean values (True/False) | `True, False` |
| `complex` | Numbers with real & imaginary parts | `3+4j, complex(2,-5)` |

🎯 **Mastering these data types helps in efficient numerical computation and data manipulation in Python! 🚀**

