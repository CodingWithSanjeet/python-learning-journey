def greet(name, age):
    print(f"Hello, {name} you're {age} years old!")
# greet("Sanjeet",43)
# greet(age=43,name="Sanjeet")
    
def car_details(car_type="truck",car_name="bmw"):
    print(f"I have {car_type} named {car_name}")

# car_details(car_name="Ford",car_type="Car")

def format_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# print(format_name("sanjeet","kumar"))

def multiply(a, b):
    """Calculate the multiplication of a, and b

    Args:
        a (int): First integer number
        b (int): Second integer number

    Returns:
        int: Multiplication of 'a' and 'b'
    """
    return a * b

# print(multiply(5, 6))

plants = ["Lemon Tree", "Mango Tree", "Apple Tree"]

def water_plants(plants):
    for plant in plants:
        action = f"Watering the {plant}"
        print(action)
        
# water_plants(plants=plants)

def sum_numbers(*args):
    return sum(args)

# print(f"Sum of numbers: {sum_numbers(1,2,4,5,3)}")


# **(double asteriks) before the parameter cause Python to create a dictionary
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

print(build_profile("Sanjeet",last="Kumar",location="Bangalore",age=32))
    