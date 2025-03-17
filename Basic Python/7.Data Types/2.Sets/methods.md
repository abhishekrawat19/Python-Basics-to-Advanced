# Set Methods in Python (With Code & Output)

## 1. Adding & Removing Elements

| Method | Purpose | Returns |
|--------|---------|---------|
| `add(value)` | Adds an element to the set | ✅ Modifies in-place |
| `remove(value)` | Removes an element, raises error if not found | ✅ Modifies in-place |
| `discard(value)` | Removes an element, does nothing if not found | ✅ Modifies in-place |
| `pop()` | Removes & returns an arbitrary element | ✅ Element |
| `clear()` | Removes all elements from the set | ✅ Modifies in-place |

### Examples
#### `add(value)`
```python
s = {1, 2, 3}
s.add(4)
print(s)  # Output: {1, 2, 3, 4}
```

#### `remove(value)`
```python
s = {1, 2, 3}
s.remove(2)
print(s)  # Output: {1, 3}

# s.remove(5)  # Error: KeyError
```

#### `discard(value)`
```python
s = {1, 2, 3}
s.discard(2)
print(s)  # Output: {1, 3}

s.discard(5)  # No error, set remains unchanged
```

#### `pop()`
```python
s = {1, 2, 3}
print(s.pop())  # Output: Random element (e.g., 1)
print(s)  # Output: Remaining set
```

#### `clear()`
```python
s = {1, 2, 3}
s.clear()
print(s)  # Output: set()
```

---

## 2. Set Operations (Methods & Operators)

### Union
```python
s1 = {1, 2}
s2 = {3, 4}
print(s1 | s2)  # Output: {1, 2, 3, 4}
print(s1.union(s2))  # Output: {1, 2, 3, 4}
```

### Intersection
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # Output: {2, 3}
print(s1.intersection(s2))  # Output: {2, 3}
```

### Difference
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 - s2)  # Output: {1}
print(s1.difference(s2))  # Output: {1}
```

### Symmetric Difference
```python
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 ^ s2)  # Output: {1, 4}
print(s1.symmetric_difference(s2))  # Output: {1, 4}
```

---

## 3. Checking Set Properties (Methods & Operators)

### Subset
```python
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1 <= s2)  # Output: True
print(s1.issubset(s2))  # Output: True
```

### Proper Subset
```python
s1 = {1, 2}
s2 = {1, 2, 3}
print(s1 < s2)  # Output: True
```

### Superset
```python
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1 >= s2)  # Output: True
print(s1.issuperset(s2))  # Output: True
```

### Proper Superset
```python
s1 = {1, 2, 3}
s2 = {1, 2}
print(s1 > s2)  # Output: True
```

### Disjoint Sets
```python
s1 = {1, 2}
s2 = {3, 4}
print(s1.isdisjoint(s2))  # Output: True
```

---

## Summary
- **Adding & Removing Elements**: `add()`, `remove()`, `discard()`, `pop()`, `clear()`
- **Operations (Methods & Operators)**: `union()` (`|`), `intersection()` (`&`), `difference()` (`-`), `symmetric_difference()` (`^`)
- **Checking Properties (Methods & Operators)**: `issubset()` (`<=`), Proper Subset (`<`), `issuperset()` (`>=`), Proper Superset (`>`), `isdisjoint()`

