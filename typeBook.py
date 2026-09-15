class Book:
    def __init__(
        self, title: str, author: str, rating: int, review: str
    ) -> None:
        self.title = title
        self.author = author
        self.rating = rating
        self.review = review
        