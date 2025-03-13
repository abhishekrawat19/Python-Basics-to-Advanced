# Exception Handling in Python

Python provides a robust way to handle runtime errors using exception handling. This prevents the program from crashing and allows for proper error management.

## 1. Basic Exception Handling
Use `try` and `except` to catch errors.

```python
try:
    num = int("hello")  # Causes ValueError
except ValueError:
    print("Invalid input! Please enter a number.")
```
**Output:**
```
Invalid input! Please enter a number.
```
✅ Prevents the program from crashing.

---

## 2. Handling Multiple Exceptions
You can catch multiple exceptions using one or multiple `except` blocks.

```python
try:
    a = [10, 20]
    print(a[5])  # IndexError
except (ValueError, IndexError) as e:
    print("Error:", e)
```
✅ Handles `ValueError` and `IndexError` in a single block.

---

## 3. Using `else` and `finally`
- `else` runs **only if no exception occurs**.
- `finally` **always runs**, even if an exception occurs.

```python
try:
    num = int("10")  # No error
except ValueError:
    print("Invalid input!")
else:
    print("Conversion successful:", num)
finally:
    print("Execution completed.")
```
**Output:**
```
Conversion successful: 10
Execution completed.
```
✅ Ensures cleanup code runs (`finally`).

---

## 4. Raising Exceptions (`raise`)
Manually trigger an exception using `raise`.

```python
age = -5
if age < 0:
    raise ValueError("Age cannot be negative!")
```
**Output:**
```
ValueError: Age cannot be negative!
```
✅ Useful for enforcing rules.

---

## 5. Types of Exceptions in Python
Python exceptions can be categorized into different types:

### **1. Built-in (Generic) Exceptions**
These are predefined exceptions in Python.

- **Type Errors**: `TypeError` (wrong type used)
- **Value Errors**: `ValueError` (invalid value for an operation)
- **Index Errors**: `IndexError` (accessing an out-of-range index)
- **Key Errors**: `KeyError` (accessing a missing key in a dictionary)
- **IO Errors**: `FileNotFoundError`, `PermissionError`

### **2. Custom (User-Defined) Exceptions**
You can define your own exceptions by subclassing `Exception`.

```python
class CustomError(Exception):
    pass

try:
    raise CustomError("Something went wrong!")
except CustomError as e:
    print("Caught custom exception:", e)
```
✅ Useful for application-specific error handling.

### **3. System (Critical) Exceptions**
These are low-level exceptions that can stop the Python interpreter.

- **MemoryError** – Not enough memory
- **RecursionError** – Too many recursive calls
- **KeyboardInterrupt** – User pressed `Ctrl+C`
- **SystemExit** – Program exit requested (`sys.exit()`)

---

## 6. Advanced Exception Handling Techniques

### **1. Exception Chaining (`__cause__` and `__context__`)**
Python allows chaining exceptions using `raise from` to maintain traceback clarity.

```python
try:
    try:
        int("invalid")  # Raises ValueError
    except ValueError as e:
        raise TypeError("Type conversion error") from e
except TypeError as e:
    print("Chained Exception:", e.__cause__)
```
✅ Helps track the root cause of errors.

---

### **2. Custom Logging in Exception Handling**
Instead of printing errors, use `logging` for better tracking.

```python
import logging
logging.basicConfig(filename="errors.log", level=logging.ERROR)

try:
    x = 1 / 0  # ZeroDivisionError
except ZeroDivisionError as e:
    logging.error("Exception occurred: %s", e)
```
✅ Saves errors in a log file instead of printing them.

---

### **3. Using `sys.exc_info()` for Exception Details**
`sys.exc_info()` provides detailed exception context, useful for debugging.

```python
import sys

try:
    1 / 0
except Exception:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("Exception Type:", exc_type)
    print("Exception Message:", exc_value)
```
✅ Retrieves detailed error information dynamically.

---

### **4. Ignoring Specific Exceptions Using `pass`**
If an exception is expected and doesn't need handling, use `pass`.

```python
try:
    int("abc")  # Causes ValueError
except ValueError:
    pass  # Silently ignore error
```
✅ Useful when handling non-critical exceptions.

---

## Summary Table

| Block | Purpose |
|-------|---------|
| `try` | Code that may raise an error |
| `except` | Handles the error |
| `else` & `finally` | `else` runs if no error occurs, `finally` always runs (cleanup) |
| `raise` | Manually trigger an exception |
| `raise from` | Chains exceptions for better debugging |
| `logging` | Stores errors in logs instead of printing |
| `sys.exc_info()` | Retrieves detailed exception information |
| `pass` | Silently ignores expected exceptions |

---

Exception handling ensures that errors are properly managed, keeping the program stable and user-friendly while offering advanced debugging techniques.

