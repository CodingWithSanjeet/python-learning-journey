full_name = {"Sanjeet": "Kumar", "Manish": "Prasad"}
# print(full_name)
person = {"name": "Sanjeet","age": 30, "city": "Bangalore"}
# print(person["name"]) #if the key not found then will throw error
# print(person.get("age")) #if the key not exist it will not throw error

# person["email"] ="sanjeet@google.com"
# person["is_employee"] =True
# person["age"]=32

# person.pop("age")
# person.popitem()
# del person["is_employee"]
# person.clear()
# print(person)


# for key in person:
#     print(key)

# for value in person.values():
#     print(value)
    
for key, value in person.items():
    print(f"{key} -> {value}")
    
family = {"mom":{"name": "Sita", "age": 57}, "dad": {"name": "Ram", "age": 54}}
for parent_type, parent_info in family.items():
    print(f"\nParent Type: {parent_type}\n")
    parent_name = f"Name: {parent_info["name"]}"
    parent_age = f"Age: {parent_info["age"]}"
    print(f"  {parent_name}")
    print(f"  {parent_age}")
    
    
speakers = {"Sanjeet Kumar":["GenAI", "FullStack Development"],"Nikhil Gupta":["Machine Learning","Backend Development"],"Maninsh Prasad":["Team Lead","Lang Chain"]}

for speaker_name, topics in speakers.items():
    print(f"{speaker_name} will talk: ")
    for topic in topics:
        print(f"-{topic}")
        