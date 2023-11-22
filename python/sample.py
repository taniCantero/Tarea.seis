
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def name_with_label(self):
        return f"name: {self.name}"

    def email_with_label(self):
        return f"email: {self.email}"

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def title_and_author(self):
        return f"{self.title} - {self.author}"

user = User(name="peter", email="peter@example.com")
print(
    user.name_with_label(),
    user.email_with_label()
)

book = Book("PythonBook", "Guido")
print(book.title_and_author())