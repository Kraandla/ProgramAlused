class Book:

    def __init__(self, author: str, title: str, cover: str, rating: int, length: int):
        """
        Book constructor.
        :param author: Name of author
        :param title: Title of book
        :param cover: Color of the cover
        :param rating: Rating of the book
        :param pages: How many pages the book has
        """
        self.author = author
        self.title = title
        self.cover = cover
        self.rating = rating
        self.length = length

    def __repr__(self):
        return f"Author: {self.author} Title: {self.title} Cover: {self.cover} Rating: {self.rating} Length: {self.length} pages"


class Library:
    def __init__(self, library_name:str):
        self.library = library_name
        self.library_books = []
        self.book_amount = 0


    def can_add_book(self, book: Book) -> bool:
        """
        1. Checks if the library stores a book with the same details and
        2. Checks if the book has over 5 pages
        :param book: Book construct
        :return: bool
        """
        if book not in self.library_books and book.length > 5:
            return True
        return False

    def add_book(self, book:Book) -> None:
        """
        Adds book if the book is valid and isn't in the library.
        Return none if it is not valid.
        :param book: Book construct
        :return: None
        """
        if self.can_add_book(book):
            self.library_books.append(book)
            self.book_amount += 1
        else:
            return

    def can_remove_book(self, book: Book):
        """
        If library has book returns bool to check if it can be removed.
        """
        return book in self.library_books

    def remove_book(self, book: Book):
        """
        Removes a book if the book is inside the library.
        :param book:
        """
        if self.can_remove_book(book):
            self.library_books.remove(book)
            self.book_amount -= 1

    def what_sentence_to_use(self) -> str:
        """
        Checks how many books the library has.
        If it has 1 book it returns a sentence with the word book.
        If it has no books it returns a sentence saying that.
        :return:
        """
        string = "books"
        string2 = "are"
        book_string = ""
        for x in self.library_books:
            book_string += x.title + ", "
        book_string = book_string[:-2] + "."
        if self.book_amount == 1:
            string = "book"
            string2 = "is"
        if self.book_amount > 0:
            sentence = f"The {self.library} library has {self.book_amount} {string} which {string2}: {book_string}"
        else:
            sentence = f"The {self.library} library has no books"
        return sentence

    def __repr__(self) -> str:
        """
        :return: Sentence
        """
        sentence = self.what_sentence_to_use()
        return sentence


class Libraries:

    def __init__(self):
        self.libraries = []

    def can_add_library(self, library_name: Library) -> bool:
        return library_name in self.libraries

    def add_library(self, library_name: Library)-> None:
        if self.can_add_library(library_name):
            self.libraries.append(library_name)
        else:
            return
    def get_libraries(self):
        return self.libraries

def console_commands():
    """
    Generates random data
    :return:
    """
    from random import randrange
    names = ["Joosep", "Mihkel", "Tauno", "Rooga", "Kevin Randla"]
    title = ["Rando", "Adventure", "Not adventure", "Cool adventure", "Baby adventure"]
    libraries = ["Rando", "Kookos", "Pahkel", "Targutaja"]
    for x in range(0, 40):
        print(f"new_library{x} = Library('{libraries[randrange(0,4)]}')")
    for x in range(0,60):
        author = names[randrange(0,4)]
        print(f"book{x} = Book(" + "'" + author + "'" + "," + "'" + title[randrange(0,4)]+ "','red'" + "," + str(randrange(0,365))+")")
    for x in range(0,40):
        print(f"new_library{x}.add_book(book{randrange(0,59)})")

