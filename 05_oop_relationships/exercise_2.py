# Association:
class Book:
    def __init__(self, name):
        self.name = name
        
class Reader:
    
    def __init__(self, name):
        self.name =  name
        
    def read_book(self, book):
        self.book = book.name
        print(f"{self.name} is reading {self.book}")
        
b1 = Book("DSA")        
r1 = Reader("Alice")
r1.read_book(b1)
