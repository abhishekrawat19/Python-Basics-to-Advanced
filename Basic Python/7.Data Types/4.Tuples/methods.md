# Tuple Methods in Python (With Code & Output)

## 1. Accessing & Counting Elements

| Method | Purpose | Returns |
|--------|---------|---------|
| `count(value)` | Counts occurrences of a value in the tuple | ✅ Count |
| `index(value)` | Finds the first index of a value | ✅ Index (or raises error) |

### Examples
#### `count(value)`
```python
tuple1 = (1, 2, 2, 3, 4, 2)
print(tuple1.count(2))  # Output: 3
```

#### `index(value)`
```python
tuple1 = (10, 20, 30, 40)
print(tuple1.index(30))  # Output: 2

# tuple1.index(50)  # Error: ValueError
```

---

## 2. Tuple Operations

| Operation | Purpose | Example | Returns |
|-----------|---------|---------|---------|
| `+` | Concatenates two tuples | `(1, 2) + (3, 4)` | ✅ New tuple |
| `*` | Repeats tuple elements | `("a",) * 3` | ✅ New tuple |
| `len()` | Finds tuple length | `len((1, 2, 3))` | ✅ Integer |
| `in` | Checks if an element exists | `3 in (1, 2, 3)` | ✅ Boolean |

### Examples
#### Concatenation (`+`)
```python
tuple1 = (1, 2)
tuple2 = (3, 4)
print(tuple1 + tuple2)  # Output: (1, 2, 3, 4)
```

#### Repetition (`*`)
```python
tuple1 = ("a",)
print(tuple1 * 3)  # Output: ('a', 'a', 'a')
```

#### Length (`len()`)
```python
tuple1 = (10, 20, 30)
print(len(tuple1))  # Output: 3
```

#### Membership (`in`)
```python
tuple1 = (1, 2, 3)
print(3 in tuple1)  # Output: True
```

---

## 3. Tuple Unpacking

| Feature | Purpose | Example |
|---------|---------|---------|
| Tuple unpacking | Assigns tuple elements to variables | `a, b = (10, 20)` |

### Example
```python
tuple1 = (10, 20, 30)
a, b, c = tuple1
print(a, b, c)  # Output: 10 20 30
```

---

## Summary
- **Accessing Elements**: `count()`, `index()`
- **Operations**: Concatenation (`+`), Repetition (`*`), Length (`len()`), Membership (`in`)
- **Tuple Unpacking**: Assign tuple values to variables

