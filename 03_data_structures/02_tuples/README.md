# Python Tuples - Complete Guide

Tuples are **immutable**, ordered collections that cannot be changed after creation. They are perfect for storing data that should remain constant throughout your program's execution.

## 📁 Related Files

- **`tuple_operations.py`** - Basic tuple operations and iteration
- **`tuples_README.md`** - This comprehensive guide for tuples

## 🎯 What are Tuples?

Tuples are:
- **Immutable**: Cannot be changed after creation
- **Ordered**: Items have a defined order and maintain that order
- **Indexed**: Access items using numerical indices (starting from 0)
- **Hashable**: Can be used as dictionary keys (if all elements are hashable)
- **Heterogeneous**: Can store different data types
- **Memory Efficient**: Use less memory than lists

## 🔧 Basic Tuple Operations

### Creating Tuples
```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Tuple with values
coordinates = (10, 20)
colors = ("red", "green", "blue")
mixed = ("hello", 42, True, 3.14)

# Single item tuple (note the comma!)
single_item = (42,)          # Comma is required
single_item = 42,            # Alternative syntax

# Without parentheses (tuple packing)
point = 10, 20               # Creates tuple (10, 20)
name, age = "John", 25       # Creates and unpacks tuple

# From other iterables
from_list = tuple([1, 2, 3])       # (1, 2, 3)
from_string = tuple("hello")       # ('h', 'e', 'l', 'l', 'o')
from_range = tuple(range(5))       # (0, 1, 2, 3, 4)
```

### Accessing Elements
```python
colors = ("red", "green", "blue", "yellow")

# Positive indexing
first_color = colors[0]      # "red"
second_color = colors[1]     # "green"

# Negative indexing (from the end)
last_color = colors[-1]      # "yellow"
second_last = colors[-2]     # "blue"

# Slicing (returns a new tuple)
some_colors = colors[1:3]    # ("green", "blue")
first_two = colors[:2]       # ("red", "green")
last_two = colors[-2:]       # ("blue", "yellow")
all_colors = colors[:]       # Creates a copy of the tuple
```

## 🔒 Immutability Features

### From `tuple_operations.py` Example
```python
# Tuple: Immutable List
names = ("Sanjeet", "Mohan")

# This would cause an error - tuples are immutable!
# names[0] = "Rohit"  # TypeError: 'tuple' object does not support item assignment

# Iteration works the same as lists
for name in names:
    print(name)
```

### What Immutability Means
```python
point = (10, 20)

# These operations are NOT allowed:
# point[0] = 15        # TypeError
# point.append(30)     # AttributeError
# del point[0]         # TypeError
# point.remove(10)     # AttributeError

# But you can reassign the entire tuple
point = (15, 25)       # This creates a new tuple
```

### Mutable Objects in Tuples
```python
# Tuple containing mutable objects
data = ([1, 2], [3, 4])

# The tuple itself is immutable
# data[0] = [5, 6]     # Error: can't reassign tuple element

# But the mutable objects inside can be modified
data[0].append(3)      # This works: ([1, 2, 3], [3, 4])
data[1][0] = 99        # This works: ([1, 2, 3], [99, 4])
```

## 📊 Tuple Methods and Operations

### Limited Methods (Due to Immutability)
```python
numbers = (1, 2, 3, 2, 1, 4, 2, 5)

# Available methods
count_of_2 = numbers.count(2)    # Count occurrences: 3
index_of_3 = numbers.index(3)    # Find first index: 2

# General operations
length = len(numbers)            # Length: 8
maximum = max(numbers)           # Maximum: 5
minimum = min(numbers)           # Minimum: 1
total = sum(numbers)             # Sum: 20

# Membership testing
has_3 = 3 in numbers            # True
no_6 = 6 not in numbers         # True
```

### Tuple Concatenation and Repetition
```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

# Concatenation (creates new tuple)
combined = tuple1 + tuple2       # (1, 2, 3, 4, 5, 6)

# Repetition (creates new tuple)
repeated = tuple1 * 3            # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Note: Original tuples remain unchanged
print(tuple1)                    # Still (1, 2, 3)
```

## 🎯 Tuple Unpacking

### Basic Unpacking
```python
point = (10, 20)
x, y = point                     # x = 10, y = 20

person = ("Alice", 25, "Engineer")
name, age, job = person          # Unpack all elements

# Swapping variables (Pythonic way)
a, b = 5, 10
a, b = b, a                      # Now a = 10, b = 5
```

