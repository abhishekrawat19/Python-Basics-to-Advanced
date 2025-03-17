# String Methods in Python (With Code & Output)

## 1. Modifying Strings

| Method | Purpose | Returns |
|--------|---------|---------|
| `upper()` | Converts all characters to uppercase | ✅ New string |
| `lower()` | Converts all characters to lowercase | ✅ New string |
| `title()` | Capitalizes first letter of each word | ✅ New string |
| `capitalize()` | Capitalizes the first character of the string | ✅ New string |
| `strip()` | Removes leading & trailing spaces | ✅ New string |
| `replace(old, new)` | Replaces occurrences of a substring | ✅ New string |
| `format(*args, **kwargs)` | Formats string with values | ✅ New string |
| `encode(encoding='utf-8')` | Encodes the string in specified format | ✅ Encoded bytes |

### Examples
#### `upper()`
```python
text = "hello world"
print(text.upper())  # Output: "HELLO WORLD"
```

#### `lower()`
```python
text = "Hello World"
print(text.lower())  # Output: "hello world"
```

#### `title()`
```python
text = "hello world"
print(text.title())  # Output: "Hello World"
```

#### `capitalize()`
```python
text = "hello world"
print(text.capitalize())  # Output: "Hello world"
```

#### `strip()`
```python
text = "  hello world  "
print(text.strip())  # Output: "hello world"
```

#### `replace(old, new)`
```python
text = "hello world"
print(text.replace("hello", "hi"))  # Output: "hi world"
```

#### `format(*args, **kwargs)`
```python
name = "Alice"
age = 25
print("My name is {} and I am {} years old".format(name, age))  # Output: "My name is Alice and I am 25 years old"
```

#### `encode(encoding='utf-8')`
```python
text = "hello world"
encoded_text = text.encode("utf-8")
print(encoded_text)  # Output: b'hello world'
```

---

## 2. Searching in Strings

| Method | Purpose | Returns |
|--------|---------|---------|
| `find(substring)` | Finds the first occurrence index | ✅ Index (or -1) |
| `index(substring)` | Like `find()`, but raises error if not found | ✅ Index |
| `count(substring)` | Counts occurrences of a substring | ✅ Count |
| `startswith(prefix)` | Checks if string starts with prefix | ✅ Boolean |
| `endswith(suffix)` | Checks if string ends with suffix | ✅ Boolean |

### Examples
#### `find(substring)`
```python
text = "hello world"
print(text.find("world"))  # Output: 6
```

#### `index(substring)`
```python
text = "hello world"
print(text.index("world"))  # Output: 6

# text.index("Python")  # Error: ValueError
```

#### `count(substring)`
```python
text = "banana"
print(text.count("a"))  # Output: 3
```

#### `startswith(prefix)`
```python
text = "hello world"
print(text.startswith("hello"))  # Output: True
```

#### `endswith(suffix)`
```python
text = "hello world"
print(text.endswith("world"))  # Output: True
```

---

## 3. Splitting and Joining Strings

| Method | Purpose | Returns |
|--------|---------|---------|
| `split(separator)` | Splits string into a list | ✅ List |
| `join(iterable)` | Joins iterable elements into a string | ✅ New string |

### Examples
#### `split(separator)`
```python
text = "hello world python"
print(text.split())  # Output: ["hello", "world", "python"]
```

#### `join(iterable)`
```python
words = ["hello", "world"]
print(" ".join(words))  # Output: "hello world"
```

---

## 4. Checking String Properties

| Method | Purpose | Returns |
|--------|---------|---------|
| `isalnum()` | Checks if all characters are alphanumeric | ✅ Boolean |
| `isalpha()` | Checks if all characters are alphabetic | ✅ Boolean |
| `isdigit()` | Checks if all characters are digits | ✅ Boolean |
| `isspace()` | Checks if string contains only whitespace | ✅ Boolean |

### Examples
#### `isalnum()`
```python
text = "hello123"
print(text.isalnum())  # Output: True
```

#### `isalpha()`
```python
text = "hello"
print(text.isalpha())  # Output: True
```

#### `isdigit()`
```python
text = "12345"
print(text.isdigit())  # Output: True
```

#### `isspace()`
```python
text = "   "
print(text.isspace())  # Output: True
```

---

## Summary
- **Modifying**: `upper()`, `lower()`, `title()`, `capitalize()`, `strip()`, `replace()`, `format()`, `encode()`
- **Searching**: `find()`, `index()`, `count()`, `startswith()`, `endswith()`
- **Splitting & Joining**: `split()`, `join()`
- **Checking Properties**: `isalnum()`, `isalpha()`, `isdigit()`, `isspace()`

