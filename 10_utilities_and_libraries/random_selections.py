# from random import randint
from random import choice

fruits = ["Apple", "Pine Apple","Papaya","Grapes","Guava","Mango"]

def random_fruit(fruits):
    # random_index = randint(a=0, b=len(fruits)-1)
    # picked_fruit = fruits[random_index]
    if not fruits:
        return print("Fruit list is empty.")
    picked_fruit = choice(fruits)
    print(f"You picked: {picked_fruit}")
    
random_fruit(fruits=fruits)