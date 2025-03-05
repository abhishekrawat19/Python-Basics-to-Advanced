# Exception Handling in Python

## What is Exception Handling?
Exception handling is a mechanism in Python that allows us to deal with runtime errors gracefully, preventing crashes and providing meaningful error messages.

## Basic Syntax
Python provides the `try-except` block to catch and handle exceptions.

```python
try:
    # Code that may raise an exception
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
```

## Multiple Exceptions
You can handle multiple exceptions using multiple `except` blocks or a tuple.

```python
try:
    value = int("abc")
except ValueError:
    print("Invalid conversion to integer.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## Catching Any Exception
Using `Exception` catches all exceptions but is not always recommended.

```python
try:
    x = 1 / 0
except Exception as e:
    print(f"An error occurred: {e}")
```

## Finally Block
The `finally` block executes regardless of whether an exception occurs.

```python
try:
    f = open("file.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution completed.")
```

## Else Block
The `else` block executes if no exception occurs.

```python
try:
    num = int("123")
except ValueError:
    print("Invalid number.")
else:
    print("Conversion successful.")
```

## Raising Exceptions
Use `raise` to manually throw exceptions.

```python
x = -5
if x < 0:
    raise ValueError("Negative values are not allowed.")
```

## Custom Exceptions
You can define your own exception classes.

```python
class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error message.")
except CustomError as e:
    print(e)
```

## Types of Exceptions
Python provides several built-in exceptions, including:

### Generic Exceptions
These exceptions are general-purpose and often serve as base classes for more specific exceptions:
- **Exception**: Base class for all exceptions.
- **RuntimeError**: Raised when an error does not fit into any other category.
- **SystemExit**: Raised when `sys.exit()` is called to exit the program.
- **KeyboardInterrupt**: Raised when the user interrupts execution (Ctrl+C).

### Specific Exceptions
These exceptions are raised in well-defined situations:
- **ArithmeticError**: Base class for arithmetic errors.
- **ZeroDivisionError**: Raised when division by zero occurs.
- **ValueError**: Raised when a function receives an argument of the right type but an inappropriate value.
- **TypeError**: Raised when an operation is performed on an incorrect data type.
- **IndexError**: Raised when an index is out of range.
- **KeyError**: Raised when a key is not found in a dictionary.
- **FileNotFoundError**: Raised when a file operation fails because the file does not exist.
- **IOError**: Raised when an I/O operation fails.
- **ImportError**: Raised when an import statement fails.
- **NameError**: Raised when a variable is not defined.
- **AttributeError**: Raised when an invalid attribute reference occurs.
- **MemoryError**: Raised when a program runs out of memory.
- **AssertionError**: Raised when an `assert` statement fails.

### Default Exceptions
These exceptions are raised automatically by the Python interpreter:
- **IndentationError**: Raised when there is an indentation issue in the code.
- **SyntaxError**: Raised when there is a syntax issue in the code.
- **EOFError**: Raised when an unexpected end-of-file condition occurs.
- **FloatingPointError**: Raised when a floating-point operation fails.


