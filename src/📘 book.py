class Book:
    def __init__(self, title, author):
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
        if self._available:
            self._available = False
            return True
        return False

    def return_book(self):
        self._available = True

    def __str__(self):
        status = "Available" if self._available else "Borrowed"
        return f"{self._title} by {self._author} - {status}"
