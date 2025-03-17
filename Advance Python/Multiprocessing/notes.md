# Multiprocessing in Python

## Introduction
Multiprocessing in Python allows you to run multiple processes in parallel, leveraging multiple CPU cores for better performance. The `multiprocessing` module provides an interface similar to threading but uses separate memory space for each process.


## Key Concepts

### 1. Process
A process is an instance of a program that runs independently.

```python
from multiprocessing import Process

def worker():
    print("Worker process")

if __name__ == "__main__":
    p = Process(target=worker)
    p.start()
    p.join()
```

### 2. Pool
The `Pool` class provides a convenient way to parallelize execution.

```python
from multiprocessing import Pool

def square(n):
    return n * n

if __name__ == "__main__":
    with Pool(4) as pool:
        result = pool.map(square, [1, 2, 3, 4])
    print(result)  # [1, 4, 9, 16]
```

### 3. Queue
Used for inter-process communication.

```python
from multiprocessing import Process, Queue

def producer(q):
    q.put("Hello from Process")

def consumer(q):
    print(q.get())

if __name__ == "__main__":
    q = Queue()
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
```

### 4. Lock
Prevents race conditions when multiple processes access shared resources.

```python
from multiprocessing import Process, Lock

def worker(lock):
    with lock:
        print("Locked execution")

if __name__ == "__main__":
    lock = Lock()
    processes = [Process(target=worker, args=(lock,)) for _ in range(3)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
```

### 5. Shared Memory (Value & Array)
Used to share state between processes.

```python
from multiprocessing import Process, Value

def increment(shared_value):
    shared_value.value += 1

if __name__ == "__main__":
    val = Value('i', 0)
    processes = [Process(target=increment, args=(val,)) for _ in range(5)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(val.value)  # Expected output: 5
```

## Summary
- `Process`: Creates separate memory processes.
- `Pool`: Manages multiple worker processes.
- `Queue`: Facilitates inter-process communication.
- `Lock`: Ensures exclusive access to shared resources.
- `Value/Array`: Allows shared memory between processes.

Multiprocessing is useful for CPU-bound tasks, while multithreading is better for I/O-bound tasks.