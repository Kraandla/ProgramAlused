from Store import Store
from Book import Book

if __name__ == '__main__':
    book1 = Book("Sipsik", "Eno Raud", 5,5)
    book2 = Book("Sipsik", "Eno Raud", 5, 5)

    shop = Store("Black Books", 5)

    shop.add_book(book1)
    shop.add_book(book2)

    print(shop.get_books_by_price())
    shop.remove_book(book1)
    print(shop.books)