from pathlib import Path

path = Path("examples.txt")
try:
    content = path.read_text()
    print(content)
except FileNotFoundError as e:
    print(f"File Not Found: {e}")
# Using 'with' ensures the file is properly closed after reading
with Path.open("example.txt","r",encoding="utf-8") as file:
    content =file.read()
    print(content)