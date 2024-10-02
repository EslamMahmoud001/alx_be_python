class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self._is_checked_out = False
    
        
class Library:
    
    def __init__(self):
        self.__books = []
        
    def add_book(self, book : Book):
        self.new_book = book
        self.__books.append(self.new_book)

    def check_out_book(self, title):
        for book in self.__books:
            if title in book.title:
                book._is_checked_out = True
            
    def return_book(self, title):
        for book in self.__books:
            if title in book.title:
                if book._is_checked_out == True:
                    book._is_checked_out = False
            
    def list_available_books(self):
        for book in self.__books:
            if book._is_checked_out == False:
                print(f"{book.title} by {book.author}")
        
        
library = Library()
library.add_book(Book("Brave New World", "Aldous Huxley"))
library.add_book(Book("1984", "George Orwell"))

# Initial list of available books
print("Available books after setup:")
library.list_available_books()

# Simulate checking out a book
library.check_out_book("1984")
print("\nAvailable books after checking out '1984':")
library.list_available_books()

# Simulate returning a book
library.return_book("1984")
print("\nAvailable books after returning '1984':")
library.list_available_books()