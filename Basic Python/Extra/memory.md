
# Memory Allocation in Python

Python handles memory allocation automatically using a combination of stack memory, heap memory, memory manager, and garbage collector.

## 1. Stack Memory (Function Calls & Local Variables)

The stack memory is responsible for storing function calls and local variables. It works on the Last-In-First-Out (LIFO) principle.

### How it Works:
- Whenever a function is called, a stack frame is created.
- All local variables and function arguments are stored in this frame.
- Once the function finishes execution, the frame is removed, freeing memory automatically.

### Example:

```python
def my_function():
    x = 5  # 'x' is stored in stack memory
    y = 10  # 'y' is stored in stack memory
    return x + y

result = my_function()
```

## 2. Heap Memory (Objects & Data Structures)

The heap memory is where all objects (like lists, dictionaries, class instances) are stored. Unlike stack memory, heap memory is not automatically freed when a function ends.

### How it Works:
- Objects are stored in heap memory.
- Variables in the stack hold references (pointers) to these objects.
- The Garbage Collector manages heap memory.

### Example:

```python
a = [1, 2, 3]  # List is stored in heap memory
b = a          # Both 'a' and 'b' point to the same memory location
```

## 3. Python Memory Manager

Python has an internal Memory Manager that decides how memory is allocated and optimized.

### Memory Pools:
- Python doesn't directly request memory from the OS for each object.
- Instead, it uses memory pools to optimize allocations.

### Types of Memory Allocators:
1. **PyObject_Malloc** → Allocates memory for Python objects.
2. **PyMem_Malloc** → Used for low-level memory allocation.
3. **PyMalloc** → An optimized memory allocator for small objects.

## 4. Garbage Collection (Automatic Memory Cleanup)

Python automatically frees memory using garbage collection.

### How it Works:

### 1. Reference Counting (Primary Mechanism)

Each object keeps track of how many variables reference it. When the reference count reaches zero, the object is deleted.

#### Example:

```python
import sys

a = [1, 2, 3]
print(sys.getrefcount(a))  # Shows the reference count
b = a  # Another reference to the same list
print(sys.getrefcount(a))  # Reference count increases
del a
del b  # Now the object is removed from memory
```

### 2. Cyclic Garbage Collection (Handles Circular References)

If objects reference each other, their reference count never reaches zero. Python's `gc` module detects and removes such cycles.

#### Example:

```python
import gc

class Node:
    def __init__(self):
        self.reference = self  # Circular reference

obj = Node()
del obj  # The object is still in memory due to self-reference

gc.collect()  # Explicitly trigger garbage collection
```

## Summary

1. **Stack Memory** stores function calls and local variables (automatically freed).
2. **Heap Memory** stores objects (managed by the garbage collector).
3. **Memory Manager** optimizes memory allocation using pools.
4. **Garbage Collection** cleans up unused memory using reference counting and cycle detection.
