# Understanding `async` and `await` in Python's `asyncio`

## **Introduction**
Python's `asyncio` module allows for asynchronous programming, enabling the execution of multiple tasks concurrently. Two fundamental concepts in `asyncio` are `async` and `await`, which enable efficient execution of I/O-bound operations without blocking the main thread.

---

## **What Does `async` Do?**
- `async` is used to define an asynchronous function (also called a coroutine).
- Functions defined with `async def` return a coroutine object instead of executing immediately.
- These coroutines must be awaited to execute properly.

### **Example of an Async Function:**
```python
import asyncio

async def async_function():
    print("Start task")
    await asyncio.sleep(2)
    print("Task completed")
    return "Done"
```
**Explanation:**
- `async def async_function()` defines an async function.
- `asyncio.sleep(2)` pauses execution for 2 seconds **without blocking** other tasks.
- The function returns a coroutine object when called.

---

## **What Does `await` Do?**
- `await` is used inside `async` functions to pause execution until the awaited task completes.
- It allows **other tasks** to run while waiting.
- It must be used with another coroutine or an awaitable object.

### **Example with `await`**
```python
import asyncio

async def async_function():
    print("Start task")
    await asyncio.sleep(2)  # Pauses here without blocking
    print("Task completed")
```
**How It Works:**
1. `await asyncio.sleep(2)` makes the function pause at this point.
2. The event loop allows other tasks to execute during the wait.
3. After 2 seconds, the function resumes and prints "Task completed".

---

## **Why Do We Write `await` in Two Places?**
When calling an async function inside another, we typically need `await` in two places:
1. **Inside the async function** (to pause execution while awaiting an operation).
2. **When calling the async function** (to execute it properly).

### **Example: Awaiting Twice**
```python
import asyncio

async def async_function():
    print("Start task")
    await asyncio.sleep(2)  # First 'await' - pauses here
    print("Task completed")
    return "Done"

async def main():
    print("Calling async function...")
    result = await async_function()  # Second 'await' - waits for function to finish
    print("Result:", result)

asyncio.run(main())
```
**Breakdown:**
- `await asyncio.sleep(2)`: Pauses `async_function` execution.
- `await async_function()`: Ensures the function runs properly in `main`.

---

## **What Happens if You Don't Use `await`?**

### **1. Missing `await` inside an async function**
```python
import asyncio

async def async_function():
    print("Start task")
    asyncio.sleep(2)  # ❌ Missing 'await'
    print("Task completed")
```
**Error:**
```
TypeError: 'coroutine' object is not awaitable
```
✔ **Fix:** Use `await asyncio.sleep(2)`

---

### **2. Forgetting to `await` an Async Function**
```python
import asyncio

async def async_function():
    print("Start task")
    await asyncio.sleep(2)
    print("Task completed")

async def main():
    result = async_function()  # ❌ Missing 'await'
    print("Result:", result)

asyncio.run(main())
```
**Output:**
```
Start task
Result: <coroutine object async_function at 0x...>
```
**Issue:** `result` is a coroutine object, **not the function's return value**.  
✔ **Fix:** Use `await async_function()`

---

## **Key Takeaways**
- `async def` defines a coroutine function.
- `await` **pauses execution** until the awaited operation completes.
- If `await` is missing:
  - Inside a function: The operation won't execute properly.
  - When calling a function: The function won’t run, returning a **coroutine object** instead.

---

## **Best Practices**
✔ Always `await` async functions.  
✔ Never call async functions directly inside `asyncio.run()`.  
✔ If unsure, print the function return type to check for coroutine objects.  

This should provide a **detailed** understanding of `async` and `await`, why they are needed, and how they work in practice.

