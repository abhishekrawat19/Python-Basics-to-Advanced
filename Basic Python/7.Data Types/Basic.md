# Data Types in Python

Python provides various data types to store and manipulate different kinds of data. These data types can be broadly categorized into **Mutable** and **Immutable** types.

## 1. Mutable and Immutable Data Types

- **Mutable Data Types**: These are the data types whose values can be changed after they are created.
  - Examples: `list`, `dict`, `set`

- **Immutable Data Types**: These are the data types whose values cannot be changed once they are created.
  - Examples: `int`, `float`, `str`, `tuple`, `bool`,`complex`

---

## 2. Built-in Data Types in Python
Python has several built-in data types categorized as follows:

### a) Numeric Types
Used to store numeric values.
- **int**: Integer values (e.g., `10`, `-5`)
- **float**: Decimal values (e.g., `10.5`, `-3.14`)
- **complex**: Complex numbers (e.g., `2 + 3j`)

### b) Sequence Types
Used to store a collection of items.
- **str** (String): A sequence of characters (e.g., `'Hello'`, `"Python"`)
- **list**: Ordered and mutable collection (e.g., `[1, 2, 3]`)
- **tuple**: Ordered and immutable collection (e.g., `(1, 2, 3)`)

### c) Set Types
Used to store unordered collections of unique elements.
- **set**: Mutable, unordered collection of unique items (e.g., `{1, 2, 3}`)
- **frozenset**: Immutable version of a set (e.g., `frozenset({1, 2, 3})`)

### d) Mapping Type
Used to store key-value pairs.
- **dict** (Dictionary): A collection of key-value pairs (e.g., `{'name': 'John', 'age': 25}`)

### e) Boolean Type
Used to store True or False values.
- **bool**: Represents `True` or `False` values (e.g., `True`, `False`)

### f) Binary Types
Used to store binary data.
- **bytes**: Immutable sequence of bytes (e.g., `b'hello'`)
- **bytearray**: Mutable sequence of bytes
- **memoryview**: Memory-efficient object to handle binary data

---

## 3. Type Conversion in Python
Python provides functions to convert data types:

- **Implicit Conversion (Automatic Type Conversion)**: Performed automatically by Python (e.g., `int` to `float`)
  ```python
  x = 10   # int
  y = 2.5  # float
  result = x + y  # Implicitly converts x to float
  print(result, type(result))  # Output: 12.5 <class 'float'>
  ```
- **Explicit Conversion (Type Casting)**: Manually done using functions like `int()`, `float()`, `str()`
  ```python
  a = "100"
  b = int(a)  # Converts string to integer
  print(b, type(b))  # Output: 100 <class 'int'>
  ```

---

## 4. Checking Data Type
Python provides the `type()` function to check the data type of a variable.
```python
x = 10
print(type(x))  # Output: <class 'int'>
```

---

