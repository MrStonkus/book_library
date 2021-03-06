from book import *


# distributor class
# Distributor has new publicised books available for library
class Distributor:
    def __init__(self):
        self.books = []

    def create_book(self, isbn_nr, title_tx, author_tx, year_int):
        new_book = Book(isbn_nr, title_tx, author_tx, year_int)

        # Chek for ISBN number duplicates
        # get all existing ISBN numbers in list
        isbn_list = []
        for book in self.books:
            isbn_list.append(book.isbn)
        # check list for the same ISBN
        if new_book.isbn in isbn_list:
            return False
        else:
            self.books.append(new_book)
            self.books = self.sort_by_date(self.books)
            return new_book

    def get_books(self):
        return self.books

    # sort by book date
    def sort_by_date(self, books):
        return sorted(books, key=lambda book: book.year)
