class Book:
    __slots__ = ['title', 'author']
    def __init__(self, title, author):
        self.title = title
        self.author = author



book = Book("PythonBook", "Guido")
book.price = 300
print(book.price)