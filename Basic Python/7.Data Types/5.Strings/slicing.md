# Python Slicing - Detailed Notes

## 📌 What is Slicing in Python?
**Slicing** is a technique in Python used to extract a specific portion (or subset) of a sequence (like strings, lists, tuples, etc.) using the slice notation:

```python
sequence[start:stop:step]
```

### ✅ Explanation of Parameters:
1. **start** → The starting index (included). Default is `0`.
2. **stop** → The ending index (excluded). Default is the length of the sequence.
3. **step** → The step size (how many elements to skip). Default is `1`.

---

## 📌 Examples of Slicing

### 🔹 Slicing a String
```python
text = "PythonProgramming"

# Basic slicing
print(text[0:6])   # Output: Python  (From index 0 to 5)
print(text[:6])    # Output: Python  (Start is omitted, so starts from 0)
print(text[6:])    # Output: Programming  (Ends at the last index)

# Using step
print(text[::2])   # Output: PtoPormig  (Every second character)
print(text[::-1])  # Output: gnimmargorPnohtyP  (Reverses the string)
```

### 🔹 Slicing a List
```python
numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])  # Output: [20, 30, 40]
print(numbers[::-1]) # Output: [60, 50, 40, 30, 20, 10] (Reverses the list)
print(numbers[::2])  # Output: [10, 30, 50] (Skipping one element)
```

### 🔹 Slicing a Tuple
```python
tuple_data = (100, 200, 300, 400, 500)

print(tuple_data[:3])  # Output: (100, 200, 300)
print(tuple_data[-3:]) # Output: (300, 400, 500)
```

---

## 📌 Advanced Slicing Concepts

### 🔹 Reverse Slicing
```python
text = "Python"
print(text[::-1])  # Output: nohtyP  (Reverse a string)
```

### 🔹 Slicing with Negative Indexing
```python
numbers = [10, 20, 30, 40, 50]
print(numbers[-4:-1])  # Output: [20, 30, 40]
```

### 🔹 Using `slice()` Function
```python
text = "HelloWorld"
obj = slice(2, 8, 2)
print(text[obj])  # Output: loW
```

---

## 📌 Key Points About Slicing
- Works on **strings, lists, tuples**, and other sequence types.
- Does **not modify** the original sequence; instead, it creates a **new copy**.
- Supports **negative indexing** (e.g., `[::-1]` for reversal).
- Omitting `start` or `stop` uses default values (`0` and `len(sequence)`, respectively).

---
🎯 **Slicing is a powerful feature in Python for manipulating sequences efficiently! Mastering it improves coding skills.** 🚀

