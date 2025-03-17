# **Encapsulation in Python**

## **What is Encapsulation?**
Encapsulation is the process of **wrapping data and functionality** into a single unit. It provides **security** to class members using **access specifiers**.

Encapsulation ensures **data hiding**, preventing direct modification of variables outside the class.

In some places, access specifiers are also known as **access modifiers**.

---

## **Types of Access Specifiers**
Access specifiers determine whether a user can access the data outside of the class or not. There are three types:

### **1. Public Access Specifier**
- Members of the class that can be accessed **outside** the class.
- By default, variables and methods declared inside a class are **public**.

#### **Example:**
```python
class PublicExample:
    def __init__(self, name):
        self.name = name  # Public variable

    def display(self):
        print("Name:", self.name)  # Public method

obj = PublicExample("Alice")
print(obj.name)  # Accessible
obj.display()  # Accessible
```

---

### **2. Protected Access Specifier**
- Members of the class that **should be protected** from outside access.
- Defined using **a single underscore (`_`)** before the variable name.
- In Python, **protected members are not strictly restricted**, but it's a convention to indicate that they should not be accessed directly.

#### **Example:**
```python
class ProtectedExample:
    def __init__(self):
        self._protected_var = 10  # Protected variable

    def _protected_method(self):
        print("Protected Method")

obj = ProtectedExample()
print(obj._protected_var)  # Can still be accessed (Not strictly restricted)
obj._protected_method()  # Can still be accessed
```

---

### **3. Private Access Specifier**
- Members of the class that **cannot be accessed** outside the class.
- Defined using **double underscore (`__`)** before the variable name.
- Prevents direct access but can be accessed using **name mangling** (`_ClassName__variable`).

#### **Example:**
```python
class PrivateExample:
    def __init__(self):
        self.__private_var = 20  # Private variable

    def __private_method(self):
        print("Private Method")

    def access_private(self):
        print("Accessing Private Variable:", self.__private_var)
        self.__private_method()

obj = PrivateExample()
# print(obj.__private_var)  # This will raise an AttributeError
obj.access_private()  # Correct way to access private members

# Accessing Private Members using Name Mangling
print(obj._PrivateExample__private_var)  # Accessing private variable
obj._PrivateExample__private_method()  # Accessing private method
```

---

## **Methods to Access Private Members**
To access private members outside the class, we use **getter and setter methods**.

### **1. Getter Method (`get`)**
- Used to retrieve private variables.
- Defined using a method that returns the private variable.

#### **Example:**
```python
class Person:
    def __init__(self, age):
        self.__age = age  # Private variable

    def get_age(self):  # Getter method
        return self.__age

p = Person(25)
print(p.get_age())  # Output: 25
```

### **2. Setter Method (`set`)**
- Used to modify private variables.
- Defined using a method that updates the private variable.

#### **Example:**
```python
class Person:
    def __init__(self, age):
        self.__age = age  # Private variable

    def set_age(self, new_age):  # Setter method
        if new_age > 0:
            self.__age = new_age
        else:
            print("Age must be positive!")

p = Person(25)
p.set_age(30)
print(p.get_age())  # Output: 30
```

---

## **Advanced Concepts of Encapsulation**

### **1. Name Mangling for Private Variables**
Python provides a mechanism called **name mangling**, which modifies the variable name to avoid conflicts.
- Private members are accessed using `_ClassName__variableName`.
- However, **direct access is not recommended** as it breaks encapsulation.

#### **Example:**
```python
class Sample:
    def __init__(self):
        self.__private_var = "Secret"

obj = Sample()
print(obj._Sample__private_var)  # Accessing private variable (Not recommended)
```

---

### **2. Using Properties for Encapsulation**
Python provides the `@property` decorator to create **getter and setter** methods in a cleaner way.

#### **Example:**
```python
class Product:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self):  # Getter method
        return self.__price

    @price.setter
    def price(self, new_price):  # Setter method
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive!")

p = Product(1000)
print(p.price)  # Calls getter method
p.price = 1500  # Calls setter method
print(p.price)
```

---

### **3. Preventing Direct Modification with `__slots__`**
- Using `__slots__`, we can restrict the creation of new attributes dynamically, improving memory efficiency.

#### **Example:**
```python
class SlotExample:
    __slots__ = ['name', 'age']  # Only these attributes are allowed
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = SlotExample("John", 25)
obj.name = "Alice"
# obj.address = "New York"  # This will raise an AttributeError
print(obj.name)
```

---

## **Conclusion**
Encapsulation is an essential concept in object-oriented programming that ensures **data hiding** and **controlled access**. By using access specifiers, **public, protected, and private**, we can manage access to class members effectively. Advanced techniques like **getter/setter methods, `@property`, name mangling, and `__slots__`** further enhance security and performance in Python applications.

