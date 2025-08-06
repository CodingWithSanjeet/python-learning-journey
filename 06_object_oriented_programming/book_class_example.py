class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.num_pages = 230
        
    def get_num_pages(self):
        print(f"The {self.title} has {self.num_pages} page")
        
    def update_num_page(self, new_pages):
        self.num_pages = new_pages
        print(f"{self.title}'s page updated to {self.num_pages}")
        
    def read_book(self):
        print(f"Reading (a physical book) {self.title} by {self.author}")
        
    def describe_book(self):
        print(f"{self.title} by {self.author}, genre: {self.genre}")
        
    def __str__(self):
        return f"Book Object:\n\tTitle: {self.title}\n\tAuthor:{self.author}"
    
    
class Ebook(Book):
    def __init__(self, title, author, genre,file_size, file_type):
        super().__init__(title, author, genre)
        self.file_size = file_size
        self.file_type = file_type
        
    def download_books(self):
        print(f"Downloading '{self.title}' in {self.file_type} format ({self.file_size}MB)")
        
    def describe_book(self):
        super().describe_book()
        print(f"File Size: {self.file_size}Mb, Format: {self.file_type}")
        
    def read_book(self):
        print(f"Reading {self.title} on an e-reader device...")
        
# book = Book(title="The Kite Runner", author="Sanjeet", genre="fiction")
# book.get_num_pages()
# book.read_book()
# book.describe_book()
# book.update_num_page(new_pages=12)

# ebook = Ebook(title="Half Girlfriend", author="Chetan Bhagat", genre="Love", file_size=10, file_type="Pdf")
# ebook.download_books()
# ebook.describe_book()
# ebook.read_book()