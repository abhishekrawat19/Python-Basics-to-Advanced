# Asyncio in Python

## What is Asyncio?
`asyncio` is a Python library used for writing concurrent code using the `async` and `await` syntax. It enables asynchronous programming, making it useful for I/O-bound and high-level structured network code.

---

## Why Use Asyncio?
- **Non-blocking Execution**: Runs multiple tasks concurrently without waiting.
- **Efficient I/O Handling**: Ideal for tasks like web scraping, API calls, and database queries.
- **Better Performance**: Reduces time wasted in waiting for I/O operations.
- **Scalability**: Handles thousands of tasks efficiently compared to traditional multi-threading.

---

## How Asyncio Works
Asyncio works by utilizing an **event loop** that manages and schedules asynchronous tasks. Instead of waiting for an operation (like a network request) to finish before proceeding, `asyncio` allows other tasks to continue running while waiting.

### Key Concepts:
1. **Coroutines**: Special functions defined with `async def`. These functions return a coroutine object that needs to be awaited.
2. **Event Loop**: A loop that continuously runs tasks and schedules coroutines.
3. **Tasks**: A wrapper around a coroutine that allows it to run concurrently.
4. **Futures**: Represent a value that will be available at some point in the future.

---

## Basic Asyncio Syntax & Examples

### 1. Defining an Asynchronous Function
```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

asyncio.run(say_hello())
```
#### Output:
```
Hello
(Waits for 1 second)
World
```
#### Explanation:
- `async def` defines an asynchronous function.
- `await asyncio.sleep(1)` pauses execution for 1 second without blocking other tasks.
- `asyncio.run(say_hello())` runs the coroutine in an event loop.

### 2. Running Multiple Async Tasks
```python
import asyncio

async def task1():
    await asyncio.sleep(2)
    print("Task 1 complete")

async def task2():
    await asyncio.sleep(1)
    print("Task 2 complete")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```
#### Output:
```
Task 2 complete
Task 1 complete
```
#### Explanation:
- `asyncio.gather(task1(), task2())` runs both coroutines concurrently.
- `task2` completes first since it sleeps for a shorter duration.

### 3. Using Asyncio with HTTP Requests
```python
import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = "https://example.com"
    content = await fetch_url(url)
    print(content[:100])  # Print first 100 characters

asyncio.run(main())
```
#### Why Use This?
- Faster network requests compared to synchronous approaches.
- Efficiently handles multiple API calls.

---

## Advanced Concepts in Asyncio

### 1. Creating Tasks to Run in the Background
```python
import asyncio

async def background_task():
    await asyncio.sleep(3)
    print("Background Task Complete")

async def main():
    task = asyncio.create_task(background_task())
    print("Main Task Running")
    await asyncio.sleep(1)
    print("Main Task Complete")
    await task  # Ensure background task completes

asyncio.run(main())
```
#### Output:
```
Main Task Running
Main Task Complete
Background Task Complete
```
#### Explanation:
- `asyncio.create_task()` schedules a coroutine to run in the background.
- `await task` ensures the background task completes before the program exits.

### 2. Handling Exceptions in Asyncio
```python
import asyncio

async def faulty_task():
    await asyncio.sleep(2)
    raise ValueError("Something went wrong!")

async def main():
    try:
        await faulty_task()
    except ValueError as e:
        print(f"Caught an error: {e}")

asyncio.run(main())
```
#### Output:
```
Caught an error: Something went wrong!
```

### 3. Asyncio Queue (Producer-Consumer Pattern)
```python
import asyncio

async def producer(queue):
    for i in range(5):
        await asyncio.sleep(1)
        await queue.put(i)
        print(f"Produced: {i}")

async def consumer(queue):
    while True:
        item = await queue.get()
        print(f"Consumed: {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    producers = asyncio.create_task(producer(queue))
    consumers = asyncio.create_task(consumer(queue))
    await producers
    await queue.join()
    consumers.cancel()

asyncio.run(main())
```
#### Why Use Asyncio Queue?
- Used in real-world applications like data pipelines, message queues.
- Ensures smooth producer-consumer flow.

### 4. Running Blocking Code in Asyncio (Threading)
```python
import asyncio
import time

async def async_task():
    print("Starting async task")
    await asyncio.sleep(2)
    print("Async task complete")

def blocking_task():
    print("Starting blocking task")
    time.sleep(3)
    print("Blocking task complete")

async def main():
    loop = asyncio.get_running_loop()
    blocking = loop.run_in_executor(None, blocking_task)
    await asyncio.gather(async_task(), blocking)

asyncio.run(main())
```
#### Explanation:
- `loop.run_in_executor(None, blocking_task)` runs blocking code in a separate thread.
- Avoids freezing the event loop.

---

## When to Use Asyncio?
- When performing **I/O-bound** tasks (e.g., API calls, file reading, web scraping).
- When working with **network programming** (e.g., WebSockets, TCP clients/servers).
- When dealing with **high concurrency requirements**.

## When **NOT** to Use Asyncio?
- When performing **CPU-bound** tasks (use multiprocessing instead).
- When dealing with **simple scripts** where concurrency isn't required.

---

## Real-World Applications of Asyncio
- **Web Scraping**: Fetch multiple web pages concurrently.
- **Database Queries**: Execute multiple queries asynchronously.
- **Chat Applications**: Handle real-time messaging.
- **API Integrations**: Call multiple APIs concurrently.
- **Financial Data Processing**: Stream real-time stock data.
- **IoT Applications**: Collect and process data from multiple sensors asynchronously.

Asyncio is a powerful tool for handling asynchronous tasks efficiently. Mastering it can significantly improve performance in applications dealing with high concurrency.

