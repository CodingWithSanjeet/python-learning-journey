temperature = 32
if temperature < 45:
    print("Wear a jacket")
elif temperature < 60:
    print("A t-shirt is fine")
else:
    print("It's warm - stay cool!")
    
participants = ["Bob","Rohit","Manish"]
if "Bob" in participants:
    print("Bob is registered for the event!")
else:
    print("Bob isn't registered.")
    
age = 213
toppings = ["mangose","olives", "tomatoes"]
if(toppings[0] != 'mangose'):
    print("No mangoes for toppings")
elif toppings[2] == "tomatoes":
    print("Tomatoes are there in toppings")
if age != 23:
    print("Not 23")
    
day = 'saturday'
fridge_contents = ['eggs', 'bacon']
if(day == 'saturday'):
    if("eggs" and "bacon" in fridge_contents):
        print("Time for a hearty breakfast!")
    else:
        print("Maybe just cereal today!")
else:
    print("Stick to the quick breakfase routine.")