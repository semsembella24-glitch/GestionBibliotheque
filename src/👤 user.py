class User:
    def __init__(self, name):
        self._name = name
        self._borrowed_books = []

    @property
    def name(self):
        return self._name

    @property
    def borrowed_books(self):
        return self._borrowed_books.copy()

    def borrow_book(self, book):
        if book.borrow():
            self._borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self._borrowed_books:
            book.return_book()
            self._borrowed_books.remove(book)
            return True
        return False
