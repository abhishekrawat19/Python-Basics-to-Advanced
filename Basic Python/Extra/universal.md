# Universal Methods in Python

## 🔹 Introduction
Universal methods in Python are **functions that work across multiple data types**, including strings, lists, tuples, sets, and dictionaries. These methods are applicable to **all iterable objects** and help perform operations like sorting, finding the length, and filtering elements efficiently.

---

## 🔹 List of Universal Methods in Python

| **Method**  | **Works On** | **Description** |
|------------|------------|----------------|
| `len()` | All Iterables | Returns the number of elements. |
| `sorted()` | Strings, Lists, Tuples, Sets, Dict Keys | Returns a sorted list. |
| `min()` | Strings, Lists, Tuples, Sets, Dict Keys | Returns the smallest element. |
| `max()` | Strings, Lists, Tuples, Sets, Dict Keys | Returns the largest element. |
| `sum()` | Lists, Tuples, Sets | Returns the sum of numeric elements. |
| `any()` | Strings, Lists, Tuples, Sets, Dicts | Returns `True` if any element is `True`. |
| `all()` | Strings, Lists, Tuples, Sets, Dicts | Returns `True` if all elements are `True`. |
| `enumerate()` | Strings, Lists, Tuples, Sets, Dicts | Returns index-value pairs as a tuple. |
| `zip()` | Multiple Iterables | Combines multiple iterables element-wise. |
| `map()` | Strings, Lists, Tuples, Sets | Applies a function to all elements. |
| `filter()` | Strings, Lists, Tuples, Sets | Filters elements based on a condition. |

---

## 🔹 Explanation with Examples

### ✅ **1. `len()` – Works on All Iterables**
```python
print(len("Python"))      # 6
print(len([1, 2, 3]))     # 3
print(len((1, 2, 3)))     # 3
print(len({1, 2, 3}))     # 3
print(len({"a": 1, "b": 2})) # 2 (Dictionary keys count)
```

---

### ✅ **2. `sorted()` – Works on Strings, Lists, Tuples, Sets, and Dict Keys**
```python
print(sorted("python"))        # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted([3, 1, 2]))       # [1, 2, 3]
print(sorted((3, 1, 2)))       # [1, 2, 3]
print(sorted({3, 1, 2}))       # [1, 2, 3]
print(sorted({"b": 2, "a": 1})) # ['a', 'b'] (Keys are sorted)
```

---

### ✅ **3. `min()` and `max()` – Work on All Ordered Iterables**
```python
print(min("python"))         # 'h'
print(min([3, 1, 2]))        # 1
print(min((3, 1, 2)))        # 1
print(min({3, 1, 2}))        # 1
print(min({"b": 2, "a": 1})) # 'a' (Works on keys)
```

---

### ✅ **4. `sum()` – Works on Numeric Lists, Tuples, Sets**
```python
print(sum([1, 2, 3]))     # 6
print(sum((1, 2, 3)))     # 6
print(sum({1, 2, 3}))     # 6
```
🚫 **Does NOT work on strings or dictionaries.**

---

### ✅ **5. `any()` and `all()` – Work on All Iterables**
```python
print(any([0, 1, 0]))     # True (Because at least one element is True)
print(any(""))            # False (Empty iterable)
print(all([1, 2, 3]))     # True (All are True)
print(all([1, 0, 3]))     # False (0 is False)
```

---

### ✅ **6. `enumerate()` – Works on All Iterables**
The `enumerate()` function assigns an **index to each item** in an iterable and returns it as a tuple. This is useful when looping through elements while keeping track of their position.

#### 📌 **Why Use `enumerate()`?**
- It **avoids manually managing an index counter**.
- It **makes loops more readable and efficient**.
- Works on **all iterable types (lists, tuples, strings, sets, dictionaries)**.

#### ✅ **Example:** Using `enumerate()` with a List
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
```
🔹 **Output:**
```
0 apple
1 banana
2 cherry
```

#### ✅ **Example:** Using `enumerate()` with a String
```python
for index, char in enumerate("hello"):
    print(index, char)
```
🔹 **Output:**
```
0 h
1 e
2 l
3 l
4 o
```

---

### ✅ **7. `zip()` – Works on Multiple Iterables**
```python
list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(list(zip(list1, list2)))  
# [(1, 'a'), (2, 'b'), (3, 'c')]
```

---

### ✅ **8. `map()` – Works on All Iterables**
```python
print(list(map(str.upper, "hello")))  
# ['H', 'E', 'L', 'L', 'O']
```

---

### ✅ **9. `filter()` – Works on All Iterables**
```python
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  
# [2, 4]
```

---

## 🔹 Conclusion
✔️ **Universal methods work on multiple data types** (strings, lists, tuples, sets, and dictionaries).  
✔️ **Common universal methods:** `len()`, `sorted()`, `min()`, `max()`, `sum()`, `any()`, `all()`, `enumerate()`, `zip()`, `map()`, `filter()`.  
✔️ **Some methods like `sum()` don’t work on non-numeric data types (strings, dicts).**  

Let me know if you need more details! 🚀

