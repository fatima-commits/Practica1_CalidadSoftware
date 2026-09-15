from typeBook import Book

class BookRepository:
    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def get_all_books(self) -> list[Book]:
        return self.books