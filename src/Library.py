from book import Book
from user import User
from loan import Loan

class Library:
    def __init__(self):
        self._books = []
        self._users = []
        self._loans = []

    def add_book(self, book: Book):
        self._books.append(book)

    def remove_book(self, book: Book):
        self._books.remove(book)

    def register_user(self, user: User):
        self._users.append(user)

    def borrow_book(self, book: Book, user: User):
        if book.available:
            book.borrow()
            loan = Loan(book, user)
            self._loans.append(loan)

    def return_book(self, book: Book):
        for loan in self._loans:
            if loan.book == book and loan.active:
                loan.close()

    def display_status(self):
        print("Books:")
        for book in self._books:
            print(f"{book.title} - Available: {book.available}")

        print("\nActive Loans:")
        for loan in self._loans:
            if loan.active:
                print(f"{loan.book.title} borrowed by {loan.user.name}")