### Advanced Unpacking
```python
numbers = (1, 2, 3, 4, 5)

# Unpack with star operator (Python 3+)
first, *middle, last = numbers   # first=1, middle=[2,3,4], last=5
first, second, *rest = numbers   # first=1, second=2, rest=[3,4,5]
*beginning, last = numbers       # beginning=[1,2,3,4], last=5

# Ignoring values with underscore
first, _, third, *_ = numbers    # Only keep first and third
```

### Function Returns
```python
def get_name_age():
    """Return multiple values as a tuple"""
    return "John", 25

def get_statistics(data):
    """Return multiple statistics"""
    return min(data), max(data), sum(data) / len(data)

# Unpacking returned tuples
name, age = get_name_age()
minimum, maximum, average = get_statistics([1, 2, 3, 4, 5])

# Using returned tuple directly
stats = get_statistics([1, 2, 3, 4, 5])
print(f"Min: {stats[0]}, Max: {stats[1]}, Avg: {stats[2]}")
```

## 🔄 Converting Between Types

### Tuple ↔ List Conversion
```python
# Tuple to list
my_tuple = (1, 2, 3, 4)
my_list = list(my_tuple)         # [1, 2, 3, 4]

# List to tuple
my_list = [1, 2, 3, 4]
my_tuple = tuple(my_list)        # (1, 2, 3, 4)

# Useful for temporary modification
coords = (10, 20, 30)
temp_list = list(coords)         # Convert to list
temp_list.append(40)             # Modify
coords = tuple(temp_list)        # Convert back: (10, 20, 30, 40)
```

### Other Conversions
```python
# Tuple to set (removes duplicates)
numbers = (1, 2, 2, 3, 3, 3)
unique_set = set(numbers)        # {1, 2, 3}

# Tuple to string
words = ("hello", "world", "python")
sentence = " ".join(words)       # "hello world python"

# String to tuple
text = "hello"
char_tuple = tuple(text)         # ('h', 'e', 'l', 'l', 'o')
```

## 🎯 Common Use Cases

### 1. Coordinates and Points
```python
# 2D point
point_2d = (10, 20)
x, y = point_2d

# 3D point
point_3d = (10, 20, 30)
x, y, z = point_3d

# RGB color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
```

### 2. Database Records
```python
# Student records
students = [
    ("Alice", 20, "Computer Science", 3.8),
    ("Bob", 19, "Mathematics", 3.6),
    ("Carol", 21, "Physics", 3.9)
]

# Process records
for name, age, major, gpa in students:
    print(f"{name} ({age}): {major} - GPA: {gpa}")
```

### 3. Dictionary Keys
```python
# Tuples as dictionary keys (hashable)
locations = {
    (0, 0): "Origin",
    (10, 20): "Point A",
    (30, 40): "Point B"
}

# Access using tuple key
origin = locations[(0, 0)]       # "Origin"

# This wouldn't work with lists (unhashable)
# locations = {[0, 0]: "Origin"}  # TypeError
```

### 4. Function Arguments
```python
def calculate_distance(point1, point2):
    """Calculate distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Using tuples as arguments
p1 = (0, 0)
p2 = (3, 4)
distance = calculate_distance(p1, p2)  # 5.0
```

### 5. Named Tuples (Advanced)
```python
from collections import namedtuple

# Create a named tuple class
Person = namedtuple('Person', ['name', 'age', 'city'])

# Create instances
alice = Person('Alice', 30, 'New York')
bob = Person('Bob', 25, 'San Francisco')

# Access by name or index
print(alice.name)       # 'Alice'
print(alice[0])         # 'Alice' (same as above)
print(alice.age)        # 30

# Still immutable like regular tuples
# alice.age = 31        # AttributeError
```

## ⚡ Performance Benefits

### Memory Efficiency
```python
import sys

# Tuples use less memory
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

print(f"List size: {sys.getsizeof(my_list)} bytes")
print(f"Tuple size: {sys.getsizeof(my_tuple)} bytes")
# Tuple is typically smaller
```

### Speed Comparison
```python
import timeit

# Tuple creation is faster
list_time = timeit.timeit(lambda: [1, 2, 3, 4, 5], number=1000000)
tuple_time = timeit.timeit(lambda: (1, 2, 3, 4, 5), number=1000000)

print(f"List creation: {list_time:.4f} seconds")
print(f"Tuple creation: {tuple_time:.4f} seconds")
# Tuple creation is typically faster
```

