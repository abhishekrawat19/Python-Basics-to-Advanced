# ============================
# List Comprehension Examples
# ============================

# 1. Basic List Comprehension (Square of numbers)
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)  # Output: [1, 4, 9, 16, 25]

# 2. List Comprehension with Condition (Even Numbers)
even_numbers = [x for x in range(10) if x % 2 == 0]
print("Even Numbers:", even_numbers)  # Output: [0, 2, 4, 6, 8]

# 3. Nested List Comprehension (Multiplication Table)
multiplication_table = [[x * y for x in range(1, 6)] for y in range(1, 6)]
print("Multiplication Table:", multiplication_table)

# 4. List Comprehension with `if-else`
numbers = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print("Even or Odd:", numbers)  # Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# 5. List Comprehension using a Function
def square(n):
    return n * n

squared_numbers = [square(x) for x in range(1, 6)]
print("Squared using Function:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# =====================
# Different Ways to Zip
# =====================

# Sample Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = [100, 200, 300]

# 1. Basic Zip
zipped = list(zip(list1, list2))  # Pairs elements from both lists
print("Zipped List:", zipped)  # Output: [('a', 1), ('b', 2), ('c', 3)]

# 2. Unzipping a Zipped List
unzipped = list(zip(*zipped))  # Unzips the pairs back into separate lists
print("Unzipped:", unzipped)  # Output: [('a', 'b', 'c'), (1, 2, 3)]

# 3. Zipping Three Lists
zipped_three = list(zip(list1, list2, list3))
print("Three-way Zip:", zipped_three)  # Output: [('a', 1, 100), ('b', 2, 200), ('c', 3, 300)]

# 4. Using `zip` in List Comprehension (Concatenating elements)
concatenated = [f"{letter}-{num}" for letter, num in zip(list1, list2)]
print("Concatenated Zipped Elements:", concatenated)  # Output: ['a-1', 'b-2', 'c-3']

# 5. Dictionary from Two Lists using Zip
keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]
person_dict = dict(zip(keys, values))
print("Dictionary from Zip:", person_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# =========================
# Using zip() in a Loop
# =========================
for letter,num in zip(list1, list2):
    print(f"Letter: {letter} num: {num} ")

for letter in zip(list1, list2):
    print(f"Letter: {letter} ")
# ==============
# Final Summary
# ==============
# ✅ List Comprehension provides a compact way to generate lists
# ✅ `zip()` is useful for combining multiple lists
# ✅ `zip(*zipped_list)` unzips the data back into original lists
# ✅ `zip` can be used to create dictionaries and for iteration

