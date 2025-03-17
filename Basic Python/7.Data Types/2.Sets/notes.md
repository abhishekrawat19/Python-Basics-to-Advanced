# **Set Data Type in Python**

## **Introduction to Sets**
A **set** in Python is an **unordered, mutable, iterable** collection of **unique elements**. Sets are useful when we need to store multiple items but do not want duplicate values.

### **Key Characteristics of Sets:**
- **Unordered** – Elements do not maintain a specific order.
- **Mutable** – You can add or remove elements.
- **Unique Elements** – No duplicate values are allowed.
- **Heterogeneous** – Can store different data types.
- **Unindexed** – Cannot access elements using an index.
- **Uses Hashing** – Optimized for fast membership tests.

---

## **Creating a Set in Python**
A set can be created using **curly braces `{}`** or the built-in **`set()`** function.

```python
# Creating a set
my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}

# Creating an empty set
empty_set = set()  # {} creates an empty dictionary
print(type(empty_set))  # Output: <class 'set'>
```

---

## **Set Methods in Python**
Python provides several built-in methods for performing operations on sets.

### **1. Adding Elements to a Set**
```python
s = {1, 2, 3}
s.add(4)  # Adds a single element
s.update([5, 6, 7])  # Adds multiple elements
print(s)  # Output: {1, 2, 3, 4, 5, 6, 7}
```

### **2. Removing Elements from a Set**
```python
s.remove(3)  # Removes 3, raises an error if not found
s.discard(2)  # Removes 2, no error if not found
s.pop()  # Removes a random element
s.clear()  # Removes all elements
print(s)  # Output: set()
```

### **3. Set Operations (Mathematical Set Theory)**
```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union -> {1, 2, 3, 4, 5}
print(A & B)  # Intersection -> {3}
print(A - B)  # Difference -> {1, 2}
print(A ^ B)  # Symmetric Difference -> {1, 2, 4, 5}
```

### **4. Other Useful Set Methods**
| **Method**                | **Description** |
|---------------------------|----------------|
| `copy()`                  | Returns a shallow copy of the set |
| `issubset(set2)`          | Checks if the set is a subset of another set |
| `issuperset(set2)`        | Checks if the set is a superset of another set |
| `isdisjoint(set2)`        | Checks if two sets have no common elements |
| `difference_update(set2)` | Removes elements found in another set |
| `intersection_update(set2)` | Keeps only elements found in both sets |
| `symmetric_difference_update(set2)` | Updates set with elements that are in either but not both |

---

## **Frozen Sets (Immutable Sets)**
A **frozen set** is an immutable version of a set.
```python
fs = frozenset([1, 2, 3, 4])
print(fs)  # Output: frozenset({1, 2, 3, 4})
```
> **Frozen sets cannot be modified** after creation.

---

## **Use Cases of Sets in Python**
- **Removing duplicates** from a list.
- **Fast membership testing** (`in` operator).
- **Mathematical operations** like union, intersection, and difference.

---

## **Set vs Other Data Types**
| **Property**   | **Set** | **List** | **Tuple** | **Dictionary** |
|---------------|--------|---------|---------|--------------|
| Mutable      | ✅ | ✅ | ❌ | ✅ |
| Ordered      | ❌ | ✅ | ✅ | ✅ (Python 3.7+) |
| Duplicates   | ❌ | ✅ | ✅ | Keys ❌, Values ✅ |
| Indexing     | ❌ | ✅ | ✅ | ✅ (by keys) |

---

## **Conclusion**
- **Sets** are **unordered collections** of **unique elements**.
- They provide **fast lookups** and support **mathematical operations**.
- Use **frozen sets** if immutability is required.
- Sets are **not suitable** where element order matters.
