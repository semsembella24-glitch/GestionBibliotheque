class Book:
    def __init__(self, title: str, author: str):
        self._title = title
        self._author = author
        self._available = True

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def available(self):
        return self._available

    def borrow(self):
        self._available = False

    def return_book(self):
        self._available = True
