# 📌p Python Strings - Detailed Notes

## 🔹 Introduction to Strings
A **string** in Python is a **sequence of characters** enclosed in **single (`'`), double (`"`), or triple (`'''` or """ """)** quotes.

### ✅ Characteristics of Strings:
- **Immutable**: Once created, they cannot be changed.
- **Ordered**: Characters have a fixed position (indexing).
- **Iterable**: Can be traversed using loops.
- **Supports Various Operations**: Slicing, concatenation, repetition, etc.

### 🔹 Creating Strings
```python
# Single and double quotes
string1 = 'Hello'
string2 = "World"

# Triple quotes for multiline strings
multi_line = '''This is
a multiline string'''

# String with special characters
escaped_string = "He said, \"Python is great!\""

print(string1, string2)  # Output: Hello World
```

---

## 🔹 Accessing Strings

### 🔸 Indexing
Python supports **positive and negative indexing**.

```python
text = "Python"

print(text[0])   # Output: P  (First character)
print(text[-1])  # Output: n  (Last character)
print(text[3])   # Output: h
```

### 🔸 Slicing
```python
text = "Python Programming"

print(text[0:6])   # Output: Python
print(text[:6])    # Output: Python (same as above)
print(text[7:])    # Output: Programming
print(text[-11:-1]) # Output: Programmin
print(text[::2])   # Output: Pto rgamn (every second character)
```

---

## 🔹 Modifying Strings
Since strings are **immutable**, direct modification is **not allowed**.

```python
text = "Hello"
# text[0] = 'J'  # ❌ TypeError: 'str' object does not support item assignment

# Correct way - Reassign a new string
text = "Jello"
print(text)  # Output: Jello
```

---

## 🔹 String Concatenation and Repetition
```python
str1 = "Hello"
str2 = "World"

# Concatenation
result = str1 + " " + str2
print(result)  # Output: Hello World

# Repetition
repeat = "Python " * 3
print(repeat)  # Output: Python Python Python
```

---

## 🔹 String Methods
Python provides numerous **built-in string methods**.

### 🔸 **Case Conversion Methods**
```python
text = "Python Programming"

print(text.upper())    # Output: PYTHON PROGRAMMING
print(text.lower())    # Output: python programming
print(text.capitalize())  # Output: Python programming
print(text.title())    # Output: Python Programming
print(text.swapcase()) # Output: pYTHON pROGRAMMING
```

### 🔸 **Checking String Content**
```python
text = "Hello123"

print(text.isalpha())  # False (contains numbers)
print(text.isdigit())  # False (contains letters)
print(text.isalnum())  # True (only letters and numbers)
print("   ".isspace()) # True (only spaces)
print("Python".startswith("Py"))  # True
print("Python".endswith("on"))    # True
```

### 🔸 **Finding and Replacing**
```python
text = "Python is fun"

print(text.find("is"))    # Output: 7 (index of "is")
print(text.index("fun"))  # Output: 10
print(text.replace("fun", "awesome"))  # Output: Python is awesome
```

### 🔸 **Splitting and Joining**
```python
text = "Python,Java,C++"

# Splitting into list
langs = text.split(",")  
print(langs)  # Output: ['Python', 'Java', 'C++']

# Joining list into string
joined = "-".join(langs)
print(joined)  # Output: Python-Java-C++
```

---

## 🔹 Advanced String Operations

### 🔸 **String Formatting**
1⃣ **Using `format()` method**
```python
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: My name is Alice and I am 25 years old.
```

2⃣ **Using f-strings (Python 3.6+)**
```python
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")  
```

3⃣ **Using `%` Operator (Old Style)**
```python
name = "Alice"
age = 25
print("My name is %s and I am %d years old." % (name, age))
```

---

### 🔸 **Escape Characters**

| Escape Sequence | Meaning |
|----------------|---------|
| `\n` | New Line |
| `\t` | Tab |
| `\\` | Backslash |
| `\'` | Single Quote |
| `\"` | Double Quote |

```python
print("Hello\nWorld")  # Newline
print("Hello\tWorld")  # Tab
print("She said, \"Python is awesome!\"")
```

---

## 🔹 📈 Summary

✅ Strings are **immutable, ordered, iterable** and support **indexing & slicing**.  
✅ Methods like `.upper()`, `.lower()`, `.replace()`, `.split()`, `.join()` help in string manipulation.  
✅ Advanced techniques include **f-strings, regex, raw strings, encoding/decoding, and translation tables**.  
✅ Understanding **Unicode and escape sequences** is essential for handling special characters.  

---
🚀 **Mastering strings in Python will improve your text processing skills and make your code more efficient!** 🔥

