"""Módulo de persistencia y gestión de la colección de libros."""

from typeBook import Book


class BookRepository:
    """Clase para administrar la colección de libros leídos."""

    def __init__(self) -> None:
        """Inicializa la lista de libros."""
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        """Agrega un objeto libro a la colección."""
        self.books.append(book)

    def get_all_books(self) -> list[Book]:
        """Obtiene la lista completa de libros almacenados."""
        return self.books
