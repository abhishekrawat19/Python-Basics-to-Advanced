# Function Caching in Python

## What is Function Caching?
Function caching is a technique used to store the results of expensive function calls and reuse them when the same inputs occur again. This improves performance by avoiding redundant calculations and unnecessary recomputation.

---

## Why Use Function Caching?
Function caching provides several benefits, including:
- **Reduces Computation Time**: Saves previously computed results, preventing redundant calculations.
- **Optimizes Performance**: Particularly useful for recursive functions and computationally expensive operations.
- **Efficient Memory Use**: Stores only required results, improving resource efficiency.
- **Enhances API Performance**: Reduces the number of calls to external APIs by caching responses.
- **Speeds Up Machine Learning Pipelines**: Helps cache precomputed results to speed up ML model training and inference.
- **Avoids Repetitive Database Queries**: Caching database queries can significantly reduce load on the database server.

---

## Methods for Function Caching in Python

### 1. Using `functools.lru_cache`
Python’s `lru_cache` (Least Recently Used Cache) is a built-in decorator that caches function results in memory.

#### How It Works:
- **Stores recent function calls** in a fixed-size cache.
- **Automatically removes least recently used entries** when the cache reaches maximum capacity.
- **Prevents redundant calculations**, making repeated calls significantly faster.

#### Example with Explanation:
```python
from functools import lru_cache  # Importing lru_cache from functools
import time  # Importing time module to simulate delay

@lru_cache(maxsize=3)  # Caches the last 3 function calls
def slow_function(n):
    """Simulates a slow function by adding a delay."""
    time.sleep(2)  # Simulating a time-consuming operation
    return n * n  # Returns the square of n

print(slow_function(4))  # First call, takes 2 seconds
print(slow_function(4))  # Second call, returns instantly from cache
```
✅ Stores results of function calls and retrieves them instantly when the same input is used again.

#### Parameters:
- `maxsize`: Defines how many function calls to cache (None for unlimited caching).
- `typed`: If `True`, stores results separately for different types of the same function argument.

---

### 2. Using `cachetools` for Time-Based Expiry
Unlike `lru_cache`, `cachetools` allows cache expiration after a set time limit.

#### How It Works:
- **Caches function results** but removes entries after a defined time (TTL - Time to Live).
- **Useful for caching API responses** where stale data should be discarded after some time.

#### Installation:
To install the `cachetools` library, run:
```sh
pip install cachetools
```

#### Example with Explanation:
```python
from cachetools import TTLCache  # Importing TTLCache from cachetools
import time  # Importing time module

# Creating a cache that can hold 5 values and expires after 10 seconds
cache = TTLCache(maxsize=5, ttl=10)

def cached_function(n):
    """Checks if the value exists in cache; if not, computes and stores it."""
    if n in cache:
        return cache[n]  # Return from cache if available
    result = n * n  # Compute the result
    cache[n] = result  # Store result in cache
    return result

print(cached_function(4))  # Computed and stored
print(cached_function(4))  # Retrieved from cache

time.sleep(11)  # Wait for cache to expire
print(cached_function(4))  # Recomputes since cache expired
```
✅ Useful when caching needs automatic expiration.

---

### 3. Using `diskcache` for Persistent Caching
`diskcache` stores cache on disk, making it persistent across multiple script executions.

#### How It Works:
- **Stores function results on disk**, so cached results persist even after the program stops.
- **Ideal for caching database queries, ML predictions, or API calls**.

#### Installation:
To install `diskcache`, run:
```sh
pip install diskcache
```

#### Example with Explanation:
```python
import diskcache as dc  # Importing diskcache

# Creating a disk-based cache storage
cache = dc.Cache("my_cache")

def expensive_function(n):
    """Checks cache before computing; stores result for future use."""
    if n in cache:
        return cache[n]  # Return cached value
    result = n * n  # Compute result
    cache[n] = result  # Store result in cache
    return result

print(expensive_function(5))  # Computed and stored on disk
print(expensive_function(5))  # Retrieved from disk cache
```
✅ Ideal for caching across multiple executions of a script.

---

## Advanced Topics in Function Caching

### 4. Using Custom Cache Mechanisms
For more control, use a **custom dictionary-based cache**:
```python
cache = {}  # Creating an empty dictionary for caching

def cached_function(n):
    """Caches function output manually using a dictionary."""
    if n in cache:
        return cache[n]  # Return cached value
    result = n * n  # Compute result
    cache[n] = result  # Store result
    return result
```
✅ Gives full control over cache logic but requires manual cache management.

---

### 5. Memoization in Recursive Functions
Memoization optimizes recursive functions by caching previously computed results.

#### Example: Fibonacci Sequence with Memoization
```python
from functools import lru_cache  # Importing lru_cache

@lru_cache(maxsize=None)  # No limit on cache size

def fibonacci(n):
    """Computes Fibonacci numbers efficiently using caching."""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))  # Runs much faster than without caching
```
✅ Saves redundant recursive calls, making large recursive computations feasible.

---

### 6. Hybrid Caching Strategies
For large applications, combine multiple caching techniques:
- **Use `lru_cache` for small, frequently used calculations.**
- **Use `diskcache` for caching expensive database queries.**
- **Use `cachetools.TTLCache` for caching API responses that expire.**

---

## Real-Time Use Cases of Function Caching

| Use Case | Suitable Caching Method |
|----------|-------------------------|
| Repeating calculations | `functools.lru_cache` |
| Web API response caching | `cachetools.TTLCache` |
| Machine learning model predictions | `diskcache` |
| Processing large datasets | `functools.lru_cache` or `diskcache` |
| Recursive algorithms | `functools.lru_cache` |
| Avoiding redundant DB queries | `diskcache` or `cachetools.TTLCache` |

Function caching is an essential optimization technique, especially for computationally expensive tasks, API integrations, and data-intensive applications. 🚀

