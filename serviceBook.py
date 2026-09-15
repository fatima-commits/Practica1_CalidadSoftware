"""Módulo de capa de servicio para libros."""

from repositoryBook import BookRepository
from typeBook import Book
from validator import Validator


class BookService:
    """Servicio para coordinar la lógica de registro de libros."""

    def __init__(self, repo: BookRepository) -> None:
        """Inicializa el servicio de libros."""
        self.repo = repo

    def register_book(
        self, title: str, author: str, rating_str: str, review: str
    ) -> bool:
        """Registra un libro si pasa las comprobaciones de validación."""
        if not Validator.validate_book_data(title, author, rating_str, review):
            return False

        book = Book(
            title=title.strip(),
            author=author.strip(),
            rating=int(rating_str),
            review=review.strip(),
        )
        self.repo.add_book(book)
        return True
