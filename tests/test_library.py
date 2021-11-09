import unittest

from library import *
from book import *

class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()


    def test_buy_book(self):
        expecting = 'ISBN:45 title:Title1 author:Author year:1960 state:available'

        book = Book(45, 'Title1', 'Author', 1960)
        self.library.buy_book(book)
        result = self.library.available_books[0].to_string()

        self.assertEqual(expecting, result)


    def test_get_all_books(self):
        # add books to library
        self.add_books_to_available_library()

        self.add_books_to_borrowed_library()

        result = len(self.library.get_all_books())
        self.assertEqual(6, result)


    def test_get_available_books(self):
        # add books to library
        self.add_books_to_available_library()
        result = len(self.library.get_available_books())
        self.assertEqual(3, result)


    def test_borrow_book(self):
        # add books to library
        self.add_books_to_available_library()
        result = self.library.borrow_book(2, self.library.available_books)
        expecting = 'ISBN:0 title:Title1 author:Author1 year:2001 state:borrowed'
        self.assertEqual(expecting, result.to_string())

    def test_get_borrowed_books(self):
        # add books to library
        self.add_books_to_borrowed_library()
        result = len(self.library.get_borrowed_books())
        self.assertEqual(3, result)


    def test_return_book(self):
        # add books to library
        self.add_books_to_borrowed_library()
        result = self.library.return_book(3, self.library.borrowed_books)
        expecting = 'ISBN:100 title:TitleII2 author:AuthorII2 year:1902 state:available'
        self.assertEqual(expecting, result.to_string())

    def test_search_book(self):
        # add books to library
        self.add_books_to_available_library()
        self.add_books_to_borrowed_library()

        # add additional books that need to be found
        expected_book1 = Book(66, 'Boss', 'Fill', 2015)
        self.library.available_books.append(expected_book1)
        expected_book2 = Book(77, 'Boss', 'Tom', 2017)
        self.library.available_books.append(expected_book2)

        result = self.library.search_book('Boss')
        result = (result[0] == expected_book1 and result[1] == expected_book2)
        self.assertTrue(result)


    def test_sort_by_date(self):
        # add books with various years to library
        book1 = Book(111, 'Title1', 'Author1', 2000)
        self.library.available_books.append(book1)
        book2 = Book(222, 'Title2', 'Author2', 1900)
        self.library.available_books.append(book2)
        book3 = Book(333, 'Title3', 'Author3', 2020)
        self.library.available_books.append(book3)

        sorted_books = self.library.sort_by_date(self.library.available_books)
        result = sorted_books[0].year < sorted_books[1].year < sorted_books[2].year

        self.assertTrue(result)

    # helper functions, not tests
    def add_books_to_borrowed_library(self):
        isbn = 100
        for i in range(3):
            book = Book(isbn, f'TitleII{i}', f'AuthorII{i}', 1900 + i)
            self.library.borrowed_books.append(book)

    def add_books_to_available_library(self):
        isbn = 0
        for i in range(3):
            book = Book(isbn, f'Title{i}', f'Author{i}', 2000 + i)
            self.library.available_books.append(book)



if __name__ == '__main__':
    unittest.main()
