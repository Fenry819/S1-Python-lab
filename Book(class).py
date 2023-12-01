class Publisher:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Publisher name:", self.name)

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author

    def display(self):
        super().display()
        print("Title:", self.title)
        print("Author:", self.author)

class Python(Book):
    def __init__(self, name, title, author, price, pages):
        super().__init__(name, title, author)
        self.price = price
        self.pages = pages

    def display(self):
        super().display()
        print("Price of book:", self.price)
        print("Number of pages:", self.pages)


python_book = Python("O'Reilly", "Learning Python", "Mark Lutz", 39.99, 1648)

python_book.display()
