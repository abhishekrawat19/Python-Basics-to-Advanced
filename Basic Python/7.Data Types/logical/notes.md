# Removing Elements in Python

## 1. Removing Elements from Lists

| Method | Removes by | Returns Removed Item? | Error if Not Found? |
|--------|-----------|----------------------|---------------------|
| `remove(value)` | First occurrence of a **value** | ❌ No | ✅ Yes (`ValueError`) |
| `pop(index)` | **Index** (default last) | ✅ Yes | ✅ Yes (`IndexError`) |
| `del list[index]` | **Index** or entire list | ❌ No | ✅ Yes (`IndexError`) |
| `clear()` | **All elements** | ❌ No | ❌ No |
| List comprehension | Condition-based filtering | ❌ No | ❌ No |

### Examples
#### `remove(value)`
```python
numbers = [1, 2, 3, 4, 2]
numbers.remove(2)  # Removes the first 2
print(numbers)  # Output: [1, 3, 4, 2]

numbers.remove(10)  # Error: Value not in list
```
**Error Output:**
```
ValueError: list.remove(x): x not in list
```

#### `pop(index)`
```python
numbers = [10, 20, 30, 40]
removed_item = numbers.pop(2)  # Removes item at index 2
print(numbers)  # Output: [10, 20, 40]
print(removed_item)  # Output: 30

numbers.pop(10)  # Error: Index out of range
```
**Error Output:**
```
IndexError: pop index out of range
```

#### `del` (Delete by Index or Entire List)
```python
numbers = [10, 20, 30, 40]
del numbers[1]  # Removes element at index 1
print(numbers)  # Output: [10, 30, 40]

del numbers[10]  # Error: Index out of range
```
**Error Output:**
```
IndexError: list assignment index out of range
```

#### `clear()`
```python
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)  # Output: []
```

#### List Comprehension (Remove Items Conditionally)
```python
numbers = [1, 2, 3, 4, 5, 6]
numbers = [num for num in numbers if num % 2 == 0]  # Keeps only even numbers
print(numbers)  # Output: [2, 4, 6]
```

---

## 2. Removing Elements from Sets

| Method | Removes by | Error if Not Found? | Returns Removed Item? |
|--------|-----------|---------------------|-----------------------|
| `remove(value)` | **Value** | ✅ Yes (`KeyError`) | ❌ No |
| `discard(value)` | **Value** | ❌ No | ❌ No |
| `pop()` | **Random item** (unordered) | ✅ Yes (`KeyError` if empty) | ✅ Yes |
| `clear()` | **All elements** | ❌ No | ❌ No |

### Examples
#### `remove()` (Raises Error if Not Found)
```python
s = {1, 2, 3}
s.remove(2)  # Removes 2
print(s)  # Output: {1, 3}

s.remove(10)  # Error: Value not in set
```
**Error Output:**
```
KeyError: 10
```

#### `discard()` (No Error if Not Found)
```python
s = {1, 2, 3}
s.discard(2)  # Removes 2
s.discard(10)  # No error if 10 is not in the set
print(s)  # Output: {1, 3}
```

#### `pop()` (Removes and Returns a Random Element)
```python
s = {10, 20, 30}
removed_item = s.pop()  # Removes a random element
print(s)  # Output: Remaining elements
print(removed_item)  # Output: Removed element

empty_set = set()
empty_set.pop()  # Error: Cannot pop from an empty set
```
**Error Output:**
```
KeyError: 'pop from an empty set'
```

#### `clear()` (Remove All Elements)
```python
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()
```

---

## Summary
- **For lists**: `remove()`, `pop()`, `del`, `clear()`, list comprehension
- **For sets**: `remove()`, `discard()`, `pop()`, `clear()`

