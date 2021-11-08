from distributor import *
from library import *


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
                        # TODO make function for all
                    case 3:
                        # Buy book
                        books = distributor.get_books()
                        self.list_books(books, "published")
                        book_nr = self.get_customer_input('buy')
                        if book_nr <= 0 or book_nr > len(distributor.books):
                            text = f'Incorrect number. It must be from 1 to {len(distributor.books)} !'
                            console.print(text)
                        else:
                            # get original book from distributor
                            original_book = distributor.books[book_nr - 1]
                            book_copy = library.buy_book(original_book)
                            print(f'Success, purchased book -> {book_copy.to_string()}')
                    case 4:
                        # List all library's books
                        books = library.get_all_books()
                        self.list_books(books, "library")
                    case 5:
                        # Borrow book
                        available_books = library.get_available_books()
                        self.list_books(available_books, "available")
                        book_nr = self.get_customer_input('borrow')
                        if book_nr <= 0 or book_nr > len(available_books):
                            print(f'Incorrect number. It must be from 1 to {len(available_books)} !')
                        else:
                            borrowed_book = library.borrow_book(book_nr, available_books)
                            print(f'Success, borrowed book -> {borrowed_book.to_string()}')
                    case 6:
                        # Return book
                        borrowed_books = library.get_borrowed_books()
                        self.list_books(borrowed_books, "borrowed")
                        book_nr = self.get_customer_input('return')
                        if book_nr <= 0 or book_nr > len(borrowed_books):
                            print(f'Incorrect number. It must be from 1 to {len(borrowed_books)} !')
                        else:
                            returned_book = library.return_book(book_nr, borrowed_books)
                            print(f'Success, returned book -> {returned_book.to_string()}')
                    case 7:
                        # Search book
                        search_text = self.get_customer_input('search')
                        results = library.search_book(search_text)
                        if results:
                            self.list_books(results, 'search_results')
                        else:
                            print('Sorry, no results by searching criteria.')
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

    # @book_state could be published, library, available and borrowed
    def list_books(self, books, book_state):
        if not len(books):
            print(f'There are no {book_state} books...')
        else:
            nr = 1
            if book_state == 'library':
                print(f"------ All library's books ------")
                for book in books:
                    print(f'{nr}. {book.to_string()}')
                    nr += 1
            elif book_state == 'published':
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
