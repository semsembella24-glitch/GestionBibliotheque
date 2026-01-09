
class Loan:
    def __init__(self, book, user):
        self._book = book
        self._user = user
        self._active = True

    @property
    def book(self):
        return self._book

    @property
    def user(self):
        return self._user

    @property
    def active(self):
        return self._active

    def close(self):
        self._active = False
        self._book.return_book()

