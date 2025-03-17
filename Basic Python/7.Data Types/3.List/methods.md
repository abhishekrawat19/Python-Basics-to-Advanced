# List Methods in Python (With Code & Output)

## 1. Adding Elements to a List

| Method | Description | Returns | Error if Invalid? |
|--------|------------|---------|------------------|
| `append(value)` | Adds a single element at the end | ❌ No | ❌ No |
| `extend(iterable)` | Adds all elements from an iterable | ❌ No | ❌ No |
| `insert(index, value)` | Inserts an element at a specific index | ❌ No | ❌ No |

### Examples
#### `append(value)`
```python
my_list = [10, 20, 30]
my_list.append(40)
print(my_list)  # Output: [10, 20, 30, 40]
```

#### `extend(iterable)`
```python
my_list = [10, 20]
my_list.extend([30, 40])
print(my_list)  # Output: [10, 20, 30, 40]
```

#### `insert(index, value)`
```python
my_list = [10, 30, 40]
my_list.insert(1, 20)
print(my_list)  # Output: [10, 20, 30, 40]
```

---

## 2. Removing Elements from a List

| Method | Removes by | Returns Removed Item? | Error if Not Found? |
|--------|-----------|----------------------|---------------------|
| `remove(value)` | First occurrence of a **value** | ❌ No | ✅ Yes (`ValueError`) |
| `pop(index)` | **Index** (default last) | ✅ Yes | ✅ Yes (`IndexError`) |
| `del list[index]` | **Index** or entire list | ❌ No | ✅ Yes (`IndexError`) |
| `clear()` | **All elements** | ❌ No | ❌ No |

### Examples
#### `remove(value)`
```python
numbers = [1, 2, 3, 4, 2]
numbers.remove(2)  # Removes the first 2
print(numbers)  # Output: [1, 3, 4, 2]
```

#### `pop(index)`
```python
numbers = [10, 20, 30, 40]
removed_item = numbers.pop(2)
print(numbers)  # Output: [10, 20, 40]
print(removed_item)  # Output: 30
```

#### `del` (Delete by Index or Entire List)
```python
numbers = [10, 20, 30, 40]
del numbers[1]
print(numbers)  # Output: [10, 30, 40]
```

#### `clear()`
```python
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)  # Output: []
```

---

## 3. Searching for Elements in a List

| Method | Purpose | Returns |
|--------|---------|---------|
| `index(value)` | Finds index of the first occurrence of `value` | ✅ Yes |
| `count(value)` | Counts occurrences of `value` | ✅ Yes |

### Examples
#### `index(value)`
```python
numbers = [10, 20, 30, 40]
print(numbers.index(30))  # Output: 2
```

#### `count(value)`
```python
numbers = [1, 2, 2, 3, 4, 2]
print(numbers.count(2))  # Output: 3
```

---

## 4. Sorting and Reversing Lists

| Method | Purpose | Modifies List? |
|--------|---------|---------------|
| `sort()` | Sorts the list in ascending order | ✅ Yes |
| `reverse()` | Reverses the list order | ✅ Yes |
| `sorted(list)` | Returns a sorted copy | ❌ No |

### Examples
#### `sort()`
```python
numbers = [4, 2, 3, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 3, 4]
```

#### `reverse()`
```python
numbers = [1, 2, 3, 4]
numbers.reverse()
print(numbers)  # Output: [4, 3, 2, 1]
```

#### `sorted(list)`
```python
numbers = [4, 2, 3, 1]
print(sorted(numbers))  # Output: [1, 2, 3, 4]
print(numbers)  # Output: [4, 2, 3, 1] (Unchanged)
```

---

## 5. Copying a List

| Method | Purpose |
|--------|---------|
| `copy()` | Creates a shallow copy |

### Example
```python
original = [1, 2, 3]
copy_list = original.copy()
print(copy_list)  # Output: [1, 2, 3]
```

---

## Summary
- **Adding Elements**: `append()`, `extend()`, `insert()`
- **Removing Elements**: `remove()`, `pop()`, `del`, `clear()`
- **Searching**: `index()`, `count()`
- **Sorting & Reversing**: `sort()`, `reverse()`, `sorted()`
- **Copying**: `copy()`



AEIRPDCICSRSC
LIST AIE CRDP CI 