if __name__ == '__main__':
    console_commands()

    new_library0 = Library('Kookos')
    new_library1 = Library('Targutaja')
    new_library2 = Library('Targutaja')
    new_library3 = Library('Kookos')
    new_library4 = Library('Pahkel')
    new_library5 = Library('Rando')
    new_library6 = Library('Pahkel')
    new_library7 = Library('Rando')
    new_library8 = Library('Rando')
    new_library9 = Library('Rando')
    new_library10 = Library('Kookos')
    new_library11 = Library('Rando')
    new_library12 = Library('Targutaja')
    new_library13 = Library('Rando')
    new_library14 = Library('Targutaja')
    new_library15 = Library('Rando')
    new_library16 = Library('Targutaja')
    new_library17 = Library('Pahkel')
    new_library18 = Library('Rando')
    new_library19 = Library('Targutaja')
    new_library20 = Library('Pahkel')
    new_library21 = Library('Kookos')
    new_library22 = Library('Kookos')
    new_library23 = Library('Pahkel')
    new_library24 = Library('Rando')
    new_library25 = Library('Rando')
    new_library26 = Library('Targutaja')
    new_library27 = Library('Pahkel')
    new_library28 = Library('Targutaja')
    new_library29 = Library('Targutaja')
    new_library30 = Library('Targutaja')
    new_library31 = Library('Rando')
    new_library32 = Library('Kookos')
    new_library33 = Library('Rando')
    new_library34 = Library('Kookos')
    new_library35 = Library('Targutaja')
    new_library36 = Library('Targutaja')
    new_library37 = Library('Rando')
    new_library38 = Library('Kookos')
    new_library39 = Library('Kookos')
    book0 = Book('Tauno', 'Adventure', 'red', 140)
    book1 = Book('Mihkel', 'Rando', 'red', 196)
    book2 = Book('Tauno', 'Adventure', 'red', 42)
    book3 = Book('Rooga', 'Adventure', 'red', 91)
    book4 = Book('Joosep', 'Cool adventure', 'red', 55)
    book5 = Book('Joosep', 'Cool adventure', 'red', 236)
    book6 = Book('Mihkel', 'Adventure', 'red', 7)
    book7 = Book('Tauno', 'Cool adventure', 'red', 80)
    book8 = Book('Mihkel', 'Rando', 'red', 81)
    book9 = Book('Joosep', 'Not adventure', 'red', 55)
    book10 = Book('Mihkel', 'Rando', 'red', 167)
    book11 = Book('Mihkel', 'Not adventure', 'red', 304)
    book12 = Book('Tauno', 'Cool adventure', 'red', 301)
    book13 = Book('Joosep', 'Rando', 'red', 290)
    book14 = Book('Tauno', 'Rando', 'red', 192)
    book15 = Book('Joosep', 'Rando', 'red', 253)
    book16 = Book('Tauno', 'Not adventure', 'red', 144)
    book17 = Book('Rooga', 'Not adventure', 'red', 159)
    book18 = Book('Tauno', 'Cool adventure', 'red', 185)
    book19 = Book('Rooga', 'Rando', 'red', 354)
    book20 = Book('Tauno', 'Adventure', 'red', 152)
    book21 = Book('Mihkel', 'Not adventure', 'red', 114)
    book22 = Book('Joosep', 'Adventure', 'red', 2)
    book23 = Book('Joosep', 'Cool adventure', 'red', 332)
    book24 = Book('Joosep', 'Not adventure', 'red', 125)
    book25 = Book('Mihkel', 'Not adventure', 'red', 200)
    book26 = Book('Rooga', 'Not adventure', 'red', 254)
    book27 = Book('Tauno', 'Cool adventure', 'red', 261)
    book28 = Book('Rooga', 'Adventure', 'red', 172)
    book29 = Book('Rooga', 'Not adventure', 'red', 75)
    book30 = Book('Mihkel', 'Not adventure', 'red', 200)
    book31 = Book('Mihkel', 'Not adventure', 'red', 347)
    book32 = Book('Rooga', 'Not adventure', 'red', 322)
    book33 = Book('Joosep', 'Rando', 'red', 38)
    book34 = Book('Joosep', 'Adventure', 'red', 9)
    book35 = Book('Rooga', 'Cool adventure', 'red', 37)
    book36 = Book('Rooga', 'Not adventure', 'red', 102)
    book37 = Book('Tauno', 'Adventure', 'red', 238)
    book38 = Book('Tauno', 'Cool adventure', 'red', 16)
    book39 = Book('Rooga', 'Rando', 'red', 214)
    book40 = Book('Tauno', 'Not adventure', 'red', 226)
    book41 = Book('Joosep', 'Cool adventure', 'red', 74)
    book42 = Book('Rooga', 'Not adventure', 'red', 83)
    book43 = Book('Joosep', 'Cool adventure', 'red', 97)
    book44 = Book('Rooga', 'Adventure', 'red', 104)
    book45 = Book('Joosep', 'Not adventure', 'red', 188)
    book46 = Book('Tauno', 'Cool adventure', 'red', 206)
    book47 = Book('Mihkel', 'Rando', 'red', 88)
    book48 = Book('Rooga', 'Rando', 'red', 199)
    book49 = Book('Joosep', 'Cool adventure', 'red', 15)
    book50 = Book('Tauno', 'Not adventure', 'red', 103)
    book51 = Book('Tauno', 'Rando', 'red', 50)
    book52 = Book('Joosep', 'Rando', 'red', 173)
    book53 = Book('Joosep', 'Rando', 'red', 50)
    book54 = Book('Mihkel', 'Not adventure', 'red', 248)
    book55 = Book('Tauno', 'Adventure', 'red', 334)
    book56 = Book('Tauno', 'Adventure', 'red', 247)
    book57 = Book('Rooga', 'Rando', 'red', 167)
    book58 = Book('Joosep', 'Adventure', 'red', 258)
    book59 = Book('Joosep', 'Rando', 'red', 66)
    new_library0.add_book(book0)
    new_library1.add_book(book6)
    new_library2.add_book(book8)
    new_library3.add_book(book1)
    new_library4.add_book(book5)
    new_library5.add_book(book42)
    new_library6.add_book(book22)
    new_library7.add_book(book30)
    new_library8.add_book(book23)
    new_library9.add_book(book57)
    new_library10.add_book(book25)
    new_library11.add_book(book9)
    new_library12.add_book(book55)
    new_library13.add_book(book58)
    new_library14.add_book(book33)
    new_library15.add_book(book13)
    new_library16.add_book(book3)
    new_library17.add_book(book3)
    new_library18.add_book(book31)
    new_library19.add_book(book16)
    new_library20.add_book(book54)
    new_library21.add_book(book26)
    new_library22.add_book(book57)
    new_library23.add_book(book41)
    new_library24.add_book(book26)
    new_library25.add_book(book22)
    new_library26.add_book(book21)
    new_library27.add_book(book36)
    new_library28.add_book(book45)
    new_library29.add_book(book21)
    new_library30.add_book(book37)
    new_library31.add_book(book29)
    new_library32.add_book(book1)
    new_library33.add_book(book58)
    new_library34.add_book(book6)
    new_library35.add_book(book3)
    new_library36.add_book(book27)
    new_library37.add_book(book42)
    new_library38.add_book(book13)
    new_library39.add_book(book48)

    # new_library.remove_book(book)
    # print(new_library.__repr__())