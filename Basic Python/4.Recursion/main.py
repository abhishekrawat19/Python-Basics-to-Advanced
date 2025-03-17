# Recursive Problems in Python

# 1. Factorial Calculation
# Write a recursive function to compute the factorial of a number.
def factorial(n):
    if n == 1:
        return 1  # Base case: factorial of 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive call with n-1
print(factorial(5))  # Expected output: 120

# 2. Fibonacci Series
# Write a recursive function to return the nth Fibonacci number.
def fibonacci(n):
    if n == 0:
        return 0  # Base case: Fibonacci of 0 is 0
    elif n == 1:
        return 1  # Base case: Fibonacci of 1 is 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Sum of previous two numbers
print(fibonacci(6))  # Expected output: 8

# 3. Sum of Digits
# Write a recursive function to calculate the sum of digits of a number.
def sum_of_digits(n):
    if n == 0:
        return 0  # Base case: sum of digits of 0 is 0
    else:
        return (n % 10) + sum_of_digits(n // 10)  # Extract last digit and recurse
print(sum_of_digits(1234))  # Expected output: 10

# 4. Reverse a String
# Write a function that reverses a given string using recursion.
def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])
print(reverse_string("hello"))  # Expected: "olleh"

# 5. Power Function (x^n)
# Implement a function to calculate x raised to the power n using recursion.
def power(x, n):
    if n == 0:
        return 1  # Base case: any number raised to 0 is 1
    else:
        return x * power(x, n - 1)  # Multiply x recursively
print(power(2, 3))  # Expected: 8

# 6. Check Palindrome
# Write a function that checks if a string is a palindrome using recursion.
def is_palindrome(s):
    if len(s) <= 1:
        return True  # Base case: single character or empty string is palindrome
    if s[0] != s[-1]:
        return False  # If first and last characters do not match, return False
    return is_palindrome(s[1:-1])  # Check remaining substring
print(is_palindrome("racecar"))  # Expected: True

# 7. Greatest Common Divisor (GCD)
# Implement a function to find the GCD of two numbers using recursion.
def gcd(a, b):
    if b == 0:
        return a  # Base case: when remainder is 0, return a
    else:
        return gcd(b, a % b)  # Recursive call with remainder
print(gcd(48, 18))  # Expected: 6

# 8. Count Occurrences of a Character in a String
# Write a recursive function to count occurrences of a given character in a string.
def count_char(s, char):
    if len(s) == 0:
        return 0  # Base case: empty string has 0 occurrences
    count = 1 if s[0] == char else 0
    return count + count_char(s[1:], char)  # Count and recurse on substring
print(count_char("banana", "a"))  # Expected: 3

# 9. Tower of Hanoi
# Implement the Tower of Hanoi problem using recursion.
def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)
tower_of_hanoi(3, "A", "B", "C")

# 10. Find the Maximum Element in a List
# Write a recursive function to find the maximum element in a list.
def find_max(lst, n):
    if n == 1:
        return lst[0]  # Base case: when only one element is left, return it
    return max(lst[n - 1], find_max(lst, n - 1))  # Compare last element with max of rest
print(find_max([1, 4, 9, 3, 7], 5))  # Expected: 9
