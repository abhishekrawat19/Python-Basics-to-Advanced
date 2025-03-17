# Python Dictionary - Detailed Notes

## 📌 Introduction to Dictionaries
A **dictionary** in Python is an **unordered**, **mutable**, and **indexed** collection that stores data in **key-value pairs**. It provides an efficient way to organize and retrieve data.

### ✅ Characteristics of Dictionaries:
- **Unordered**: No guaranteed order (prior to Python 3.7, now insertion order is preserved).
- **Mutable**: Can be modified after creation.
- **Key-Value Pairing**: Each key maps to a corresponding value.
- **Keys Must Be Unique**: Duplicate keys are not allowed.
- **Keys Must Be Immutable**: Can be strings, numbers, or tuples, but not lists or other dictionaries.

## 📌 Creating a Dictionary
Dictionaries can be created using curly braces `{}` or the `dict()` constructor.

```python
# Empty dictionary
my_dict = {}

# Dictionary with key-value pairs
student = {"name": "Alice", "age": 25, "course": "Python"}

# Using the dict() constructor
employee = dict(id=101, name="John", salary=50000)
```

## 📌 Accessing Dictionary Elements
We can access dictionary values using **keys**.

```python
student = {"name": "Alice", "age": 25, "course": "Python"}

# Accessing values
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 25

# Handling missing keys
print(student.get("grade", "Not Assigned"))  # Output: Not Assigned
```

## 📌 Modifying a Dictionary
Since dictionaries are **mutable**, we can modify them easily.

```python
student["age"] = 26  # Update value
student["grade"] = "A"  # Add new key-value pair
print(student)
```

## 📌 Dictionary Methods

### 🔹 Adding and Updating Elements
```python
student.update({"city": "New York", "grade": "A"})
```

### 🔹 Removing Elements
```python
del student["course"]  # Remove a specific key
removed_value = student.pop("age")  # Remove and return the value
student.clear()  # Remove all elements
```

### 🔹 Iterating Over a Dictionary
```python
# Iterate over keys
dict1 = {"a": 1, "b": 2, "c": 3}
for key in dict1:
    print(key, "->", dict1[key])
```

## 📌 Advanced Dictionary Concepts

### 1️⃣ **Using `.items()` Method**
The `.items()` method returns a view object containing key-value pairs, allowing efficient iteration.
```python
student = {"name": "Alice", "age": 25, "course": "Python"}
for key, value in student.items():
    print(key, "->", value)
```

### 2️⃣ **Dictionary Comprehension**
A concise way to create dictionaries.
```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)  # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### 3️⃣ **Merging Dictionaries (Python 3.9+)**
```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = dict1 | dict2  # Overwrites duplicate keys
```

### 4️⃣ **Using `defaultdict` (from `collections` module)**
Automatically initializes missing keys with a default value.
```python
from collections import defaultdict
dd = defaultdict(int)
dd["a"] += 1  # No KeyError, default value is 0
```

### 5️⃣ **Using `Counter` for Frequency Counting**
```python
from collections import Counter
word_counts = Counter("banana")
print(word_counts)  # Output: {'b': 1, 'a': 3, 'n': 2}
```

## 📌 Summary
- **Dictionaries store key-value pairs efficiently.**
- **`.items()` allows easy key-value iteration.**
- **Advanced techniques** include `defaultdict`, `Counter`, `dict comprehension`, and `dictionary merging`.

---
💡 **Mastering dictionaries enhances Python efficiency!** 🚀

