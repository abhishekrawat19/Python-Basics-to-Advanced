# Python List - Detailed Notes

## 📌 Introduction to Lists
A **list** is a built-in data structure in Python that allows you to store multiple values in a single variable. Lists are **ordered**, **mutable**, and **allow duplicate values**.

### ✅ Characteristics of Lists:
- **Ordered**: Elements maintain their insertion order.
- **Mutable**: Elements can be changed after creation.
- **Indexed**: Accessed using index values (starting from 0).
- **Allows Duplicates**: Can store multiple occurrences of the same value.
- **Supports Heterogeneous Data**: Can contain different data types (e.g., integers, strings, lists).

## 📌 Creating a List
Lists can be created in multiple ways:

```python
# Empty list
my_list = []

# List with elements
numbers = [1, 2, 3, 4, 5]

# List with mixed data types
mixed_list = [1, "hello", 3.14, [10, 20]]

# Using list constructor
new_list = list((10, 20, 30))
```

## 📌 Accessing Elements
Elements in a list can be accessed using **indexing** and **slicing**.

```python
my_list = [10, 20, 30, 40, 50]

# Access by index
print(my_list[0])   # Output: 10
print(my_list[-1])  # Output: 50 (last element)

# Slicing
print(my_list[1:4])  # Output: [20, 30, 40]
print(my_list[:3])   # Output: [10, 20, 30]
print(my_list[::2])  # Output: [10, 30, 50]
```

## 📌 Modifying a List
Since lists are **mutable**, we can modify them using assignment or built-in methods.

```python
my_list = [10, 20, 30]

# Modify an element
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30]

# Append a new element
my_list.append(40)
print(my_list)  # Output: [10, 25, 30, 40]

# Extend with another list
my_list.extend([50, 60])
print(my_list)  # Output: [10, 25, 30, 40, 50, 60]
```

## 📌 List Methods
### 🔹 Adding Elements
```python
list1 = [1, 2, 3]

list1.append(4)        # Adds single element at the end
list1.insert(1, 10)    # Inserts element at a specific index
list1.extend([5, 6])   # Merges another list
```

### 🔹 Removing Elements
```python
list1.pop()        # Removes and returns the last element
list1.pop(1)       # Removes and returns element at index 1
list1.remove(2)    # Removes the first occurrence of 2
list1.clear()      # Removes all elements
```

### 🔹 Sorting and Reversing
```python
numbers = [5, 1, 8, 3]
numbers.sort()      # Sorts in ascending order
numbers.sort(reverse=True)  # Sorts in descending order
numbers.reverse()   # Reverses the list
```

### 🔹 Copying a List
```python
new_list = numbers.copy()  # Creates a shallow copy
```

## 📌 Advanced List Concepts

### 1️⃣ **List Comprehension**
A concise way to create lists using loops.

```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
```

### 2️⃣ **Filtering with List Comprehension**
```python
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8]
```

### 3️⃣ **Nested Lists (2D Lists)**
```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[1][2])  # Output: 6
```

### 4️⃣ **Unpacking Lists**
```python
my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)  # Output: 1 2 3
```

### 5️⃣ **List as Stack (LIFO)**
```python
stack = []
stack.append(10)
stack.append(20)
print(stack.pop(1))  # Output: 20
```

### 6️⃣ **List as Queue (FIFO)**
```python
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())  # Output: 1
```

### 7️⃣ **Using `zip()` with Lists**
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
pairs = list(zip(names, ages))
print(pairs)  # Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

### 8️⃣ **Using `map()` with Lists**
```python
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]
```

## 📌 Summary
- Lists are **ordered, mutable**, and allow duplicate values.
- Various operations like **indexing, slicing, adding, removing, and modifying** are possible.
- Advanced operations include **list comprehension, nested lists, unpacking, stacks, queues, and functional programming techniques**.

---
🎯 **Lists are one of the most powerful data structures in Python! Mastering them helps in handling data efficiently.** 🚀

