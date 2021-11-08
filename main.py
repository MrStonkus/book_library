import copy
from book import *
from distributor import *

# # distributor class
# # Distributor has new publicised books available for library
# class Distributor:
#     def __init__(self):
#         self.books = []
#
#     def create_book(self, isbn_nr, title_tx, author_tx, year_int):
#         new_book = Book(isbn_nr, title_tx, author_tx, year_int)
#
#         # Chek for dublicates
#         # get all isbn numbers in list
#         isbn_list = []
#         for book in self.books:
#             isbn_list.append(book.isbn)
#         # check list for the same isbn
#         if new_book.isbn in isbn_list:
#             print("The same ISBN number is in the list!")
#         else:
#             self.books.append(new_book)
#
#     def list_books(self):
#         console.list_books(self.books, "published")


# library class
class Library:
    def __init__(self):
        self.available_books = []
        self.borrowed_books = []

    def buy_book(self):
        console.list_books(distributor.books, 'published')
        book_nr = console.get_customer_input('buy')
        if book_nr <= 0 or book_nr > len(distributor.books):
            text = f'Incorrect number. It must be from 1 to {len(distributor.books)} !'
            console.print(text)
        else:
            # get original book from distributor
            original_book = distributor.books[book_nr -1]
            # make copy
            book_copy = copy.deepcopy(original_book)
            book_copy.state = 'available'
            self.available_books.append(book_copy)

            text = f'Bought book {book_copy.to_string()}'
            console.print(text)

    def list_books(self):
        self.available_books = self.sort_by_date(self.available_books)
        self.borrowed_books = self.sort_by_date(self.borrowed_books)
        console.list_books(self.available_books, "available")
        console.list_books(self.borrowed_books, "borrowed")

    def borrow_book(self):
        self.available_books = self.sort_by_date(self.available_books)
        console.list_books(self.available_books, 'available')
        book_nr = console.get_customer_input('borrow')
        if book_nr <= 0 or book_nr > len(library.available_books):
            text = f'Incorrect number. It must be from 1 to {len(library.available_books)} !'
            console.print(text)
        else:
            # get book by number and remove from available_books array
            borrowed_book = library.available_books.pop(book_nr - 1)
            borrowed_book.state = 'borrowed'
            # set book to borrowed array
            self.borrowed_books.append(borrowed_book)

            text = f'The book {borrowed_book.to_string()} has been borrowed'
            console.print(text)

    def return_book(self):
        console.list_books(library.borrowed_books, 'borrowed')
        book_nr = console.get_customer_input('return')
        if book_nr <= 0 or book_nr > len(library.borrowed_books):
            text = f'Incorrect number. It must be from 1 to {len(library.borrowed_books)} !'
            console.print(text)
        else:
            # get book by number and remove from borrowed_books array
            returning_book = library.borrowed_books.pop(book_nr - 1)
            returning_book.state = 'available'
            # set book to available_books array
            self.available_books.append(returning_book)

            text = f'The book {returning_book.to_string()} has been returned to library'
            console.print(text)

    def search_book(self):
        search_input = console.get_customer_input('search')
        # search will be from two arrays, from available and borrowed books
        library_books = library.available_books + library.borrowed_books
        res_title = list(filter(lambda x: x.title == search_input, library_books))
        res_author = list(filter(lambda x: x.author == search_input, library_books))
        results_arr = res_title + res_author
        sorted_arr = self.sort_by_date(results_arr)
        if sorted_arr:
            console.list_books(sorted_arr, 'search_results')
        else:
            text = 'Sorry, no results by searching criteria.'
            console.print(text)
    # sort by book date
    def sort_by_date(self, books):
        return sorted(books, key=lambda book_copy: book_copy.year)

# console class (main)
class Console:
    def print_menu(self):

        exit_out = False
        while not exit_out:
            print('''
                ------ LIBRARY MENU ------

                1. Create new book (publish)
                2. List published books
                3. Buy book
                4. List all library's books
                5. Borrow book
                6. Return book
                7. Search book
                8. Quit
                ''')
            try:
                menu_nr = int(input('Enter menu number (1-8): '))
            except ValueError:
                print('Choose from 1 to 8!')
            else:
                match menu_nr:
                    case 1:
                        # Create new book(publish)
                        isbn, title, author, year = self.get_new_book_inputs()
                        new_book = distributor.create_book(isbn, title, author, year)
                        if new_book:
                            print(f'Success, new book -> {new_book.to_string()} was created.')
                        else:
                            print("Book was not created, check ISBN number!")
                    case 2:
                        # List published books
                        books = distributor.get_books()
                        self.list_books(books, "published")
                    case 3:
                        # Buy book
                        library.buy_book()
                    case 4:
                        # List all library's books
                        library.list_books()
                    case 5:
                        # Borrow book
                        library.borrow_book()
                    case 6:
                        # Return book
                        library.return_book()
                    case 7:
                        # Search book
                        library.search_book()
                    case 8:
                        # Quit
                        exit_out = True
                    case _:
                        print('Choose from 1 to 8!')

    def get_new_book_inputs(self):
        print('*all inputs are required!')

        while True:
            try:
                isbn_nr = int(input("Enter book's ISBN number (only numbers): "))
            except ValueError:
                print("This is an unaccepted response, enter a valid value")
                continue
            else:
                break

        while True:
            try:
                title_tx = input("Enter book's title: ")
                if not title_tx:
                    raise ValueError('Empty string!')
            except ValueError as e:
                print(e)
                continue
            else:
                break

        while True:
            try:
                author_tx = input("Enter book's author: ")
                if not author_tx:
                    raise ValueError('Empty string!')
            except ValueError as e:
                print(e)
                continue
            else:
                break

        while True:
            try:
                year_nr = int(input("Enter year of publication (only numbers): "))
            except ValueError:
                print("This is an unaccepted response, enter a valid value")
                continue
            else:
                break

        return isbn_nr, title_tx, author_tx, year_nr

    # @book_state could be published, available and borrowed
    def list_books(self, books, book_state):
        if not len(books):
            print(f'There are no {book_state} books...')
        else:
            nr = 1
            if book_state == 'published':
                print('------ List of published books to buy ------')
                for book in books:
                    print(f'{nr}. {book.to_string()}')
                    nr += 1
            elif book_state == 'available':
                print('------ List available books in Library  ------')
                for book in books:
                    print(f'{nr}. {book.to_string()}')
                    nr += 1
            elif book_state == 'borrowed':
                print('------ List borrowed books in Library  ------')
                for book in books:
                    print(f'{nr}. {book.to_string()}')
                    nr += 1
            elif book_state == 'search_results':
                print('------ Search results ------')
                for book in books:
                    print(f'{nr}. {book.to_string()}')
                    nr += 1


    def print(self, text):
        print(text)


    # type can be (buy, borrow and return)
    def get_customer_input(self, type):
        if type == 'search':
            print('------ SEACH ------')
            input_nr = input(f'Enter Title or Author of the looking book :')
        else:
            while True:
                try:
                    input_nr = int(input(f'Enter row number of book to {type}: (exm. 1 to {type} first book) :'))
                except ValueError:
                    print("This is an unaccepted response, enter a valid value")
                    continue
                else:
                    break
        return input_nr



# app start
if __name__ == '__main__':
    console = Console()
    distributor = Distributor()
    library = Library()

    # load default books
    distributor.create_book(100, 'title1', 'author1', 2010)
    distributor.create_book(101, 'title1', 'author1', 2002)
    distributor.create_book(102, 'title1', 'author1', 2020)
    distributor.create_book(103, 'title4', 'author4', 2004)

    console.print_menu()
