# **Abstraction in Python**

## **What is Abstraction?**
Abstraction is a fundamental concept in **Object-Oriented Programming (OOP)** that is used to **hide** the internal implementation of a process while providing **only the necessary functionality** to the user.

Hiding the internal implementation by providing the functionality to the user is known as abstraction.

While working with real time project or designing the software or apps the Architects will make use of abstraction..


### **Key Features of Abstraction:**
1. **Hides Implementation Details:** The internal workings of a process are not exposed to the user.
2. **Simplifies Software Development:** Users interact with only the necessary parts of the system.
3. **Enhances Security:** Restricts direct access to certain functionalities.
4. **Widely Used in Software Development:** Helps in designing large-scale applications.

---

## **Key Components of Abstraction**
### **1. Abstract Class**
An **abstract class** is a class that contains at least one **abstract method** (a method that is declared but not implemented). Abstract classes serve as **blueprints** for other classes.

- Abstract classes **cannot be instantiated** directly.
- They must **inherit from the `ABC` (Abstract Base Class) module**.

### **2. Abstract Method**
An **abstract method** is a method that is declared but not implemented inside an abstract class. It is defined using the **`@abstractmethod` decorator** from the `abc` module.

### **3. Concrete Class**
A **concrete class** is a class that **implements all the abstract methods** of its parent abstract class. It can be instantiated (object creation is possible).

---

## **Implementing Abstraction in Python**
To use abstraction in Python, we need to import `ABC` and `abstractmethod` from the `abc` module.
Abstract Base Class
### **Example: Implementing Abstract Class & Method**
```python
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method with no implementation

    @abstractmethod
    def habitat(self):
        pass

# Concrete class implementing abstract methods
class Dog(Animal):
    def sound(self):
        return "Barks"
    
    def habitat(self):
        return "Domestic"

# Object creation
dog = Dog()
print(dog.sound())   # Output: Barks
print(dog.habitat()) # Output: Domestic
```

### **Explanation:**
1. **Animal** is an **abstract class**.
2. **sound() and habitat()** are **abstract methods**.
3. **Dog** is a **concrete class** that implements the abstract methods.
4. Since all abstract methods are implemented, an object of `Dog` can be created.

---

## **Advanced Concepts in Abstraction**

### **1. Preventing Object Creation of Abstract Class**
An **abstract class cannot be instantiated**, meaning you cannot create an object of an abstract class.

```python
animal = Animal()  # This will raise an error
```
**Error:** `TypeError: Can't instantiate abstract class Animal with abstract methods sound, habitat`

---

### **2. Using `super()` in Abstract Methods**
Sometimes, abstract classes may provide partial implementation and require subclasses to extend the functionality.

```python
class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def details(self):
        print(f"Brand: {self.brand}")

class Car(Vehicle):
    def details(self):
        super().details()
        print("Type: Car")

car = Car("Toyota")
car.details()
```
**Output:**
```
Brand: Toyota
Type: Car
```

- `super().details()` calls the implementation in `Vehicle` before adding subclass-specific details.

---

### **3. Abstract Class with Concrete Methods**
Abstract classes can have **both abstract and concrete methods**.

```python
class Shape(ABC):
    def area(self):
        print("Calculating area...")
    
    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def perimeter(self):
        return 4 * self.side

sq = Square(5)
sq.area()  # Output: Calculating area...
print(sq.perimeter())  # Output: 20
```

- The `area()` method is **concrete**, meaning it can be directly used by subclasses.
- The `perimeter()` method is **abstract** and must be implemented in subclasses.

---

### **4. Multiple Inheritance with Abstract Classes**
Abstract classes can be used in multiple inheritance scenarios.

```python
class Engine(ABC):
    @abstractmethod
    def engine_type(self):
        pass

class Wheels(ABC):
    @abstractmethod
    def wheel_count(self):
        pass

class Car(Engine, Wheels):
    def engine_type(self):
        return "Petrol"
    
    def wheel_count(self):
        return 4

car = Car()
print(car.engine_type())  # Output: Petrol
print(car.wheel_count())  # Output: 4
```

- The `Car` class **inherits from multiple abstract classes** and must implement all abstract methods.

---

## **Key Differences Between Abstract Class and Concrete Class**

| Feature        | Abstract Class | Concrete Class |
|--------------|--------------|---------------|
| Abstract Methods | Yes | No |
| Object Creation | Not possible | Possible |
| Used For | Defining a blueprint | Implementing full functionality |

---

## **Conclusion**
- **Abstraction helps in hiding complex implementations** and exposing only necessary functionality.
- **Abstract classes** act as **blueprints** for child classes.
- **Concrete classes** implement abstract methods and can be instantiated.
- **Advanced features like multiple inheritance and `super()` usage make abstraction powerful**.

Abstraction is widely used in software development, making code **scalable, maintainable, and secure**.

---

