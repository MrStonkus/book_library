import copy


# library class
class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def buy_book(self, org_book):
        # make copy
        book_copy = copy.deepcopy(org_book)
        book_copy.state = 'available'
        self.available_books.append(book_copy)
        self.available_books = self.sort_by_date(self.available_books)
        return book_copy

    def get_all_books(self):
        # TODO make sorting at the update list
        arr1 = self.available_books
        arr2 = self.borrowed_books
        all_books = arr1 + arr2
        sorted_books = self.sort_by_date(all_books)
        return sorted_books

    def get_available_books(self):
        available_books = self.available_books
        return available_books

    def borrow_book(self, book_nr, available_books):
        # get book by number and remove from available_books array
        borrowed_book = available_books.pop(book_nr - 1)
        borrowed_book.state = 'borrowed'
        # update borrowed array
        self.borrowed_books.append(borrowed_book)
        self.borrowed_books = self.sort_by_date(self.borrowed_books)

        return borrowed_book

    def get_borrowed_books(self):
        borrowed_books = self.borrowed_books
        return borrowed_books

    def return_book(self, book_nr, borrowed_books):
        # get book by number and remove from borrowed_books array
        returning_book = borrowed_books.pop(book_nr - 1)
        returning_book.state = 'available'
        # update available_books array
        self.available_books.append(returning_book)
        self.available_books = self.sort_by_date(self.available_books)
        return returning_book

    def search_book(self, search_text):
        # search will be from two arrays, from available and borrowed books
        books = self.get_all_books()

        res_title = list(filter(lambda x: x.title == search_text, books))
        res_author = list(filter(lambda x: x.author == search_text, books))
        results_arr = res_title + res_author
        sorted_arr = self.sort_by_date(results_arr)
        return sorted_arr

    # sort by book date
    def sort_by_date(self, books):
        return sorted(books, key=lambda book: book.year)
