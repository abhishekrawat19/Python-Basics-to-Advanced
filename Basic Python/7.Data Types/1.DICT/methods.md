# Dictionary Methods in Python (With Code & Output)

## 1. Adding & Removing Elements

| Method | Purpose | Returns |
|--------|---------|---------|
| `dict[key] = value` | Adds or updates a key-value pair | ✅ Modifies in-place |
| `pop(key)` | Removes a key and returns its value, raises error if not found | ✅ Value |
| `popitem()` | Removes & returns the last inserted key-value pair | ✅ (key, value) tuple |
| `del dict[key]` | Removes a key, raises error if not found | ✅ Modifies in-place |
| `clear()` | Removes all elements from the dictionary | ✅ Modifies in-place |

### Explanation & Examples
#### `dict[key] = value` (Adding/Updating)
- This method adds a new key-value pair to the dictionary or updates an existing key.
```python
d = {'a': 1, 'b': 2}
d['c'] = 3
print(d)  # Output: {'a': 1, 'b': 2, 'c': 3}
```

#### `pop(key)`
- Removes a key from the dictionary and returns its value. Raises `KeyError` if the key is not found.
```python
d = {'a': 1, 'b': 2}
print(d.pop('a'))  # Output: 1
print(d)  # Output: {'b': 2}

# d.pop('c')  # Error: KeyError
```

#### `popitem()`
- Removes and returns the last inserted key-value pair as a tuple.
```python
d = {'a': 1, 'b': 2}
print(d.popitem())  # Output: ('b', 2) (last inserted item)
print(d)  # Output: {'a': 1}
```

#### `del dict[key]`
- Deletes a specific key from the dictionary. Raises `KeyError` if the key does not exist.
```python
d = {'a': 1, 'b': 2}
del d['a']
print(d)  # Output: {'b': 2}

# del d['c']  # Error: KeyError
```

#### `clear()`
- Removes all key-value pairs from the dictionary.
```python
d = {'a': 1, 'b': 2}
d.clear()
print(d)  # Output: {}
```

---

## 2. Dictionary Operations

### Merging Dictionaries
- Combines two dictionaries into one. Python 3.9+ supports the `|` operator for merging.
```python
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
print({**d1, **d2})  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(d1 | d2)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4} (Python 3.9+)
```

### Getting Keys, Values, and Items
- `keys()`, `values()`, and `items()` return dictionary views.
```python
d = {'a': 1, 'b': 2}
print(d.keys())  # Output: dict_keys(['a', 'b'])
print(d.values())  # Output: dict_values([1, 2])
print(d.items())  # Output: dict_items([('a', 1), ('b', 2)])
```

---

## 3. Checking & Setting Default Values

### Checking Existence of a Key
- The `in` keyword checks if a key exists in the dictionary.
```python
d = {'a': 1, 'b': 2}
print('a' in d)  # Output: True
print('c' in d)  # Output: False
```

### Using `get()`
- `get()` retrieves a value for a key, returning `None` (or a default value) if the key does not exist.
```python
d = {'a': 1, 'b': 2}
print(d.get('a'))  # Output: 1
print(d.get('c', 'Not Found'))  # Output: Not Found
```

### Using `setdefault()`
- `setdefault()` retrieves the value of a key if it exists; otherwise, it sets a default value.
```python
d = {'a': 1}
d.setdefault('b', 2)
print(d)  # Output: {'a': 1, 'b': 2}
d.setdefault('a', 100)  # Won't overwrite existing key
print(d)  # Output: {'a': 1, 'b': 2}
```

---

## Summary
- **Adding & Removing Elements**: `dict[key] = value`, `pop()`, `popitem()`, `del`, `clear()`
- **Operations**: Merging (`|`, `**` unpacking), `keys()`, `values()`, `items()`
- **Checking & Setting Defaults**: `in`, `get()`, `setdefault()`

