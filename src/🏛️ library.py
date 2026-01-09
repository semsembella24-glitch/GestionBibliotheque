from book import Book
from user import User
from loan import Loan

class Library:
    def __init__(self):
        self._books = []
        self._users = []
        self._active_loans = []

    @property
    def books(self):
        return self._books.copy()

    @property
    def users(self):
        return self._users.copy()

    @property
    def active_loans(self):
        return self._active_loans.copy()

    def add_book(self, book):
        self._books.append(book)

    def register_user(self, user):
        self._users.append(user)

    def borrow_book(self, user, book):
        if user.borrow_book(book):
            loan = Loan(user, book)
            self._active_loans.append(loan)
            return loan
        return None

    def return_book(self, loan):
        if loan in self._active_loans:
            loan.close()
            self._active_loans.remove(loan)

    def display_status(self):
        print("📚 Books:")
        for book in self._books:
            print(book)

        print("\n📄 Active loans:")
        for loan in self._active_loans:
            print(f"{loan.book.title} borrowed by {loan.user.name}")
