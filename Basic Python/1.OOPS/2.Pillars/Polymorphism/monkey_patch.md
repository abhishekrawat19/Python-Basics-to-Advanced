# Monkey Patching in Python

## 🔹 **What is Monkey Patching?**
Monkey patching is a technique in Python where we **dynamically modify or extend classes and methods at runtime** without altering the original class definition in the source code. The key difference between monkey patching and simple method replacement is that **monkey patching stores the reference of the original method before redefining it**, allowing us to restore it later if needed.

---

## ✅ **Why Use Monkey Patching?**
Monkey patching is commonly used for:
- **Fixing bugs** in third-party libraries without modifying the library code.
- **Modifying the behavior** of a method temporarily.
- **Testing and debugging**, where we override methods to simulate different conditions.
- **Adding features** to a class at runtime without changing its original definition.

---

## ✅ **Correct Example of Monkey Patching**
### 🔹 Storing the Original Method Before Overwriting
Here, we properly store the reference to the original method before replacing it.

```python
class Example:
    def show(self):
        print("Original Method")

# Creating an object
obj = Example()
obj.show()  # Output: Original Method

# 🔹 Store reference of the original method
original_show = Example.show

# 🔹 Define a new method
def patched_show(self):
    print("Patched Method")

# 🔹 Monkey patching: Replacing the method while storing the old one
Example.show = patched_show

obj.show()  # Output: Patched Method

# 🔹 Restoring the original method
obj.show = original_show  # Restoring previous method
obj.show()  # Output: Original Method
```

✔ **Now it's true monkey patching because we stored the original method (`original_show`) before replacing it.**  
✔ We can revert to the original method anytime.

---

## ✅ **Monkey Patching in Method Overloading**
Since Python does not support method overloading, monkey patching allows us to **retain old method versions and still call them when needed**.

```python
class Overload:
    @staticmethod
    def add(a, b):
        return a + b  # First method

# 🔹 Store the reference of the original method before overwriting
previous_add = Overload.add  

@staticmethod
def new_add(a, b):
    return a * b  # New method replaces old method

Overload.add = new_add  # Monkey patching

print(Overload.add(3, 4))   # Output: 12 (Multiplication method)
print(previous_add(3, 4))   # Output: 7  (Restored original method)
```

✔ **Now both the old and new versions can be used.**  
✔ This is useful when we need to **modify behavior but still retain access to the previous method**.

---

## 🎯 **Key Takeaways**
1. **Monkey patching is not just overriding a method—it also involves storing the reference of the original method before redefining it.**  
2. It allows us to **modify class behavior at runtime while keeping the original method accessible**.  
3. This technique is useful in debugging, hotfixing, and testing without permanently changing the original source code.  

🚀 **With proper monkey patching, we can modify behavior dynamically while still maintaining access to the original implementation!**