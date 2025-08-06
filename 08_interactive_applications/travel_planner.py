print("Let's plan your dream travel itinerary ✈️")
print("\nEnter 'done' when you're finished")
dream_destinations = {}
while True:
    dream_place = input("\nWhich place would you like to visit?")
    if dream_place.lower() == 'done':
        break
    note = input("Anything specific you'd like to see in {dream_place}? (press enter to skip)")
    dream_destinations[dream_place]=note if note else 'Nothing special!'
    print("Got it! Let's keep going or type 'done' to finish!")
    
print("\nYour Dream Travel Itinerary:")
for place, note in dream_destinations.items():
    print(f"- {place} : {note}")
    
print("\nLooks like an exciting adventure awaits! Safe Travels.")
    