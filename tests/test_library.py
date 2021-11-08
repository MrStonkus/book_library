from unittest import TestCase
from distributor import *
from library import *
from book import *

class TestLibrary(TestCase):

    def setUp(self):
        self.library = Library()

    def test_buy_book(self):
        expecting = 'ISBN:45 title:Title1 author:Author year:1960 state:available'

        book = Book(45, 'Title1', 'Author', 1960)
        self.library.buy_book(book)
        result = self.library.available_books[0].to_string()

        self.assertEqual(expecting, result)

    # def test_get_all_books(self):
    #     self.fail()
    #
    # def test_get_available_books(self):
    #     self.fail()
    #
    # def test_borrow_book(self):
    #     self.fail()
    #
    # def test_get_borrowed_books(self):
    #     self.fail()
    #
    # def test_return_book(self):
    #     self.fail()
    #
    # def test_search_book(self):
    #     self.fail()
    #
    # def test_sort_by_date(self):
    #     self.fail()
