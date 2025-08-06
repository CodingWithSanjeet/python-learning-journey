# import arithmetic
# num1=3
# num2=4
# result = arithmetic.add(num1,num2)
# result_two= arithmetic.sub(num1,num2)
# print(f"Sum of {num1} + {num2} : {result}\nSubtraction of {num1} - {num2} is: {result_two}")

# from arithmetic import add, mul
# num1 =5
# num2 =10
# print(f"Sum of {num1} and {num2}: {add(num1, num2)}\nMultiplication of {num1} and {num2} is: {mul(num1, num2)}")

# import arithmetic as Math

# add_result = Math.add(4, 3)
# sub_result = Math.sub(43,23)
# print(f"Sum: {add_result}, Sub: {sub_result}")

# -----------------------------------------------------------
# import book_generator
# from book_generator import *
# from book_generator import Book as book
# from book_generator import Book, Ebook

# book = Book(title="Half Girlfriend",author="Chetan Bhagat",genre="Love")
# ebook = Ebook(title="Table No 118",author="Chetan Bhagat", genre="Crime", file_size=80, file_type="PDF")
# print(book)
# ebook.describe_book()
# -------------------------------------------------
from pathlib import Path
content = "Hey, there\n"
content += "Welcome to the world of Python\n"
content += "Python ❤️"
def readfile(file_name):
    path = Path(file_name)
    if not path.exists():
        return []
    return path.read_text(encoding='utf-8')

def write_to_file(filename, content):
    path = Path(filename)
    return path.write_text(content, encoding="utf-8")

# print(readfile("example.txt"))
# write_to_file("command.txt",content=content)
# contents = path.read_text()
# print(contents)

# Using 'with' ensures the file is properly closed after reading
# with Path.open("command.txt", "r", encoding="utf-8") as file:
#     contents = file.read()
#     print(contents)
    
with Path.open("command.txt","w",encoding="utf-8") as file:
    content = input("Please enter your text: ")
    file.write(content)
    print("Content has been updated successfully!")
    