"""Módulo para formatear la información visual de los libros."""

from typeBook import Book


class Formatter:
    """Proporciona métodos de formato para la interfaz visual."""

    @staticmethod
    def format_book_summary(book: Book) -> str:
        """Genera un resumen en texto de un libro."""
        stars = '★' * book.rating + '☆' * (5 - book.rating)
        return f'"{book.title}" por {book.author} - {stars}'
