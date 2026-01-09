from datetime import datetime

class Loan:
    def __init__(self, user, book):
        self._user = user
        self._book = book
        self._date = datetime.now()
        self._active = True

    @property
    def user(self):
        return self._user

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def active(self):
        return self._active

    def close(self):
        if self._active:
            self._book.return_book()
            self._active = False


