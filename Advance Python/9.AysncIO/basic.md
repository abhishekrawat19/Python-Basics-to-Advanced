# Asyncio in Python - Detailed Explanation

## 1. Basic Syntax & Working

### What is Asyncio?
`asyncio` is a Python library that provides asynchronous programming capabilities. It enables running non-blocking code, which is useful for I/O-bound tasks such as network requests, file operations, and database queries.

### Basic Syntax
```python
import asyncio

async def my_function():
    print("Start Function")
    await asyncio.sleep(2)  # Simulating an I/O-bound operation
    print("End Function")

asyncio.run(my_function())
```

### Working
1. `async def` defines an asynchronous function (coroutine).
2. `await` suspends the coroutine execution until the awaited operation completes.
3. `asyncio.run(my_function())` starts the event loop and executes the coroutine.

#### Dry Run (Step-by-Step Execution)
```
Step 1: my_function() is called and starts execution.
Step 2: "Start Function" is printed.
Step 3: The function encounters `await asyncio.sleep(2)`, suspends execution for 2 seconds.
Step 4: After 2 seconds, "End Function" is printed.
```

---

## 2. Single & Multiple Function Execution (With Dry Run Explanation)

### Running a Single Async Function
```python
import asyncio

async def single_task():
    print("Task started")
    await asyncio.sleep(3)
    print("Task completed")

asyncio.run(single_task())
```
#### Dry Run
```
Step 1: "Task started" is printed.
Step 2: The function pauses at `await asyncio.sleep(3)`, suspending execution for 3 seconds.
Step 3: After 3 seconds, "Task completed" is printed.
```

### Running Multiple Async Functions Concurrently
```python
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())
```

#### Dry Run
```
Step 1: "Task 1 started" and "Task 2 started" are printed.
Step 2: Task 2 sleeps for 1 second, Task 1 sleeps for 2 seconds.
Step 3: After 1 second, "Task 2 completed" is printed.
Step 4: After 2 seconds, "Task 1 completed" is printed.
```

---

## 3. `asyncio.gather()` - Syntax, Use, and Working

### Syntax
```python
await asyncio.gather(task1(), task2(), task3())
```

### Explanation:
- `asyncio.gather()` runs multiple asynchronous tasks **concurrently**.
- The function calls inside `gather()` start at the same time.
- The execution completes when all the gathered tasks are finished.

### Example Using `asyncio.gather()`
```python
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(3)
    print("Data fetched")
    return "Sample Data"

async def process_data():
    print("Processing data...")
    await asyncio.sleep(2)
    print("Data processed")

async def main():
    result = await asyncio.gather(fetch_data(), process_data())
    print("All tasks completed.", result)

asyncio.run(main())
```

#### Dry Run
```
Step 1: "Fetching data..." and "Processing data..." are printed.
Step 2: `fetch_data` sleeps for 3 seconds, `process_data` sleeps for 2 seconds.
Step 3: After 2 seconds, "Data processed" is printed.
Step 4: After 3 seconds, "Data fetched" is printed.
Step 5: "All tasks completed." is printed with the result.
```

### Why Use `asyncio.gather()`?
- Efficiently runs multiple async functions concurrently.
- Improves performance when handling multiple I/O-bound tasks.
- Returns results in the same order as the function calls inside `gather()`.

By mastering `asyncio` and `asyncio.gather()`, you can optimize performance in applications that require concurrent execution of tasks!

