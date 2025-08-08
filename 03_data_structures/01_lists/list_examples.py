#!/usr/bin/env python3
"""
Python Lists - Essential Examples
==================================

Complete collection of list examples covering all major operations.
Consolidates all concepts from the README into practical examples.
"""


def main():
    print("=" * 50)
    print("PYTHON LISTS - ESSENTIAL EXAMPLES")
    print("=" * 50)
    
    # 1. CREATION & BASICS
    print("\n1. LIST CREATION & BASICS")
    print("-" * 30)
    
    # Different ways to create lists
    empty_list = []
    fruits = ["apple", "banana", "orange"]
    mixed_data = [1, "hello", True, 3.14]
    numbers = list(range(5))  # [0, 1, 2, 3, 4]
    chars = list("hello")     # ['h', 'e', 'l', 'l', 'o']
    
    print(f"Empty list: {empty_list}")
    print(f"Fruits: {fruits}")
    print(f"Mixed data: {mixed_data}")
    print(f"From range: {numbers}")
    print(f"From string: {chars}")
    
    # 2. ADDING & REMOVING
    print("\n2. ADDING & REMOVING ELEMENTS")
    print("-" * 35)
    
    shopping_cart = ["milk"]
    shopping_cart.append("bread")           # Add single item
    shopping_cart.extend(["eggs", "cheese"]) # Add multiple items
    shopping_cart.insert(0, "butter")       # Insert at position
    print(f"After adding: {shopping_cart}")
    
    shopping_cart.remove("milk")            # Remove by value
    last_item = shopping_cart.pop()         # Remove last (returns item)
    print(f"After removing: {shopping_cart}")
    print(f"Popped item: {last_item}")
    
    # 3. ACCESSING & SLICING
    print("\n3. ACCESSING & SLICING")
    print("-" * 25)
    
    data = [10, 20, 30, 40, 50]
    print(f"Original: {data}")
    print(f"First item [0]: {data[0]}")
    print(f"Last item [-1]: {data[-1]}")
    print(f"Middle slice [1:4]: {data[1:4]}")
    print(f"Every second [::2]: {data[::2]}")
    print(f"Reversed [::-1]: {data[::-1]}")
    
    # 4. LIST COMPREHENSIONS
    print("\n4. LIST COMPREHENSIONS")
    print("-" * 25)
    
    # Basic comprehension
    squares = [x**2 for x in range(6)]
    print(f"Squares: {squares}")
    
    # With condition
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Even numbers: {evens}")
    
    # Transform strings
    words = ["hello", "world", "python"]
    uppercase = [word.upper() for word in words if len(word) > 4]
    print(f"Long words uppercase: {uppercase}")
    
    # 5. METHODS & OPERATIONS
    print("\n5. METHODS & OPERATIONS")
    print("-" * 25)
    
    test_scores = [85, 92, 78, 92, 89]
    print(f"Test scores: {test_scores}")
    print(f"Length: {len(test_scores)}")
    print(f"Max: {max(test_scores)}")
    print(f"Min: {min(test_scores)}")
    print(f"Sum: {sum(test_scores)}")
    print(f"Average: {sum(test_scores)/len(test_scores):.1f}")
    print(f"Count of 92: {test_scores.count(92)}")
    print(f"Index of 78: {test_scores.index(78)}")
    
    # Sorting
    sorted_scores = sorted(test_scores)  # New list
    print(f"Sorted (new): {sorted_scores}")
    test_scores.sort(reverse=True)       # In-place
    print(f"Sorted in-place (desc): {test_scores}")
    
    # 6. MEMBERSHIP & COMPARISON
    print("\n6. MEMBERSHIP & COMPARISON")
    print("-" * 30)
    
    colors = ["red", "blue", "green"]
    print(f"Colors: {colors}")
    print(f"'red' in colors: {'red' in colors}")
    print(f"'yellow' not in colors: {'yellow' not in colors}")
    
    # List comparison
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [1, 3, 2]
    print(f"[1,2,3] == [1,2,3]: {list1 == list2}")
    print(f"[1,2,3] == [1,3,2]: {list1 == list3}")
    print(f"[1,2] < [2,1]: {[1,2] < [2,1]}")
    
    # 7. COPYING & REFERENCES
    print("\n7. COPYING & REFERENCES")
    print("-" * 25)
    
    original = ["a", "b", "c"]
    shallow_copy = original[:]           # Shallow copy
    reference = original                 # Just a reference
    
    print(f"Original: {original}")
    original.append("d")
    print(f"After append to original:")
    print(f"  Original: {original}")
    print(f"  Shallow copy: {shallow_copy}")
    print(f"  Reference: {reference}")
    
    # 8. NESTED LISTS & CAVEAT
    print("\n8. NESTED LISTS - REFERENCE CAVEAT")
    print("-" * 35)
    
    # WRONG way - all rows share same reference
    wrong_matrix = [[0] * 3] * 3
    print(f"Wrong matrix: {wrong_matrix}")
    wrong_matrix[0][0] = 1
    print(f"After [0][0] = 1: {wrong_matrix}")
    print("❌ All rows changed!")
    
    # RIGHT way - each row is independent
    right_matrix = [[0] * 3 for _ in range(3)]
    print(f"Right matrix: {right_matrix}")
    right_matrix[0][0] = 1
    print(f"After [0][0] = 1: {right_matrix}")
    print("✅ Only intended row changed!")
    
    # 9. PRACTICAL PATTERNS
    print("\n9. PRACTICAL PATTERNS")
    print("-" * 20)
    
    # Remove duplicates while preserving order
    with_dupes = [1, 2, 2, 3, 1, 4, 3]
    no_dupes = []
    for item in with_dupes:
        if item not in no_dupes:
            no_dupes.append(item)
    print(f"Remove dupes: {with_dupes} → {no_dupes}")
    
    # Enumerate for index + value
    items = ["apple", "banana", "cherry"]
    print("Enumerate example:")
    for i, item in enumerate(items):
        print(f"  {i}: {item}")
    
    # Zip multiple lists
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["NYC", "LA", "Chicago"]
    print("Zip example:")
    for name, age, city in zip(names, ages, cities):
        print(f"  {name}, {age}, {city}")
    
    # List as stack (LIFO)
    stack = []
    stack.append("first")
    stack.append("second")
    stack.append("third")
    print(f"Stack: {stack}")
    last_out = stack.pop()
    print(f"Popped: {last_out}, Stack: {stack}")
    
    print("\n" + "=" * 50)
    print("All essential list concepts demonstrated!")
    print("=" * 50)


if __name__ == "__main__":
    main()