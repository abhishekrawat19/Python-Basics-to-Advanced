from functools import reduce

# Write a lambda function to find the maximum of two numbers.
max_num = (lambda x, y: x if x > y else y)(12, 4)
print(max_num)

# Write a lambda function to check if a number is positive, negative, or zero.
number = (lambda x: "positive" if x > 0 else ("zero" if x == 0 else "negative"))(12)
print(number)

# Create a lambda function to calculate the area of a rectangle given its length and width.
area = (lambda x, y: x * y)(12, 10)
print(area)

# Write a lambda function to check if a given string is a palindrome.
palindrome = (lambda s: "Palindrome" if s == s[::-1] else "Not")("ada")
print(palindrome)

# Use a lambda function to extract even numbers from a list using filter().
a = [12, 12, 3, 4, 6, 8]
even = list(filter(lambda x: x % 2 == 0, a))
print(even)

# Use a lambda function to convert a list of temperatures from Celsius to Fahrenheit using map().
celsius = [32, 0, 34, 27]
fahrenheit = list(map(lambda x: x * (9/5) + 32, celsius))
print(fahrenheit)

# Write a lambda function to compute the factorial of a number using reduce().
num = 5
factorial = reduce(lambda x, y: x * y, range(1, num + 1))
print(factorial)

# Write a lambda function to sort a list of dictionaries based on a specific key.
people = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Charlie", "age": 20}
]
sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)

# Use a lambda function to find the longest word in a list of words.
list1 = ['abhishek', 'sam', 'adams', 'chris']
longest = reduce(lambda a, b: a if len(a) > len(b) else b, list1)
print(longest)

# Write a lambda function to check if a given number is a multiple of both 3 and 5.
check = (lambda x: x % 5 == 0 and x % 3 == 0)(30)
print(check)

# Use a lambda function to capitalize the first letter of each word in a list using map().
list1 = ['abhishek', 'sam', 'adams', 'chris']
caps = list(map(lambda x: x.capitalize(), list1))
print(caps)

# Write a lambda function to find the second largest number in a list.
list1 = [20, 20, 40, 50]
largest = reduce(lambda x, y: x if x > y else y, list1)
new_list = list(filter(lambda x: x != largest, list1))
second_largest = reduce(lambda x, y: x if x > y else y, new_list)
print(second_largest)

# Create a lambda function to compute the sum of squares of a list of numbers using reduce().
list1 = [1, 2, 3]
sum_squares = reduce(lambda x, y: x + y, map(lambda x: x**2, list1))
print(sum_squares)

# Use a lambda function to filter out words from a list that start with a specific letter.
words = ["apple", "banana", "apricot", "cherry", "avocado"]
filtered_words = list(filter(lambda word: not word.startswith('a'), words))
print(filtered_words)

# Write a lambda function to compute the sum of digits of a given number.
num = list(str(123))
sum_digits = reduce(lambda x, y: int(x) + int(y), num)
print(sum_digits)
