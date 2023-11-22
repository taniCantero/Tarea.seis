class Book:
    def __init__(self, title):
        self.__title = title
    
    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title
        
    x = property(get_title, set_title)

book = Book("PythonBook")
print(book.x)
book.x = "RubyBook"
print(book.x)