# Advanced File Handling in Python

Python provides various advanced techniques for efficient and secure file handling. This guide covers essential advanced topics along with detailed explanations and code examples.

---

## 1. Working with File Buffers
### What is File Buffering?
File buffering is the temporary storage of data before writing it to a file or reading from it. Python automatically applies buffering for efficiency.

### How to Use File Buffering?
The `buffering` parameter in `open()` allows control over buffering:

```python
# Open file with a custom buffer size (2048 bytes)
with open("example.txt", "w", buffering=2048) as file:
    file.write("Buffered data writing!")
```
✅ Reduces direct disk operations, improving performance.

---

## 2. Memory-Mapped Files (`mmap`)
### What is `mmap`?
The `mmap` module allows direct file manipulation in memory, making it efficient for handling large files.

### How to Use `mmap`?
```python
import mmap

with open("example.txt", "r+") as file:
    mmapped_file = mmap.mmap(file.fileno(), 0)  # Memory-map the file
    print(mmapped_file.readline())  # Read efficiently
    mmapped_file.close()
```
✅ Best for modifying large files without loading them entirely into memory.

---

## 3. File Locking (Preventing Simultaneous Access)
### Why Use File Locking?
When multiple processes access the same file, data corruption can occur. File locking ensures safe access.

### How to Implement File Locking?
On Linux/macOS, use `fcntl`, while on Windows, use `msvcrt`.

#### Linux/macOS:
```python
import fcntl

with open("example.txt", "w") as file:
    fcntl.flock(file, fcntl.LOCK_EX)  # Lock file
    file.write("Locked write operation!")
    fcntl.flock(file, fcntl.LOCK_UN)  # Unlock file
```

#### Windows:
```python
import msvcrt

def lock_file(file):
    msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)

def unlock_file(file):
    msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)

with open("example.txt", "w") as file:
    lock_file(file)
    file.write("Locked operation!")
    unlock_file(file)
```
✅ Ensures safe multi-threaded/multi-process file access.

---

## 4. Using `tempfile` for Temporary Files
### Why Use Temporary Files?
Temporary files are used for short-term storage and are automatically deleted when closed.

### How to Create Temporary Files?
```python
import tempfile

with tempfile.NamedTemporaryFile(delete=False) as temp:
    temp.write(b"Temporary data")
    print("Temporary file created at:", temp.name)
```
✅ Prevents cluttering the filesystem with unused files.

---

## 5. Reading and Writing Compressed Files (`gzip`, `bz2`)
### Why Use Compressed Files?
Compressed files save storage space and speed up data transfer.

### How to Handle Gzip Files?
```python
import gzip

with gzip.open("example.txt.gz", "wt") as file:
    file.write("Compressed text")

with gzip.open("example.txt.gz", "rt") as file:
    print(file.read())
```
✅ Useful for handling large datasets efficiently.

---

## 6. Working with CSV and JSON Files
### Why CSV and JSON?
- CSV is simple for tabular data.
- JSON is widely used for APIs and structured data.

### Handling CSV Files:
```python
import csv

# Writing to a CSV file
with open("data.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
```

### Handling JSON Files:
```python
import json

data = {"name": "Alice", "age": 25}
with open("data.json", "w") as file:
    json.dump(data, file)
```
✅ Common formats for data storage and exchange.

---

## 7. Asynchronous File Handling (`aiofiles`)
### Why Use Async File Handling?
Standard file operations are blocking. `aiofiles` enables non-blocking file I/O for better performance.

### How to Use `aiofiles`?
```python
import aiofiles
import asyncio

async def read_file():
    async with aiofiles.open("example.txt", "r") as file:
        content = await file.read()
        print(content)

asyncio.run(read_file())
```
✅ Ideal for handling large-scale I/O operations asynchronously.

---

## 8. Handling Large Files Efficiently
### Why Process Large Files in Chunks?
Loading large files into memory can cause performance issues. Processing in chunks avoids memory overload.

### How to Read Large Files in Chunks?
```python
with open("large_file.txt", "r") as file:
    while chunk := file.read(1024):  # Read in 1KB chunks
        process(chunk)
```
✅ Avoids memory overflow when handling large files.

---

## 9. Monitoring File Changes (`watchdog`)
### Why Monitor Files?
File monitoring is useful in log tracking, real-time data processing, etc.

### How to Monitor File Changes?
```python
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"File {event.src_path} has been modified")

observer = Observer()
observer.schedule(Watcher(), path=".", recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
```
✅ Useful for tracking changes in log files or configuration files.

---

## Summary Table
| Feature | Method |
|---------|--------|
| Buffered File Handling | `open(buffering=N)` |
| Memory-Mapped Files | `mmap.mmap(fileno(), 0)` |
| File Locking | `fcntl.flock()` / `msvcrt.locking()` |
| Temporary Files | `tempfile.NamedTemporaryFile()` |
| Compressed Files | `gzip.open()` |
| CSV Handling | `csv.reader()` / `csv.writer()` |
| JSON Handling | `json.load()` / `json.dump()` |
| Async File Handling | `aiofiles.open()` |
| Large File Processing | `file.read(chunk_size)` |
| File Monitoring | `watchdog.Observer()` |

Python’s advanced file handling techniques enhance efficiency, security, and performance in modern applications.

