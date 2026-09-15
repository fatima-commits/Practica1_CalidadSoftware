"""Módulo que define la entidad Libro."""


class Book:
    """Clase que representa un libro leído con su reseña."""

    def __init__(
        self, title: str, author: str, rating: int, review: str
    ) -> None:
        """Inicializa una instancia de la clase Book."""
        self.title = title
        self.author = author
        self.rating = rating
        self.review = review
