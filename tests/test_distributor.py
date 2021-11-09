import unittest

from book import *
from distributor import *


class TestDistributor(unittest.TestCase):
    def setUp(self):
        self.distributor = Distributor()

    def test_create_book(self):
        new_object = self.distributor.create_book(66, 'Title', 'Author', 2006)
        self.assertEqual('ISBN:66 title:Title author:Author year:2006 state:published', new_object.to_string())


    def test_create_book_duplicate(self):
        self.distributor.create_book(66, 'Title', 'Author', 2006)
        duplicate = self.distributor.create_book(66, 'Title', 'Author', 2006)
        self.assertEqual(False, duplicate)


    def test_get_books(self):
        self.distributor.create_book(66, 'Title', 'Author', 2006)
        self.distributor.create_book(33, 'Title2', 'Author2', 2020)
        self.distributor.create_book(400, 'Title3', 'Author3', 2000)
        self.assertEqual(3, len(self.distributor.get_books()))

    def test_sort_by_date(self):
        self.distributor.create_book(66, 'Title', 'Author', 2006)
        self.distributor.create_book(33, 'Title2', 'Author2', 2020)
        self.distributor.create_book(400, 'Title3', 'Author3', 2000)
        books = self.distributor.books
        is_sorted = False
        if books[0].year < books[1].year < books[2].year:
            is_sorted = True
        else:
            is_sorted = False
        self.assertTrue(is_sorted)


if __name__ == '__main__':
    unittest.main()

