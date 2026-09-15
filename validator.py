class Validator:
    @staticmethod
    def validate_book_data(
        title: str, author: str, rating_str: str, review: str
    ) -> bool:

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
        return 1 <= rating <= 5