# 1. Concatenate Two Strings Using a Lambda Function
concat_strings = lambda s1, s2: s1 + ' ' + s2
print(concat_strings("Hello", "World"))  # Output: "Hello World"

# 2. Concatenate a List of Strings Using `reduce()` and Lambda
from functools import reduce
string_list = ["Lambda", "functions", "are", "powerful"]
concatenated = reduce(lambda x, y: x + ' ' + y, string_list)
print(concatenated)  # Output: "Lambda functions are powerful"

# 3. Sort a List of Tuples Based on String Length Using Lambda
tuples_list = [("apple", 5), ("banana", 6), ("kiwi", 4)]
sorted_tuples = sorted(tuples_list, key=lambda x: len(x[0]))
print(sorted_tuples)  # Output: [('kiwi', 4), ('apple', 5), ('banana', 6)]

# 4. Find the Most Frequent Character in a String Using Lambda
from collections import Counter
most_frequent_char = lambda s: max(Counter(s).items(), key=lambda x: x[1])[0]
print(most_frequent_char("banana"))  # Output: "a"

# 5. Replace Spaces in a String with a Specific Character Using Lambda
replace_spaces = lambda s, char: s.replace(" ", char)
print(replace_spaces("hello world", "-"))  # Output: "hello-world"

# 6. Convert a List of Strings to Uppercase Using `map()` and Lambda
string_list = ["python", "lambda", "functions"]
uppercase_list = list(map(lambda s: s.upper(), string_list))
print(uppercase_list)  # Output: ["PYTHON", "LAMBDA", "FUNCTIONS"]

# 7. Generate a Fibonacci Sequence Using Lambda and `reduce()`
fib_sequence = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]], range(n-2), [0, 1])
print(fib_sequence(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 8. Filter Palindromes from a List Using Lambda and `filter()`
word_list = ["madam", "hello", "racecar", "world", "level"]
palindromes = list(filter(lambda w: w == w[::-1], word_list))
print(palindromes)  # Output: ['madam', 'racecar', 'level']

# 9. Compute the Product of Even Numbers in a List Using Lambda
even_numbers_product = lambda lst: reduce(lambda x, y: x * y, filter(lambda x: x % 2 == 0, lst))
print(even_numbers_product([1, 2, 3, 4, 5, 6]))  # Output: 48

# 10. Group Strings by Their First Letter Using `groupby()` and Lambda
from itertools import groupby
words = ["apple", "banana", "apricot", "cherry", "avocado", "blueberry"]
words.sort()  # groupby requires sorted data
grouped_words = {k: list(v) for k, v in groupby(words, key=lambda x: x[0])}
print(grouped_words)  # Output: {'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry'], 'c': ['cherry']}

from functools import reduce

# 11. Concatenate a List of Strings Using reduce()
words = ["Hello", " ", "World", "!", " Python", " is", " fun"]
concatenated = reduce(lambda x, y: x + y, words)
print(concatenated)  # Output: "Hello World! Python is fun"

# 12. Concatenate Two Strings with a Separator Using Lambda
concat_strings = lambda s1, s2, sep=" ": s1 + sep + s2
print(concat_strings("Lambda", "Functions"))  # Output: "Lambda Functions"
print(concat_strings("Hello", "World", "-"))  # Output: "Hello-World"

# 13. Concatenate Strings in a List Using join() and Lambda
words = ["Python", "is", "awesome"]
concat = lambda lst: " ".join(lst)
print(concat(words))  # Output: "Python is awesome"

# 14. Concatenate Reversed Strings in a List Using map()
words = ["hello", "world", "python"]
reverse_concat = lambda lst: "".join(map(lambda x: x[::-1], lst))
print(reverse_concat(words))  # Output: "ollehdlrownohtyp"
