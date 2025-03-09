# Q1: How can we update all student marks by adding 5 using `map()` in Python?
students = {'abhi': 90, "sam": 55, "adam": 33}

# Using map() to increase each student's marks by 5
update_stu = dict(map(lambda item: (item[0], item[1] + 5), students.items()))

print("Updated Student Marks:", update_stu)  # {'abhi': 95, 'sam': 60, 'adam': 38}


# Q2: How can we filter students who scored more than 50 using `filter()`?
top_student = dict(filter(lambda item: item[1] > 50, students.items()))

print("Students with marks > 50:", top_student)  # {'abhi': 90, 'sam': 55}


# Q3: How can we convert a list of names into uppercase using `map()`?
list1 = ['abhi', 'shek']

# Using lambda to convert each name to uppercase
upper_name = list(map(lambda x: x.upper(), list1))
print("Uppercase Names:", upper_name)  # ['ABHI', 'SHEK']

# Using `str.capitalize()` to capitalize first letter
caps = list(map(str.capitalize, list1))
print("Capitalized Names:", caps)  # ['Abhi', 'Shek']


# Q4: How can we calculate the total marks of all students using `reduce()`?
from functools import reduce

total_marks = reduce(lambda total, x: x[1] + total, students.items(), 0)
print("Total Marks:", total_marks)  # 178


# Q5: How can we find the student with the highest marks using `reduce()`?
highest_marks = reduce(lambda a, b: a if a[1] > b[1] else b, students.items())
print("Highest Scoring Student:", highest_marks)  # ('abhi', 90)


# Q6: How can we filter key-value pairs where key and value are of the same type?
ok = {'abhi': 'abhishek', 'fruit': 12, 10: 23, 100: 7.5}

def check(item):
    key, val = item  # Extract key-value pair
    return type(key) is type(val)  # Check if key and value have the same type

# Apply filter to keep only matching key-value types
new = dict(filter(check, ok.items()))
print("Filtered Dictionary:", new)  # {'abhi': 'abhishek', 10: 23}
