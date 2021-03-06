import unittest

from book import *


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book(66, 'Title', 'Author', 2006)

    def test_to_string(self):
        self.assertEqual('ISBN:66 title:Title author:Author year:2006 state:published', self.book.to_string())

if __name__ == '__main__':
    unittest.main()

