# Python Error Handling - Comprehensive Example

# Custom Exception Class
class UnderageError(Exception):
    """Custom exception for age restrictions."""

    def __init__(self, age, message="You must be 18 or older."):
        self.age = age
        self.message = message
        super().__init__(self.message)


# Function that raises a custom error
def check_age(age):
    """Checks if age is 18 or above; raises an UnderageError otherwise."""
    if age < 18:
        raise UnderageError(age)
    return "Access granted!"


# Function to safely divide numbers
def safe_divide(a, b):
    """Performs division and handles ZeroDivisionError."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"


# File handling with try-except-finally
def read_file(filename):
    """Tries to read a file and handles FileNotFoundError."""
    try:
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        return "Error: File not found!"
    finally:
        print("Closing file (if it was opened).")
        if "file" in locals():  # Check if file was opened
            file.close()


# Loop for user input validation
def get_valid_number():
    """Keeps asking for a valid number until user provides one."""
    while True:
        try:
            num = int(input("Enter a number: "))
            return num
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Demonstration of multiple exception handling
def multiple_exception_handling():
    """Handles multiple exceptions in a single try block."""
    try:
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")
    except ValueError:
        print("Error: Invalid input! Please enter a number.")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")


# Main Execution
if __name__ == "__main__":
    print("\n--- Custom Exception Handling ---")
    try:
        age = int(input("Enter your age: "))
        print(check_age(age))
    except UnderageError as e:
        print(f"Custom Error: {e}")

    print("\n--- Safe Division ---")
    print(safe_divide(10, 0))  # Demonstrates handling ZeroDivisionError

    print("\n--- File Handling ---")
    print(read_file("non_existent_file.txt"))  # Demonstrates handling FileNotFoundError

    print("\n--- User Input Validation ---")
    valid_number = get_valid_number()
    print(f"Valid number entered: {valid_number}")

    print("\n--- Multiple Exception Handling ---")
    multiple_exception_handling()  # Demonstrates handling multiple errors

    print("\n--- Program Completed Successfully! ---")


class UnderageError(Exception):
    """Custom exception for age restrictions."""

    def __init__(self, age, message="You must be 18 or older."):
        self.age = age  # Storing age
        self.message = message
        super().__init__(self.message)  # Calls Exception's constructor


try:
    age = 16
    if age < 18:
        raise UnderageError(age)  # Raising the custom exception
except UnderageError as e:
    print(f"Custom Error: {e.message} (Age entered: {e.age})")
