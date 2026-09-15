from typeBook import Book


class Formatter:
    @staticmethod
    def format_book_summary(book: Book) -> str:
        stars = '★' * book.rating + '☆' * (5 - book.rating)
        return f'"{book.title}" por {book.author} - {stars}'