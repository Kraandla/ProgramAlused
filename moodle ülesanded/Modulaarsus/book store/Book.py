"""Book."""


class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor. Each book has title, author and price.

        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __eq__(self, other) -> bool:
        return (isinstance(other
                          , Book) and other.title == self.title and
                other.author == self.author and other.price == self.price and other.rating == self.rating)

    def __repr__(self):
        return f"Book: {self.title} Author: {self.author} Price: {self.price} Rating: {self.rating}"