# Difference Between Threading and Multiprocessing in Python

## 1. Overview
Python provides two key modules for running tasks concurrently:
- `threading` for **concurrent execution** using multiple threads.
- `multiprocessing` for **parallel execution** using multiple processes.

Both are used to run multiple tasks simultaneously, but they work differently and have different use cases.

---

## 2. Explanation of Each Code Example

### **Threading Code**
```python
import threading

def print_cube(num):
    print("Cube: {}".format(num * num * num))

def print_square(num):
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Done!")
```
### **How This Code Works**
- It creates **two threads** (`t1` and `t2`).
- Both threads **share the same memory** and execute concurrently.
- The `start()` method begins thread execution.
- The `join()` method ensures the main program waits for both threads to finish before proceeding.

### **Multiprocessing Code**
```python
import multiprocessing

def print_cube(num):
    print("Cube: {}".format(num * num * num))

def print_square(num):
    print("Square: {}".format(num * num))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_square, args=(10,))
    p2 = multiprocessing.Process(target=print_cube, args=(10,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("Done!")
```
### **How This Code Works**
- It creates **two processes** (`p1` and `p2`).
- Each process runs **independently in its own memory space**.
- `start()` initiates each process.
- `join()` ensures the main program waits for both processes to complete before moving on.

---

## 3. Key Differences Between Threading and Multiprocessing

| Feature            | **Threading** | **Multiprocessing** |
|--------------------|--------------|---------------------|
| **Module Used**   | `threading`   | `multiprocessing`   |
| **Execution Mode** | Uses multiple threads within a single process | Uses multiple processes (each with its own memory) |
| **Concurrency vs. Parallelism** | **Concurrency** (tasks switch execution but share memory) | **Parallelism** (tasks run truly in parallel) |
| **Memory Usage**   | Threads share the same memory space | Each process has its own memory (higher usage) |
| **Best for**       | I/O-bound tasks (network calls, file I/O) | CPU-bound tasks (heavy computations) |
| **GIL Effect**     | Affected by Python's **Global Interpreter Lock (GIL)** (not truly parallel) | Bypasses GIL for true parallel execution |
| **Overhead**       | Lower overhead (lightweight) | Higher overhead (process creation is costly) |

---

## 4. When to Use Which?

### **Use `threading` if:**
✅ Your program is **I/O-bound** (waiting for external resources like network requests, disk operations, etc.)
- Example: Downloading multiple files from the internet.
- Example: Handling multiple requests in a web server.

### **Use `multiprocessing` if:**
✅ Your program is **CPU-bound** (heavy computations like data processing, AI/ML, etc.)
- Example: Image processing, video rendering, stock price prediction.
- Example: Running multiple calculations in parallel on multiple CPU cores.

---

## 5. Key Takeaways

- `threading` allows **concurrent** execution but is limited by Python’s **Global Interpreter Lock (GIL)**.
- `multiprocessing` achieves **true parallel execution** by running code on separate CPU cores.
- Use **threading for I/O-bound** operations and **multiprocessing for CPU-bound** operations.
- Threads **share memory**, while processes **have independent memory spaces**.

---

## 6. Example Scenarios

### **Web Scraping (Threading is better)**
```python
import threading
import requests

def fetch_data(url):
    response = requests.get(url)
    print(f"Data from {url}: {len(response.text)} bytes")

urls = ["https://example.com", "https://example.org"]
threads = [threading.Thread(target=fetch_data, args=(url,)) for url in urls]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
```
### **Image Processing (Multiprocessing is better)**
```python
import multiprocessing
from PIL import Image

def process_image(image_path):
    img = Image.open(image_path)
    img = img.convert("L")  # Convert to grayscale
    img.save("processed_" + image_path)
    print(f"Processed {image_path}")

image_files = ["image1.jpg", "image2.jpg"]
processes = [multiprocessing.Process(target=process_image, args=(img,)) for img in image_files]

for process in processes:
    process.start()

for process in processes:
    process.join()
```

---

## 7. Conclusion
If your task involves **I/O operations** (like downloading files, handling multiple client requests, or web scraping), use `threading`. If your task is **CPU-intensive** (like large calculations, AI/ML processing, or image rendering), use `multiprocessing`. 🚀

