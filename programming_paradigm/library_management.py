class Book:
    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author
        self._is_checked_out = False
    def return_book(self):
        pass
        
    
        
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

