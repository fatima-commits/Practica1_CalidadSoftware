"""Módulo de capa de servicio para libros."""

from typeBook import Book
from repositoryBook import BookRepository
from validator import Validator


class BookService:

    def __init__(self, repo: BookRepository) -> None:
        self.repo = repo

    def register_book(
        self, title: str, author: str, rating_str: str, review: str
    ) -> bool:
        
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