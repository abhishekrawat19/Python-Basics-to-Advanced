# Method Overriding

## Definition
Method overriding is a feature in object-oriented programming where a subclass provides a specific implementation of a method that is already defined in its parent class. The implementation in the child class overrides the implementation in the parent class.

### Key Requirements for Method Overriding:
1. **Inheritance**: The child class must inherit from the parent class.
2. **Same Method Name**: The method name in the child class should be the same as the one in the parent class.
3. **Same Method Signature**: The method signature (method name + parameters) should be the same.
4. **Different Implementation**: The child class provides a specific implementation according to its own needs.

## Example:
```python
class Parent:
    a = 10
    
    @staticmethod
    def marriage():
        print("You are going to marry")

class Child(Parent):
    a = 100
    
    @staticmethod
    def marriage():
        print("You are going on a trip")

ob1 = Child()
ob1.marriage()  # Calls the overridden method in the Child class
print(ob1.a)    # Prints the overridden attribute in the Child class
```

### Output:
```
You are going on a trip
100
```

## Important Points:
- The overridden method in the child class completely replaces the method from the parent class.
- If you want to call the parent class method inside the child class, you can use `super()`.

## Advanced Concepts

### 1. Calling Parent Method Using `super()`
Sometimes, we may need to call the overridden method from the parent class. This can be done using `super()`:

```python
class Parent:
    def show(self):
        print("This is Parent class method")

class Child(Parent):
    def show(self):
        super().show()  # Calling Parent's method
        print("This is Child class method")

obj = Child()
obj.show()
```

### Output:
```
This is Parent class method
This is Child class method
```

### 2. Overriding `__init__()` Constructor
A child class can override the constructor of the parent class:

```python
class Parent:
    def __init__(self, name):
        print(f"Parent Constructor: {name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Calling Parent Constructor
        print(f"Child Constructor: {age}")

obj = Child("Alice", 25)
```

### Output:
```
Parent Constructor: Alice
Child Constructor: 25
```

### 3. Method Overriding with Different Return Types
In Python, unlike Java, method overriding can have different return types.

```python
class Parent:
    def get_value(self):
        return "Parent Value"

class Child(Parent):
    def get_value(self):
        return 100  # Different return type

obj = Child()
print(obj.get_value())
```

### Output:
```
100
```

### 4. Private Methods and Overriding
Private methods (prefix `__`) cannot be overridden directly because they are name-mangled.

```python
class Parent:
    def __private_method(self):
        print("Parent Private Method")
    
    def call_private(self):
        self.__private_method()

class Child(Parent):
    def __private_method(self):
        print("Child Private Method")

obj = Child()
obj.call_private()  # Calls Parent's method
```

### Output:
```
Parent Private Method
```

**Explanation**: The private method in the Child class does not override the parent's private method due to name-mangling.

## Summary
- **Method overriding** allows customization of inherited behavior in a subclass.
- Use `super()` to access the parent class method.
- Constructors (`__init__`) can also be overridden.
- Overridden methods can have different return types in Python.
- Private methods cannot be directly overridden due to name-mangling.

This concept is essential in achieving **polymorphism** in object-oriented programming.

