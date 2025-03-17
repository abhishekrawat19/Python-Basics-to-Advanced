# Operator Precedence and Associativity in Python

## 🔹 Introduction

Operator precedence determines the order in which operations are performed in an expression. It follows a predefined hierarchy, similar to the **PEMDAS** rule in mathematics:

- **P** → Parentheses `()`
- **E** → Exponents `**`
- **MD** → Multiplication `*` and Division `/` (from left to right)
- **AS** → Addition `+` and Subtraction `-` (from left to right)

## 🔹 Python Operator Precedence Table

| Operator | Description | Associativity |
|----------|-------------|--------------|
| `()` | Parentheses | Left to Right |
| `**` | Exponentiation | Right to Left |
| `+x`, `-x`, `~x` | Unary plus, minus, bitwise NOT | Right to Left |
| `*`, `/`, `//`, `%` | Multiplication, division, floor division, modulo | Left to Right |
| `+`, `-` | Addition, subtraction | Left to Right |
| `<<`, `>>` | Bitwise shift operators | Left to Right |
| `&` | Bitwise AND | Left to Right |
| `^` | Bitwise XOR | Left to Right |
| `|` | Bitwise OR | Left to Right |
| `==`, `!=`, `>`, `<`, `>=`, `<=` | Comparison operators | Left to Right |
| `not` | Logical NOT | Right to Left |
| `and` | Logical AND | Left to Right |
| `or` | Logical OR | Left to Right |
| `=` and `+=`, `-=`, `*=`, `/=`, `//=` | Assignment operators | Right to Left |

## 🔹 Operator Associativity

**Associativity** determines the direction in which an expression is evaluated when multiple operators of the same precedence appear. Operators in Python follow either **left-to-right** or **right-to-left** associativity.

### ✅ **Left-to-Right Associativity**
Most operators, such as `+`, `-`, `*`, `/`, `//`, `%`, and comparison operators, are evaluated from **left to right**.

#### Example:
```python
print(10 - 2 + 3)  # (10 - 2) + 3 = 8 + 3 = 11
```

🔹 **Output:**
```
11
```

### ✅ **Right-to-Left Associativity**
Only **exponentiation (`**`) and assignment operators (`=` `+=` `-=` etc.)** follow **right-to-left** associativity.

#### Example:
```python
print(2 ** 3 ** 2)  # 2 ** (3 ** 2) = 2 ** 9 = 512
```
🔹 **Output:**
```
512
```

## 🔹 Examples of Operator Precedence

#### 1️⃣ **Exponentiation has higher precedence than multiplication**
```python
result = 2 ** 3 * 4
print(result)
```
🔹 **Output:**
```
32  # (2 ** 3) * 4 → 8 * 4 = 32
```

#### 2️⃣ **Parentheses change the order**
```python
result = (2 + 3) * 4
print(result)
```
🔹 **Output:**
```
20  # Parentheses are evaluated first
```

#### 3️⃣ **Left-to-right associativity for multiplication and division**
```python
result = 8 / 4 * 2
print(result)
```
🔹 **Output:**
```
4.0  # (8 / 4) * 2 = 2 * 2 = 4.0
```

#### 4️⃣ **Right-to-left associativity for exponentiation**
```python
result = 2 ** 3 ** 2
print(result)
```
🔹 **Output:**
```
512  # 2 ** (3 ** 2) = 2 ** 9 = 512
```

#### 5️⃣ **Logical AND (`and`) has higher precedence than OR (`or`)**
```python
result = True or False and False
print(result)
```
🔹 **Output:**
```
True  # False and False → False; then True or False → True
```

## 🔹 Conclusion
- **Operator precedence** defines the order in which Python evaluates expressions.
- **Associativity** determines whether operators of the same precedence level are evaluated **left-to-right** or **right-to-left**.
- **PEMDAS** (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction) applies to Python.
- Some operators follow **left-to-right** associativity, while others (like exponentiation) follow **right-to-left**.
- Always use **parentheses** to clarify complex expressions.

Let me know if you need more details! 🚀

