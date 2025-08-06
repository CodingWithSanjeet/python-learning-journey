import json
from pathlib import Path

FILE_NAME = 'countries.json'
def save_to_json(data, file_name = FILE_NAME):
    """Save the list of places to a json file """
    with Path.open(file_name,"w") as f:
        json.dump(data, f)
    
def read_from_json(file_name=FILE_NAME):
    try:
        with Path.open(file_name, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return empty list if file doesn't exist
        
def main():
    countries = []
    print("Enter country names. Type 'quit' to finish")
    while True:
        country = input("Enter Country Name:")
        if country.lower() == "quit":
            break
        countries.append(country)
    save_to_json(countries)
    saved_countries = read_from_json()
    print("\nYou've added the following countries: ")
    for country in saved_countries:
        print(f"> {country}")
        
"""
This block checks if the script is being run directly (not imported as a module).
If so, it calls the main() function to start the program.

__name__ is a special built-in variable in Python.
When you run a Python file directly (for example, python json_country_to_visit.py), Python sets __name__ to "__main__" in that file.
If the file is imported as a module in another script, __name__ will be set to the module's name (e.g., "json_country_to_visit"), not "__main__".
"""   
if __name__ == "__main__":
    main()