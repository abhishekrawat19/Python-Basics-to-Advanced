# **Object-Oriented Programming (OOP) in Python**

## **Introduction to OOP**
Object-Oriented Programming (OOP) is a paradigm that uses objects and classes to structure software. It helps manage complex real-world applications by organizing data and functionality in an intuitive manner.

### **Why OOP?**
- Helps manage large projects by dividing them into smaller modules.
- Increases **flexibility** and **reusability** of code.
- Enhances **collaboration** between different developers.
- Improves **maintainability** and **scalability** of applications.

---
## **Basic Concepts of OOP**

### **1. Class**
A class is a blueprint for creating objects. It defines properties (variables) and methods (functions) that objects of the class can use.

#### **Syntax:**
```python
class ClassName:
    # Properties and Methods
    pass
```

Example:
```python
class Animal:
    species = "Dog"  # Class property

# Creating an object
obj = Animal()
print(obj.species)  # Output: Dog
```

### **2. Object**
An object is an instance of a class. It contains specific values for the properties defined in the class.

Example:
```python
class Car:
    brand = "Toyota"

my_car = Car()  # Object instantiation
print(my_car.brand)  # Output: Toyota
```

### **3. Object Instantiation**
Creating an object from a class is known as instantiation.

Example:
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 25)  # Instantiation
print(person1.name, person1.age)  # Output: Alice 25
```

---
## **Types of Properties in a Class**

### **1. Class Properties (Static Members)**
These properties are shared by all instances of a class.

Example:
```python
class Bank:
    name = "SBI"  # Class property

print(Bank.name)  # Output: SBI
```

### **2. Instance Properties (Dynamic Members)**
These properties are unique to each object.

Example:
```python
class Customer:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number

cust1 = Customer("John", 12345)
cust2 = Customer("Doe", 67890)
print(cust1.name, cust1.account_number)  # Output: John 12345
print(cust2.name, cust2.account_number)  # Output: Doe 67890
```

---
## **Constructor in Python**
A constructor is a special method (`__init__`) that initializes an object when it is created.

Example:
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Alice", 50000)
print(emp1.name, emp1.salary)  # Output: Alice 50000
```

---
## **Class Method, Object Method & Static Method**

### **1. Object Method (Instance Method)**
- Operates on an instance of the class.
- Uses `self` as the first parameter.

Example:
```python
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def display(self):
        print(f"Student: {self.name}, Grade: {self.grade}")

s1 = Student("John", "A")
s1.display()  # Output: Student: John, Grade: A
```

### **2. Class Method**
- Works with class variables.
- Uses `cls` as the first parameter.
- Declared with `@classmethod`.

Example:
```python
class Bank:
    name = "SBI"
    
    @classmethod
    def update_name(cls, new_name):
        cls.name = new_name

Bank.update_name("HDFC")
print(Bank.name)  # Output: HDFC
```

### **3. Static Method**
- Independent of both class and instance.
- Declared with `@staticmethod`.
- Used for utility purposes.

Example:
```python
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

print(MathOperations.add(5, 3))  # Output: 8
```

---
## **Method Chaining**
Calling multiple methods in a single statement by returning `self`.

Example:
```python
class Car:
    def start(self):
        print("Car started")
        return self
    
    def drive(self):
        print("Car is driving")
        return self
    
    def stop(self):
        print("Car stopped")
        return self

Car().start().drive().stop()
```
**Output:**
```
Car started
Car is driving
Car stopped
```

---
## **Advanced OOP Concepts**

### **1. Private and Protected Members**
- **Private Members**: Not accessible outside the class (`__var`).
- **Protected Members**: Can be accessed within derived classes (`_var`).

Example:
```python
class Person:
    def __init__(self, name, age):
        self._protected = "Protected Variable"
        self.__private = "Private Variable"

obj = Person("John", 30)
print(obj._protected)  # Accessible
# print(obj.__private)  # Error: Cannot access private variable
```

### **2. `__slots__` for Memory Optimization**
Restricts the creation of instance attributes to save memory.

Example:
```python
class Optimized:
    __slots__ = ['name', 'age']
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Optimized("John", 25)
# obj.address = "NY"  # Error: Cannot add new attributes
```

### **3. Name Mangling**
Python renames private variables to prevent accidental access.

Example:
```python
class Test:
    def __init__(self):
        self.__value = 10

obj = Test()
print(obj._Test__value)  # Accessing private variable
```

---
## **Conclusion**
This guide covers essential OOP concepts in Python, including class and object creation, different types of methods, method chaining, and advanced topics like private members and memory optimization. Understanding these concepts is crucial for designing scalable and efficient applications.

