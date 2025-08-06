fruits = ["apple",2, "banana", "cherry"]
print(fruits[0])
print(fruits)
fruits[0] = "mango"
fruits.append("Mango")
fruits.remove("cherry")
fruits.pop()
fruits.pop(0)
print(fruits[1])
print(fruits)
message = f"Hello my name is Sanjeet and I like {fruits[2].title()} "
print(message)

# ----------------------------------------------------------
fruits = ["apple","mango","grapes", "banana", "cherry"]
ages = [32, 43, 54, 24]
print(f"Before sorting: {ages}")
ages.sort()
fruits.sort()
print(f"Sorted: {ages}")
print(f"sorted fruits: {fruits}")
fruits.reverse()
print(f"Reversed sorted fruits: {fruits}")
print(f"Length of list: {len(fruits)}")


# ---------------------------------------------------------------
# LOOPS

fruits = ["Apple","Cherry", "Mango","Pineapple", "Guava"]
for fruit in  fruits:
    print(fruit)