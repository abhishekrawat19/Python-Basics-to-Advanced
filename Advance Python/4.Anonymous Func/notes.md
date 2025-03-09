# Anonymous Functions in Python

## What is an Anonymous Function?
- An **anonymous function** in Python is a function that is defined **without a name**.
- These functions are created using the `lambda` keyword.
- They are often called **lambda functions**.

## Syntax of Lambda Function
```python
lambda arguments: expression
```

- The `lambda` keyword is used to define the function.
- It can take any number of arguments, but only **one expression**.
- The expression is **evaluated** and **returned**.

## Example Usage

### 1. Basic Lambda Function
```python
square = lambda x: x * x
print(square(5))  # Output: 25
```

### 2. Lambda with Multiple Arguments
```python
add = lambda x, y: x + y
print(add(3, 7))  # Output: 10
```

### 3. Using Lambda with `map()`
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
```

### 4. Using Lambda with `filter()`
```python
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]
```

### 5. Using Lambda with `sorted()`
```python
pairs = [(1, 2), (4, 1), (9, 10), (13, -3)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # Output: [(13, -3), (4, 1), (1, 2), (9, 10)]
```

## When to Use Lambda Functions
- When you need a **small, simple function** for a **short period**.
- Useful in **higher-order functions** like `map()`, `filter()`, and `sorted()`.
- Avoid using them for **complex logic** (use `def` functions instead).

## Limitations of Lambda Functions
- Limited to **one expression only** (no multiple statements).
- Less readable compared to normal functions for complex logic.

## Conclusion
Lambda functions provide a **quick and concise** way to create anonymous functions, especially useful for simple operations. However, for **readability and maintainability**, regular `def` functions should be preferred for complex logic.
