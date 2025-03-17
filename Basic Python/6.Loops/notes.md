# Loops in Python (With Advanced Topics)

## Introduction
Loops in Python are used for executing a block of code multiple times. Python provides two main types of loops:
1. **For Loop**
2. **While Loop**

Loops help automate repetitive tasks, making the code efficient and easy to manage.

---

## Types of Loops

### 1. For Loop
A `for` loop is used when the number of iterations is known beforehand. It is commonly used to iterate over sequences like lists, tuples, dictionaries, strings, etc.

#### Syntax:
```python
for variable in sequence:
    # code block
```

#### Example:
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

#### Using `range()` in `for` loop:
```python
for i in range(5):  # Generates numbers from 0 to 4
    print(i)
```

#### Iterating over a Dictionary:
```python
dict_data = {"name": "Alice", "age": 25, "city": "New York"}
for key, value in dict_data.items():
    print(f"{key}: {value}")
```

---

### 2. While Loop
A `while` loop is used when the number of iterations is not known and depends on a condition.

#### Syntax:
```python
while condition:
    # code block
```

#### Example:
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

---

## Loop Control Statements
Loop control statements help in modifying the flow of loops.

### 1. `break` Statement
Used to exit a loop immediately.

#### Example:
```python
for num in range(10):
    if num == 5:
        break  # Terminates the loop
    print(num)
```

### 2. `continue` Statement
Used to skip the current iteration and move to the next.

#### Example:
```python
for num in range(5):
    if num == 3:
        continue  # Skips iteration when num == 3
    print(num)
```

### 3. `pass` Statement
Used as a placeholder for future code.

#### Example:
```python
for i in range(3):
    pass  # Does nothing but maintains structure
```

---

## Nested Loops
Loops inside another loop are called nested loops.

#### Example:
```python
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")
```

---

## Advanced Looping Concepts

### 1. Using `else` with Loops
In Python, `else` can be used with loops and executes only if the loop is not terminated by `break`.

#### Example:
```python
for num in range(5):
    if num == 6:
        break
else:
    print("Loop completed without break")
```

### 2. List Comprehension in Loops
List comprehensions provide a compact way to create lists.

#### Example:
```python
squares = [x**2 for x in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]
```

### 3. Looping with Enumerate
`enumerate()` adds an index while looping through a sequence.

#### Example:
```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index}: {name}")
```

### 4. Using Zip Function in Loops
`zip()` allows iterating over multiple sequences simultaneously.

#### Example:
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### 5. Itertools for Advanced Looping
Python’s `itertools` module provides powerful looping tools.

#### Example of `itertools.cycle()`:
```python
import itertools
colors = ["red", "green", "blue"]
cycle_colors = itertools.cycle(colors)

for _ in range(6):
    print(next(cycle_colors))  # Cycles through colors repeatedly
```

#### Example of `itertools.product()`:
```python
from itertools import product
list1 = [1, 2]
list2 = ["A", "B"]

for pair in product(list1, list2):
    print(pair)
```

---

## Conclusion
Loops in Python provide an efficient way to iterate through sequences and perform repetitive tasks. Advanced concepts like `enumerate()`, `zip()`, and `itertools` enhance looping capabilities. Mastering loops allows for writing optimized and readable code.

