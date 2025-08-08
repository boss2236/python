
class Book:
    def __init__(self, title, author, year=None):
        self.title = title
        self.author = author
        self.year = year

    def get_description(self):
        if self.year is not None:
            return f"{self.title} by {self.author} ({self.year})"
        else:
            return f"{self.title} by {self.author}"

    def is_long_book(self, word_limit):
        title_words = self.title.split()
        num_words = len(title_words)
        return num_words > word_limit


book1 = Book(input("Enter book title: "), input("Enter book author: "), input("Enter book year (optional, press Enter to skip): ") or None)
print(book1.get_description()) # Expected: "The Hitchhiker's Guide to the Galaxy by Douglas Adams"
print(book1.is_long_book(5))  # Expected: True (Title has 6 words)
print(book1.is_long_book(1)) # Expected: False

book2 = Book("Dune", "Frank Herbert")
print(book2.get_description()) # Expected: "Dune by Frank Herbert"
print(book2.is_long_book(3))  # Expected: False (Title has 1 word)
