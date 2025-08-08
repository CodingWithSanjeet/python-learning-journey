"""
Python Lists - Basic Operations
================================

This file demonstrates basic list operations including:
- Adding elements (append, insert, extend)
- Removing elements (remove, pop, del, clear)
- List properties and membership testing
- Traditional loops vs list comprehensions

Based on: Lists README.md - Part 2: Basic Operations
"""


def demonstrate_adding_elements():
    """Demonstrates various ways to add elements to lists."""
    print("➕ ADDING ELEMENTS")
    print("=" * 20)
    
    shopping_cart = ["apple", "banana"]
    print(f"Initial shopping cart: {shopping_cart}")

    print("\n1. Adding Single Elements:")
    print("-" * 27)
    
    # Add single element to end
    shopping_cart.append("orange")
    print(f"After append('orange'): {shopping_cart}")

    # Insert at specific position
    shopping_cart.insert(1, "kiwi")
    print(f"After insert(1, 'kiwi'): {shopping_cart}")
    
    print("\n2. Adding Multiple Elements:")
    print("-" * 29)

    # Add multiple elements
    shopping_cart.extend(["mango", "pear"])
    print(f"After extend(['mango', 'pear']): {shopping_cart}")

    # Using + operator (creates new list)
    all_fruits = shopping_cart + ["grape", "cherry"]
    print(f"Using + operator (new list): {all_fruits}")
    print(f"Original cart unchanged: {shopping_cart}")


def demonstrate_combining_lists():
    """Demonstrates different ways to combine lists."""
    print("\n🔗 COMBINING LISTS")
    print("=" * 20)
    
    list1 = [1, 2]
    list2 = [3, 4]
    print(f"List 1: {list1}")
    print(f"List 2: {list2}")

    # Method 1: Addition operator (creates new list)
    combined_list = list1 + list2
    print(f"\nMethod 1 - Addition (+): {combined_list}")
    print(f"Original list1: {list1} (unchanged)")

    # Method 2: extend (modifies original list)
    list1_copy = [1, 2]  # Make a copy for demonstration
    list1_copy.extend(list2)
    print(f"Method 2 - extend(): {list1_copy}")
    print("Note: extend() modifies the original list")

    # Method 3: append (adds list as single element)
    list_a = [1, 2]
    list_a.append([3, 4])
    print(f"Method 3 - append(list): {list_a}")
    print("Note: append() adds the entire list as ONE element!")


def demonstrate_removing_elements():
    """Demonstrates various ways to remove elements from lists."""
    print("\n➖ REMOVING ELEMENTS")
    print("=" * 22)
    
    task_list = ["email", "meeting", "lunch", "email"]
    print(f"Initial task list: {task_list}")

    print("\n1. Remove by Value:")
    print("-" * 18)
    
    # Remove first occurrence of value
    task_list.remove("email")
    print(f"After remove('email'): {task_list}")
    print("Note: remove() only removes the FIRST occurrence")

    print("\n2. Remove by Index:")
    print("-" * 17)
    
    # Remove and return element by index
    last_task = task_list.pop()
    print(f"Popped last item: '{last_task}'")
    print(f"List after pop(): {task_list}")
    
    first_task = task_list.pop(0)
    print(f"Popped first item: '{first_task}'")
    print(f"List after pop(0): {task_list}")

    # Delete by index (alternative to pop)
    task_list_copy = ["email", "meeting", "lunch"]
    print(f"\nDemo list for del: {task_list_copy}")
    del task_list_copy[0]
    print(f"After del task_list[0]: {task_list_copy}")

    print("\n3. Clear All Elements:")
    print("-" * 22)
    
    # Clear all elements
    demo_list1 = ["a", "b", "c"]
    demo_list2 = ["x", "y", "z"]
    
    print(f"Before clear() - demo1: {demo_list1}")
    demo_list1.clear()
    print(f"After clear(): {demo_list1}")
    
    print(f"Before del [:] - demo2: {demo_list2}")
    del demo_list2[:]
    print(f"After del [:]: {demo_list2}")


def demonstrate_list_properties():
    """Demonstrates list properties and membership testing."""
    print("\n📊 LIST PROPERTIES & TESTING")
    print("=" * 32)
    
    student_names = ["Alice", "Bob", "Charlie", "Diana"]
    print(f"Student names: {student_names}")

    print("\n1. Length and Attributes:")
    print("-" * 24)
    
    # Get length of list
    class_size = len(student_names)
    print(f"Class size: {class_size}")

    # Check if list is empty
    is_empty = len(student_names) == 0
    print(f"Is list empty: {is_empty}")
    
    # Empty list check
    empty_list = []
    is_empty_check = len(empty_list) == 0
    print(f"Empty list check: {is_empty_check}")

    print("\n2. Membership Testing:")
    print("-" * 21)
    
    available_fruits = ["apple", "banana", "orange"]
    print(f"Available fruits: {available_fruits}")

    # Check if item exists
    is_apple_available = "apple" in available_fruits
    has_no_grapes = "grape" not in available_fruits
    print(f"Is apple available: {is_apple_available}")
    print(f"No grapes available: {has_no_grapes}")

    print("\n3. Advanced Membership Testing:")
    print("-" * 32)
    
    # Check if all/any elements meet condition
    even_numbers = [2, 4, 6, 8]
    print(f"Even numbers: {even_numbers}")
    
    all_are_even = all(num % 2 == 0 for num in even_numbers)
    has_large_number = any(num > 5 for num in even_numbers)
    print(f"All are even: {all_are_even}")
    print(f"Has number > 5: {has_large_number}")


def demonstrate_traditional_vs_comprehensions():
    """Compares traditional loops with list comprehensions."""
    print("\n🔄 TRADITIONAL LOOPS vs LIST COMPREHENSIONS")
    print("=" * 50)
    
    print("Example: Creating squares of numbers 0-9")
    print("-" * 38)
    
    # Traditional approach
    print("1. Traditional Loop:")
    list_sqrs = []
    for value in range(0, 10):
        list_sqrs.append(value ** 2)
    print(f"Traditional result: {list_sqrs}")
    
    # List comprehension approach
    print("\n2. List Comprehension:")
    ls_sqrs = [value**2 for value in range(1, 11)]
    print(f"Comprehension result: {ls_sqrs}")
    
    print("\n3. Performance and Readability:")
    print("-" * 32)
    print("✅ List comprehensions are:")
    print("  - More concise and readable")
    print("  - Generally faster")
    print("  - More Pythonic")
    print("✅ Traditional loops are better when:")
    print("  - Logic is complex")
    print("  - You need debugging breakpoints")
    print("  - Multiple operations per iteration")


def main():
    """Main function to run all demonstrations."""
    print("=" * 60)
    print("PYTHON LISTS - BASIC OPERATIONS")
    print("=" * 60)
    
    demonstrate_adding_elements()
    demonstrate_combining_lists()
    demonstrate_removing_elements()
    demonstrate_list_properties()
    demonstrate_traditional_vs_comprehensions()
    
    print("\n" + "=" * 60)
    print("BASIC OPERATIONS DEMONSTRATION COMPLETE!")
    print("=" * 60)
    print("\n🎯 Key Operations Covered:")
    print("- Adding elements: append(), insert(), extend(), +")
    print("- Combining lists: different methods and their effects")
    print("- Removing elements: remove(), pop(), del, clear()")
    print("- List properties: len(), empty checks")
    print("- Membership testing: in, not in, all(), any()")
    print("- Traditional loops vs. list comprehensions")


if __name__ == "__main__":
    main()