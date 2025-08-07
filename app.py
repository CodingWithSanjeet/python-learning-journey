import requests
from pathlib import Path

res = requests.get("https://www.python.org")

path = Path("index.html")
try:
    with open(path, "w") as f:
        f.write(res.text)
except FileNotFoundError:
    print("File not found")
finally:
    print("File written successfully")



