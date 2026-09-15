"""Módulo de validación de entradas del usuario."""

MAX_RATING = 5


class Validator:
    """Proporciona validaciones de reglas de negocio para los libros."""

    @staticmethod
    def validate_book_data(
        title: str, author: str, rating_str: str, review: str
    ) -> bool:
        """Valida que la información de un libro sea correcta."""
        if not (
            title.strip()
            and author.strip()
            and rating_str.strip()
            and review.strip()
        ):
            return False

        if not rating_str.isdigit():
            return False

        rating = int(rating_str)
        return 1 <= rating <= MAX_RATING
