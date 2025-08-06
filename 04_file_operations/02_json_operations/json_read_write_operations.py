import json
from pathlib import Path

names = ["Sanjeet","Nikhil", "Manish", "Sujeet"]
# with Path.open("names.json","w") as file:
#     contents = json.dumps(names)
#     file.write(contents)
    
with Path.open("names.json","r") as file:
    content = file.read()
    contents = json.loads(content)
    print(contents[0])