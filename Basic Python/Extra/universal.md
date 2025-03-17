# Iterable vs Iterator in Python

## **1. What is an Iterable?**
An **Iterable** is any Python object that can return its elements one at a time. It implements the `__iter__()` method, which returns an **Iterator**.

### **Examples of Iterables**
- Lists: `[1, 2, 3]`
- Tuples: `(1, 2, 3)`
- Strings: `'hello'`
- Dictionaries: `{'a': 1, 'b': 2}`
- Sets: `{1, 2, 3}`
- Custom objects that implement `__iter__()`

### **Example of an Iterable**
```python
my_list = [10, 20, 30]
for item in my_list:  # The iterable provides elements one by one
    print(item)
```

## **2. What is an Iterator?**
An **Iterator** is an object that keeps track of where it is in a sequence. It implements two special methods:
1. `__iter__()`: Returns itself (the iterator object)
2. `__next__()`: Returns the next item and moves forward in the sequence. Raises `StopIteration` when elements are exhausted.

### **Example of an Iterator**
```python
my_list = [10, 20, 30]
iterator = iter(my_list)  # Converting list to an iterator

print(next(iterator))  # Output: 10
print(next(iterator))  # Output: 20
print(next(iterator))  # Output: 30
print(next(iterator))  # Raises StopIteration
```

## **3. Key Differences: Iterable vs Iterator**
| Feature      | **Iterable** | **Iterator** |
|-------------|-------------|-------------|
| **Definition** | An object that can return an iterator. | An object that keeps state and returns the next value. |
| **Methods** | Implements `__iter__()` | Implements both `__iter__()` and `__next__()` |
| **State Tracking** | No state tracking | Keeps track of its current position |
| **Usage** | Can be looped over (for-loop) | Must use `next()` to retrieve elements manually |
| **Examples** | List, Tuple, String, Dict, Set | Object returned by `iter(iterable)` |

## **4. Converting an Iterable to an Iterator**
You can use the `iter()` function to convert an iterable into an iterator.
```python
numbers = [1, 2, 3]
it = iter(numbers)  # Now 'it' is an iterator
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # Raises StopIteration
```

## **5. Creating a Custom Iterator**
We can define a class that implements `__iter__()` and `__next__()`.

### **Example: Custom Iterator that Generates Even Numbers**
```python
class EvenNumbers:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self  # Returns itself as an iterator
    
    def __next__(self):
        if self.current > self.max:
            raise StopIteration
        self.current += 2
        return self.current - 2

# Using the custom iterator
even_iter = EvenNumbers(10)
for num in even_iter:
    print(num)  # Output: 0, 2, 4, 6, 8, 10
```

## **6. Iterators are Exhaustible**
Once an iterator is consumed, it cannot be reset unless explicitly recreated.
```python
numbers = [5, 10, 15]
it = iter(numbers)
print(next(it))  # 5
print(next(it))  # 10
print(next(it))  # 15
print(next(it))  # Raises StopIteration (No more items)
```

## **7. Generators as Iterators**
A **generator** is a special type of iterator that yields values using `yield` instead of `return`. Generators are memory-efficient.

### **Example: Generator Function**
```python
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # Raises StopIteration
```

## **8. When to Use Iterables vs Iterators?**
- **Use Iterables** when you want to loop over data multiple times (e.g., lists, tuples).
- **Use Iterators** when you need to process elements one at a time and don’t want to store everything in memory (e.g., large datasets, streaming data).

---
### **Summary**
- **Iterable**: Can return an iterator but doesn’t track position.
- **Iterator**: Tracks position and produces values one by one with `next()`.
- **Iterators are consumed once and can’t be restarted unless recreated.**
- **Generators are iterators that use `yield` and are more memory-efficient.**

Would you like more clarifications on this topic? 🚀

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

