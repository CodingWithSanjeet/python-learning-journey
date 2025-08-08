"""
List Creation Shortcuts and Reference Caveats

This script demonstrates the difference between creating lists with shortcuts
and the important caveat about references when working with nested lists.
"""

print("=" * 60)
print("LIST CREATION SHORTCUTS")
print("=" * 60)

# Basic list creation shortcuts
print("\n1. Basic List Creation Shortcuts:")
print("-" * 40)

list1 = [0] * 5
list2 = ["top"] * 4
print(f"List1 (zeros): {list1}")
print(f"List2 (strings): {list2}")

print("\n✅ This works fine for immutable objects like numbers and strings.")

print("\n" + "=" * 60)
print("THE REFERENCE CAVEAT - PROBLEMATIC APPROACH")
print("=" * 60)

print("\n2. Problem: Creating Nested Lists with Multiplication")
print("-" * 50)

# PROBLEMATIC: All sublists are the same object
listoflists = [[0] * 4] * 5
print(f"Initial nested list: {listoflists}")

print("\n🔍 Let's check if sublists are the same object:")
print(f"listoflists[0] is listoflists[1]: {listoflists[0] is listoflists[1]}")
print(f"ID of listoflists[0]: {id(listoflists[0])}")
print(f"ID of listoflists[1]: {id(listoflists[1])}")

print("\n⚠️ Modifying one element affects ALL sublists:")
listoflists[0][2] = 2
print(f"After changing listoflists[0][2] = 2: {listoflists}")

print("\n" + "=" * 60)
print("DEMONSTRATING WHY THIS HAPPENS")
print("=" * 60)

print("\n3. Understanding the Reference Issue:")
print("-" * 40)

# This shows why the problem occurs
innerlist = [0] * 4
listoflists1 = [innerlist] * 5
print(f"Original innerlist: {innerlist}")
print(f"List of lists: {listoflists1}")

print(f"\n🔍 All elements point to the same innerlist:")
print(f"listoflists1[0] is innerlist: {listoflists1[0] is innerlist}")
print(f"listoflists1[1] is innerlist: {listoflists1[1] is innerlist}")

print(f"\n⚠️ Changing the original innerlist affects everything:")
innerlist[2] = 1
print(f"After innerlist[2] = 1: {listoflists1}")

print("\n" + "=" * 60)
print("CORRECT SOLUTION - LIST COMPREHENSIONS")
print("=" * 60)

print("\n4. Solution: Use List Comprehensions")
print("-" * 40)

# CORRECT: Each sublist is a separate object
listoflistsupdated = [[0] * 4 for i in range(5)]
print(f"Initial nested list: {listoflistsupdated}")

print(f"\n🔍 Now each sublist is a different object:")
print(f"listoflistsupdated[0] is listoflistsupdated[1]: {listoflistsupdated[0] is listoflistsupdated[1]}")
print(f"ID of listoflistsupdated[0]: {id(listoflistsupdated[0])}")
print(f"ID of listoflistsupdated[1]: {id(listoflistsupdated[1])}")

print(f"\n✅ Modifying one sublist doesn't affect others:")
listoflistsupdated[0][2] = 2
print(f"After changing listoflistsupdated[0][2] = 2: {listoflistsupdated}")

print("\n" + "=" * 60)
print("ALTERNATIVE SOLUTIONS")
print("=" * 60)

print("\n5. Other Ways to Create Independent Nested Lists:")
print("-" * 50)

# Method 1: Using list() constructor in comprehension
method1 = [list([0] * 4) for _ in range(5)]
print(f"Method 1 (list constructor): {method1}")
method1[1][1] = 9
print(f"After modifying method1[1][1] = 9: {method1}")

# Method 2: Using nested loops
method2 = []
for i in range(5):
    method2.append([0] * 4)
print(f"\nMethod 2 (nested loops): {method2}")
method2[2][3] = 7
print(f"After modifying method2[2][3] = 7: {method2}")

# Method 3: Using copy.deepcopy (for more complex scenarios)
import copy
template = [[0] * 4]
method3 = [copy.deepcopy(template[0]) for _ in range(5)]
print(f"\nMethod 3 (deepcopy): {method3}")
method3[3][0] = 5
print(f"After modifying method3[3][0] = 5: {method3}")

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)

print("""
✅ DO: Use list comprehensions for nested lists
   correct = [[0] * 4 for _ in range(5)]

❌ DON'T: Use multiplication for nested lists  
   incorrect = [[0] * 4] * 5

🔍 REMEMBER: 
   - Multiplication creates references to the same object
   - List comprehensions create new objects each time
   - Use 'is' operator to check if objects are the same
   - Use id() function to see object memory addresses
""")

print("=" * 60)
print("END OF DEMONSTRATION")
print("=" * 60)