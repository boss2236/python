class ShoppingList:  # Define a class to represent a shopping list
    def __init__(self, items=None):  # This function runs when we create a new ShoppingList
        if items is None:  # If no items are given, use an empty list
            items = []
        self.items = items  # Store the list of items in the object

    def add_item(self, item):  # Define a function to add an item to the shopping list
        self.items.append(item)  # Add the given item to the list

    def remove_item(self, item):  # Define a function to remove an item from the shopping list
        if item in self.items:  # Check if the item is in the list
            self.items.remove(item)  # If it is, remove it
        else:
            print(f"Item '{item}' not found in the list.")  # If not, print a message

    def get_total_items(self):  # Define a function to count how many items are in the list
        return len(self.items)  # Return the number of items in the list

class BookCollection(ShoppingList):  # Define a class for a collection of books, based on ShoppingList
    def __init__(self, books=None):  # This function runs when we create a new BookCollection
        if books is None:  # If no books are given, use an empty list
            books = []
        super().__init__(books)  # Call the parent class (ShoppingList) constructor with the books list

    def add_book(self, book):  # Define a function to add a book to the collection
        self.add_item(book)  # Use the add_item method from ShoppingList

    def remove_book(self, book):  # Define a function to remove a book from the collection
        self.remove_item(book)  # Use the remove_item method from ShoppingList

    def get_total_books(self):  # Define a function to count how many books are in the collection
        return self.get_total_items()  # Use the get_total_items method from ShoppingList
    def find_books_by_author(self, author):  # Define a function to find books by a specific author
        author = author.lower()  # Normalize the author's name to lowercase for case-insensitive comparison
        return [book for book in self.items if author in book.lower()]  # Return a list of books that contain the author's name

# Now, implement your BookCollection class
collection = BookCollection()
collection.add_item("The Hitchhiker's Guide to the Galaxy by Douglas Adams")
collection.add_item("Dune by Frank Herbert")
collection.add_item("The Restaurant at the End of the Universe by Douglas Adams")
collection.add_item("Foundation by Isaac Asimov")

print(f"Total books in collection: {collection.get_total_items()}")
# Expected output: Total books in collection: 4

douglas_adams_books = collection.find_books_by_author("Douglas Adams")
print(f"Books by Douglas Adams: {douglas_adams_books}")
# Expected output: Books by Douglas Adams: ["The Hitchhiker's Guide to the Galaxy by Douglas Adams", "The Restaurant at the End of the Universe by Douglas Adams"]

frank_herbert_books = collection.find_books_by_author("frank herbert") # Test case-insensitivity
print(f"Books by Frank Herbert: {frank_herbert_books}")
# Expected output: Books by Frank Herbert: ['Dune by Frank Herbert']

non_existent_author_books = collection.find_books_by_author("J.K. Rowling")
print(f"Books by J.K. Rowling: {non_existent_author_books}")
# Expected output: Books by J.K. Rowling: []