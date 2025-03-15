# File Handling in Python

File handling allows Python programs to read, write, and manipulate files stored on the system. Python provides built-in functions for working with files efficiently.

## 1. Opening a File
Python uses the `open()` function to open a file. It returns a file object that can be used for further operations.

```python
file = open("example.txt", "r")  # Open file in read mode
```

Modes available:
| Mode | Description |
|------|-------------|
| `r`  | Read mode (default) |
| `w`  | Write mode (overwrites existing content) |
| `a`  | Append mode (adds content to the end) |
| `x`  | Create mode (creates a new file) |
| `b`  | Binary mode (e.g., `rb` for reading binary files) |

---

## 2. Reading a File
Use `read()`, `readline()`, or `readlines()` to fetch content.

```python
file = open("example.txt", "r")
content = file.read()  # Reads entire file
print(content)
file.close()
```

Other reading methods:
```python
line = file.readline()  # Reads one line
lines = file.readlines()  # Reads all lines as a list
```
✅ Always **close the file** after reading to free system resources.

---

## 3. Writing to a File
Use `write()` or `writelines()`.

```python
file = open("example.txt", "w")  # Overwrites content
file.write("Hello, world!\n")
file.close()
```
Appending to a file:
```python
file = open("example.txt", "a")
file.write("New line added!\n")
file.close()
```

---

## 4. Using `with` Statement
The `with` statement **automatically closes** the file after execution.

```python
with open("example.txt", "r") as file:
    content = file.read()
    print(content)  # No need to close the file manually
```
✅ Recommended way to handle files to avoid memory leaks.

---

## 5. Working with Binary Files
Binary files store non-text data (e.g., images, PDFs).

```python
with open("image.jpg", "rb") as file:
    binary_data = file.read()
```
Writing binary data:
```python
with open("copy.jpg", "wb") as file:
    file.write(binary_data)
```

---

## 6. Handling File Exceptions
Avoid errors using `try-except`.

```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
```
✅ Prevents crashes when a file is missing.

---

## 7. Checking if a File Exists
Use `os` or `pathlib` module.

```python
import os
if os.path.exists("example.txt"):
    print("File exists!")
```
Using `pathlib`:
```python
from pathlib import Path
if Path("example.txt").is_file():
    print("File exists!")
```

---

## 8. Deleting a File
Use `os.remove()`.

```python
import os
os.remove("example.txt")
```
✅ Always check if the file exists before deleting.

---

## Summary Table
| Operation | Method |
|-----------|--------|
| Open a file | `open("file.txt", "mode")` |
| Read a file | `read()`, `readline()`, `readlines()` |
| Write to a file | `write()`, `writelines()` |
| Append to a file | `open("file.txt", "a")` |
| Use `with` statement | `with open("file.txt", "r") as file:` |
| Handle file errors | `try-except FileNotFoundError` |
| Check if a file exists | `os.path.exists()`, `pathlib.Path.is_file()` |
| Delete a file | `os.remove("file.txt")` |

Python file handling allows efficient and safe manipulation of files for various applications.