## 🎯 When to Use Tuples

### Use Tuples When:
- **Data shouldn't change**: Coordinates, database records, configuration
- **Returning multiple values**: Function returns
- **Dictionary keys**: Need hashable keys
- **Performance matters**: Memory and speed optimization
- **Data integrity**: Prevent accidental modification

### Examples:
```python
# Configuration settings (shouldn't change)
DATABASE_CONFIG = ("localhost", 5432, "mydb", "user")

# Function returning multiple values
def get_user_info():
    return "John", 25, "john@email.com"

# Dictionary with coordinate keys
chess_board = {(0, 0): "rook", (0, 1): "knight", (0, 2): "bishop"}
```

## 🏃‍♂️ Running the Examples

### Basic Tuple Operations
```bash
python tuple_operations.py
```
- Shows tuple creation and iteration
- Demonstrates immutability concept
- Simple iteration example

## 🎮 Practice Exercises

### Beginner
1. Create a tuple with your personal information (name, age, city)
2. Create a function that returns the first and last elements of a tuple
3. Write code to swap two variables using tuple unpacking
4. Create a tuple of RGB color values and unpack them

### Intermediate
1. Write a function that takes a list and returns a tuple of (min, max, average)
2. Create a dictionary with tuple keys representing coordinates
3. Implement a function that rotates a point around the origin using tuples
4. Build a simple address book using tuples for contact information

### Advanced
1. Implement a simple database using lists of tuples
2. Create a function that merges two sorted tuples into one sorted tuple
3. Build a basic statistics calculator that returns multiple values as a tuple
4. Implement a simple graph representation using tuples for edges

## 💡 Best Practices

### Do's ✅
- Use tuples for data that shouldn't change
- Use tuple unpacking for cleaner code
- Use tuples as dictionary keys when appropriate
- Return multiple values from functions using tuples
- Use named tuples for better readability

### Don'ts ❌
- Don't try to modify tuples (they're immutable)
- Don't use tuples when you need to frequently add/remove items
- Don't forget the comma for single-item tuples
- Don't use tuples when list methods are needed

## 🔄 Common Patterns

### Data Processing
```python
# Processing student data
students = [("Alice", 85), ("Bob", 92), ("Carol", 78)]

# Extract names and grades
names = [student[0] for student in students]
grades = [student[1] for student in students]

# Find top student
top_student = max(students, key=lambda x: x[1])  # ("Bob", 92)
```

### Coordinate Manipulation
```python
# Working with 2D points
points = [(0, 0), (1, 1), (2, 4), (3, 9)]

# Translate all points
translated = [(x + 5, y + 5) for x, y in points]

# Calculate distances from origin
distances = [(x**2 + y**2)**0.5 for x, y in points]
```

## 🧩 Integration with Other Data Types

### With Lists
```python
# List of tuples (common pattern)
employees = [
    ("Alice", "Engineer", 75000),
    ("Bob", "Designer", 65000),
    ("Carol", "Manager", 85000)
]

# Sort by salary
sorted_by_salary = sorted(employees, key=lambda x: x[2])
```

### With Dictionaries
```python
# Convert list of tuples to dictionary
pairs = [("a", 1), ("b", 2), ("c", 3)]
my_dict = dict(pairs)  # {"a": 1, "b": 2, "c": 3}

# Convert dictionary to list of tuples
my_dict = {"a": 1, "b": 2, "c": 3}
pairs = list(my_dict.items())  # [("a", 1), ("b", 2), ("c", 3)]
```

## 📚 Key Takeaways

- **Tuples are immutable** - they cannot be changed after creation
- **Use for fixed data** - coordinates, records, configuration
- **Memory efficient** - use less memory than lists
- **Hashable** - can be used as dictionary keys
- **Fast** - creation and access are faster than lists
- **Unpacking** - elegant way to work with multiple values
- **Return multiple values** - perfect for function returns

## 🔗 Next Steps

After mastering tuples, explore:
- **Lists** (`lists_README.md`) - Mutable sequences
- **Named Tuples** - Enhanced tuples with named fields
- **Dictionaries** (`../02_dictionaries/`) - Key-value mappings
- **Sets** - Unique element collections
- **Data Classes** - Modern alternative to named tuples

---

Happy coding with Python tuples! 🐍✨