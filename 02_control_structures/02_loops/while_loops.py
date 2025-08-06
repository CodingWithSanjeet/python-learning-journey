prompt = "\nEnter 'quit' to exit the program."
prompt += "\nEnter your command:"

while True:
    command = input(prompt)
    if command == 'quit':
        break
    else:
        print(f"\nYou entered: {command}")
