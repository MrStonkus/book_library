


# create Distributor class
class Distributor:
    def __init__(self):
        self.books = []

    def create_book(self):
        isbn = input("Enter book's ISBN number: ")
        title = input("Enter book's title: ")
        author = input("Enter book's author: ")
        year = input("Enter year of publication: ")
        new_book = Book(isbn, title, author, year)
        self.books.append(new_book)

    def list_books(self):
        for book in self.books:
            print(book)


# Create library class


# state could be: root, library, borrowed
class Book:
    def __init__(self, isbn, title, author, year, state='root'):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.state = state


# create menu
if __name__ == '__main__':
    distributor = Distributor()


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
                    distributor.create_book()
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
