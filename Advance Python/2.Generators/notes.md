# **Generators in Python**

## **What is a Generator?**
A **generator** is a special type of function that generates a sequence of values **lazily** (on-demand) instead of returning them all at once. Generators are created using the `yield` keyword.
It generate the sequence of value.

---

## **Key Characteristics of Generators**
1. **Memory Efficient:** Unlike lists, generators do not store all values in memory, making them useful for handling large datasets.
2. **Lazy Evaluation:** They generate values one at a time and only when needed, improving performance.
3. **Iterators:** Generators are iterators, meaning they can be used in loops and with functions like `next()`.

---

## **How to Create a Generator?**
A function that contains at least one `yield` statement is considered a **generator function**. Unlike `return`, `yield` allows the function to pause execution and resume where it left off.

`yield` is a keyword which is used to return n number of values without breaking the flow of execution unlike the return.

### **Syntax of a Generator Function:**
```python
    def generator_name():
        yield value1
        yield value2
        yield value3
```

### **Example:**
```python
def gene():
    print("Hi")
    yield 10
    print("Hello")
    yield 20
    print("Hi")
    yield 30
    print("Hello")

# Calling the generator function
var = gene()

# Accessing the generator values
print(next(var))  # Output: Hi 10
print(next(var))  # Output: Hello 20
print(next(var))  # Output: Hi 30
```

---

## **Typecasting a Generator**
A generator function returns a **generator object**. To retrieve all values at once, you can typecast it into a list, tuple, or set.

### **Example:**
```python
print(list(gene()))  # Output: ['Hi', 10, 'Hello', 20, 'Hi', 30, 'Hello']
print(tuple(gene()))  # Output: ('Hi', 10, 'Hello', 20, 'Hi', 30, 'Hello')
print(set(gene()))  # Output: {'Hi', 'Hello', 10, 20, 30}
```

---

## **Difference Between `return` and `yield`**
| Feature        | `return` | `yield` |
|--------------|---------|--------|
| Returns      | Single value | Multiple values lazily |
| Function Type | Normal Function | Generator Function |
| Execution    | Terminates function | Pauses and resumes |
| Memory Usage | High (stores all values) | Low (on-demand generation) |

---

## **Advanced Generator Concepts**

### **1. Using Generators with Loops**
Instead of using `next()`, you can use a generator inside a loop to iterate over its values.

```python
def counter(n):
    for i in range(n):
        yield i

for value in counter(5):
    print(value)  # Output: 0 1 2 3 4
```

### **2. Generator Expressions (Similar to List Comprehensions)**
Python provides a shorter syntax for generators using **generator expressions**, similar to list comprehensions.

```python
# List comprehension
list_comp = [x*x for x in range(5)]  # Stores all values at once

# Generator expression
gen_expr = (x*x for x in range(5))  # Generates values one by one

print(list_comp)  # Output: [0, 1, 4, 9, 16]
print(list(gen_expr))  # Output: [0, 1, 4, 9, 16]
```

### **3. Using `send()` to Pass Values to Generators**
The `send()` method allows us to send values into a generator, making it more interactive.

```python
def interactive_gen():
    value = yield "Start"
    yield f"Received: {value}"

# Creating generator object
g = interactive_gen()
print(next(g))  # Output: Start
print(g.send(42))  # Output: Received: 42
```

### **4. Using `yield from` to Yield from Another Generator**
The `yield from` keyword simplifies working with nested generators.

```python
def sub_generator():
    yield 1
    yield 2
    yield 3

def main_generator():
    yield from sub_generator()
    yield 4

print(list(main_generator()))  # Output: [1, 2, 3, 4]
```

### **5. Infinite Generators**
Generators can be used to create infinite sequences.

```python
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

count = infinite_counter()
print(next(count))  # Output: 0
print(next(count))  # Output: 1
print(next(count))  # Output: 2
```

---

## **Conclusion**
Generators are a powerful feature in Python, enabling memory-efficient, lazy evaluation of data sequences. They are useful in scenarios like data streaming, file handling, and large computations. Understanding how to leverage generators can significantly improve performance and resource usage in Python applications.

