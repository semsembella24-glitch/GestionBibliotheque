from library import Library
from book import Book
from user import User

if __name__ == "__main__":
    library = Library()

    # Adding books to the library
    book1 = Book("A Short History of Nearly Everything", "Bill Bryson")
    book2 = Book("The Selfish Gene", "Richard Dawkins")
    book3 = Book("Cosmos", "Carl Sagan")
    book4 = Book("The Disappearing Spoon", "Sam Kean")

    for book in [book1, book2, book3, book4]:
        library.add_book(book)

    # Registering users
    mouna = User("Mouna")
    wissam = User("Wissam")
    library.register_user(mouna)
    library.register_user(wissam)

    # Borrowing books
    loan1 = library.borrow_book(wissam, book1)
    loan2 = library.borrow_book(mouna, book3)

    # Display library status
    library.display_status()

    # Returning a book
    library.return_book(loan1)
    print("\nAfter returning a book:")
    library.display_status()
