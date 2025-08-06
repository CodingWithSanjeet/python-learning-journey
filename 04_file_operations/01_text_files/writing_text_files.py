from pathlib import Path

content = "Hey, there\n"
content += "Welcome to the world of Python 🐍\n"
content += "It's so exciting to learn ❤️\n"
content += "Good Luck 👍"
# path = Path("example.txt")
# path.write_text(content, encoding="utf-8")
"""
Opens 'example.txt' in write mode using a context manager to ensure the file is properly closed after writing the multi-line welcome message with UTF-8 encoding.
"""
with Path.open("example.txt", "w",encoding="utf-8") as file: 
    file.write(content)
    print(f"content has been updated succfully")