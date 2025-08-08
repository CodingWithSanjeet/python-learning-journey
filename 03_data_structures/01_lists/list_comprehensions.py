#!/usr/bin/env python3
"""
Python Lists - List Comprehensions
===================================

Comprehensive examples of list comprehensions from basic to advanced.
"""


def main():
    print("=" * 50)
    print("LIST COMPREHENSIONS - COMPLETE GUIDE")
    print("=" * 50)
    
    # 1. BASIC COMPREHENSIONS
    print("\n1. BASIC COMPREHENSIONS")
    print("-" * 25)
    
    # Basic syntax: [expression for item in iterable]
    squares = [x**2 for x in range(6)]
    print(f"Squares [x**2 for x in range(6)]: {squares}")
    
    # Traditional vs comprehension
    traditional = []
    for x in range(5):
        traditional.append(x * 2)
    comprehension = [x * 2 for x in range(5)]
    print(f"Traditional loop: {traditional}")
    print(f"Comprehension:    {comprehension}")
    
    # 2. WITH CONDITIONS
    print("\n2. WITH CONDITIONS")
    print("-" * 20)
    
    # Filter even numbers
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"Even numbers: {evens}")
    
    # Transform and filter
    words = ["hello", "world", "python", "programming", "code"]
    long_upper = [word.upper() for word in words if len(word) > 4]
    print(f"Long words uppercase: {long_upper}")
    
    # Multiple conditions
    numbers = range(20)
    special = [x for x in numbers if x % 2 == 0 and x > 5]
    print(f"Even and > 5: {special}")
    
    # 3. MULTIPLE LOOPS
    print("\n3. MULTIPLE LOOPS")
    print("-" * 18)
    
    # Cartesian product
    letters = 'abc'
    digits = '123'
    combinations = [letter + digit for letter in letters for digit in digits]
    print(f"Combinations: {combinations}")
    
    # With conditions
    filtered_combos = [x + y for x in 'abc' for y in '123' if x != 'a' and y != '1']
    print(f"Filtered combinations: {filtered_combos}")
    
    # 4. NESTED COMPREHENSIONS
    print("\n4. NESTED COMPREHENSIONS")
    print("-" * 26)
    
    # 2D matrix
    matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
    print("Multiplication table:")
    for row in matrix:
        print(f"  {row}")
    
    # Flatten nested list
    nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [item for sublist in nested for item in sublist]
    print(f"Nested: {nested}")
    print(f"Flattened: {flattened}")
    
    # 5. STRING OPERATIONS
    print("\n5. STRING OPERATIONS")
    print("-" * 21)
    
    # Extract first letters
    words = ["this", "is", "a", "list", "of", "words"]
    first_letters = [word[0] for word in words]
    print(f"First letters: {first_letters}")
    
    # Character filtering
    sentence = "Hello World!"
    vowels = [char for char in sentence if char.lower() in 'aeiou']
    consonants = [char for char in sentence if char.isalpha() and char.lower() not in 'aeiou']
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    
    # 6. MATHEMATICAL OPERATIONS
    print("\n6. MATHEMATICAL OPERATIONS")
    print("-" * 28)
    
    # Perfect squares under 100
    perfect_squares = [x**2 for x in range(1, 11) if x**2 < 100]
    print(f"Perfect squares < 100: {perfect_squares}")
    
    # Fibonacci-like sequence
    fib = [1, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(8)]
    print(f"Fibonacci-like: {fib}")
    
    # Prime numbers (simple check)
    primes = [x for x in range(2, 30) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
    print(f"Primes up to 30: {primes}")
    
    # 7. PRACTICAL EXAMPLES
    print("\n7. PRACTICAL EXAMPLES")
    print("-" * 22)
    
    # File extensions
    files = ["doc.txt", "image.jpg", "script.py", "data.csv", "readme.md"]
    python_files = [f for f in files if f.endswith('.py')]
    extensions = [f.split('.')[-1] for f in files]
    print(f"Python files: {python_files}")
    print(f"Extensions: {extensions}")
    
    # Grade processing
    grades = [85, 92, 78, 96, 73, 89, 94, 67]
    passing = [g for g in grades if g >= 70]
    curved = [min(g + 5, 100) for g in grades]
    letter_grades = ['A' if g >= 90 else 'B' if g >= 80 else 'C' if g >= 70 else 'F' for g in grades]
    print(f"Passing grades: {passing}")
    print(f"Curved grades: {curved}")
    print(f"Letter grades: {letter_grades}")
    
    # 8. PERFORMANCE COMPARISON
    print("\n8. PERFORMANCE COMPARISON")
    print("-" * 27)
    
    import time
    
    # Large list creation - traditional vs comprehension
    n = 100000
    
    # Traditional method
    start = time.time()
    traditional_large = []
    for i in range(n):
        if i % 2 == 0:
            traditional_large.append(i**2)
    traditional_time = time.time() - start
    
    # List comprehension
    start = time.time()
    comprehension_large = [i**2 for i in range(n) if i % 2 == 0]
    comprehension_time = time.time() - start
    
    print(f"Traditional time: {traditional_time:.4f}s")
    print(f"Comprehension time: {comprehension_time:.4f}s")
    print(f"Speedup: {traditional_time/comprehension_time:.2f}x faster")
    print(f"Both created {len(comprehension_large)} elements")
    
    print("\n" + "=" * 50)
    print("LIST COMPREHENSIONS COMPLETE!")
    print("=" * 50)
    print("\n🎯 Key Benefits:")
    print("- More concise and readable")
    print("- Generally faster than traditional loops")
    print("- More Pythonic style")
    print("- Can replace map() and filter() functions")
    print("- Powerful for data processing and transformation")


if __name__ == "__main__":
    main()