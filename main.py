
# state could be: pub, library and borrowed.  Depending of the location
# ISBN contains simple digits without dashes
class Book:
    def __init__(self, isbn_nr, title_tx, author_tx, year_int, state='pub'):
        self.isbn = isbn_nr
        self.title = title_tx
        self.author = author_tx
        self.year = year_int
        self.state = state


# Distributor has new publicised books available for library
class Distributor:
    def __init__(self):
        self.books = []

    def create_book(self, isbn_nr, title_tx, author_tx, year_int):
        new_book = Book(isbn_nr, title_tx, author_tx, year_int)
        if self.check_for_dublicate(new_book.isbn):
            print("The same ISBN number is in the list!")
        else:
            self.books.append(new_book)

    def list_books(self):
        print('------ LIST OF AVAILABLE BOOKS ------')
        nr = 1
        for book in self.books:
            print(f'{nr}. {book.isbn} {book.title} {book.author} {book.year}')
            nr += 1

    def check_for_dublicate(self, isbn_nr):
        # get all isbn numbers in list
        isbn_list = []
        for book in self.books:
            isbn_list.append(book.isbn)
        # check list for the same isbn
        if isbn_nr in isbn_list:
            return True
        else:
            return False

# Create library class





# create menu
if __name__ == '__main__':
    distributor = Distributor()

    # load default books
    distributor.create_book(100, 'title1', 'author1', 2001)
    distributor.create_book(101, 'title2', 'author2', 2002)
    distributor.create_book(101, 'title3', 'author3', 2003)
    distributor.create_book(103, 'title4', 'author4', 2004)



    # console functions

    def get_new_book_inputs():

        isbn_nr = input("Enter book's ISBN number (only numbers): ")
        title_tx = input("Enter book's title: ")
        author_tx = input("Enter book's author: ")
        year_nr = input("Enter year of publication: ")
        return isbn_nr, title_tx, author_tx, year_nr

    isQuit = False
    while not isQuit:
        print('''
        ------ LIBRARY MENU ------
        
        1. Create new book
        2. List publication books
        3. Buy book
        4. List books in library
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
                    isbn, title, author, year = get_new_book_inputs()
                    distributor.create_book(isbn, title, author, year)
                case 2:
                    distributor.list_books()
                case 3:
                    print('3')
                case 4:
                    print('4')
                case 5:
                    print('5')
                case 6:
                    print('6')
                case 7:
                    print('7')
                case 8:
                    isQuit = True
                case _:
                    print('Choose from 1 to 8!')
