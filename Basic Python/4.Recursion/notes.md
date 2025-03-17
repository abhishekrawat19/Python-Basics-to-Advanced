# Recursion in Python

## Introduction
Recursion is a programming technique where a function calls itself to solve smaller instances of the problem until it reaches a base condition. It is widely used in problems involving divide-and-conquer strategies, such as searching, sorting, and tree traversal.

## How Recursion Works
When a recursive function is called, a new frame is added to the call stack, storing the function's local variables and execution state. This continues until the base condition is met, at which point the functions start returning their results back up the call stack.

## Syntax of Recursion in Python
```python
# Example: Factorial using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Output: 120
```

## Understanding Recursion as a Runtime Stack Mechanism
Recursion operates on a **runtime stack** where each function call is pushed onto the stack until a base condition is met. Then, the stack unwinds as functions return their results.

### Step-by-step Execution of `factorial(5)`:
1. `factorial(5)` calls `factorial(4)`
2. `factorial(4)` calls `factorial(3)`
3. `factorial(3)` calls `factorial(2)`
4. `factorial(2)` calls `factorial(1)` (Base case reached)
5. `factorial(1)` returns `1`
6. `factorial(2)` returns `2 * 1 = 2`
7. `factorial(3)` returns `3 * 2 = 6`
8. `factorial(4)` returns `4 * 6 = 24`
9. `factorial(5)` returns `5 * 24 = 120`

Each call is stored in memory until it completes execution and returns.

## Types of Recursion
### 1. **Direct Recursion**
A function calls itself directly.
```python
def countdown(n):
    if n <= 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

### 2. **Indirect Recursion**
A function calls another function that, in turn, calls the original function.
```python
def funcA(n):
    if n <= 0:
        return
    print("FuncA", n)
    funcB(n - 1)

def funcB(n):
    if n <= 0:
        return
    print("FuncB", n)
    funcA(n - 2)

funcA(5)
```

### 3. **Tail Recursion**
A recursive function where the recursive call is the last operation.
```python
def tail_factorial(n, accumulator=1):
    if n == 0:
        return accumulator
    return tail_factorial(n - 1, n * accumulator)

print(tail_factorial(5))
```

### 4. **Tree Recursion**
A function calls itself multiple times.
```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(5))
```

## Advanced Concepts in Recursion
### 1. **Backtracking**
Backtracking is an optimization technique used to explore all possibilities and backtrack if a solution is not valid.
```python
def solve_maze(maze, x, y, path):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        print("Path:", path)
        return
    if x >= len(maze) or y >= len(maze[0]) or maze[x][y] == 0:
        return
    solve_maze(maze, x + 1, y, path + "D")
    solve_maze(maze, x, y + 1, path + "R")

maze = [[1, 1, 1], [0, 1, 0], [0, 1, 1]]
solve_maze(maze, 0, 0, "")
```

### 2. **Memoization in Recursion**
Memoization stores results of previous function calls to optimize recursive algorithms.
```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))
```

### 3. **Tail Call Optimization (TCO)**
Some languages optimize tail-recursive calls to reduce stack memory usage, but Python does not support TCO natively.

### 4. **Recursion Depth in Python**
Python has a recursion depth limit to prevent excessive memory consumption.
```python
import sys
print(sys.getrecursionlimit())  # Default: 1000
sys.setrecursionlimit(2000)  # Increase limit
```

## Recursion vs Iteration
| Feature       | Recursion         | Iteration           |
|--------------|------------------|---------------------|
| Memory Usage | High (Stack calls)| Low (Loop variables)|
| Performance  | Slower            | Faster              |
| Code Length  | Concise           | Longer              |
| Complexity   | Harder to debug   | Easier to debug     |

## When to Use Recursion
- **Tree/Graph Traversals** (e.g., DFS, BFS)
- **Divide-and-Conquer Algorithms** (e.g., QuickSort, MergeSort)
- **Backtracking Problems** (e.g., N-Queens, Maze Solving)
- **Dynamic Programming** (e.g., Fibonacci with memoization)

## Conclusion
Recursion is a powerful technique that simplifies problem-solving but must be used carefully to avoid excessive memory usage. Advanced concepts like tail recursion, backtracking, and memoization further optimize recursive approaches. Understanding recursion as a runtime stack mechanism helps in debugging and optimizing recursive functions.

