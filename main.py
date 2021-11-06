
# create book class


# create Distributor class


# Create library class

# create menu
if __name__ == '__main__':
    isQuit = False
    while not isQuit:
        print('''
        ------ LIBRARY MENU ------
        
        1. Create new book
        2. Buy book
        3. List books in library
        4. Borrow book
        5. Return book
        6. Search book
        7. Quit
        ''')
        menu_nr = int(input('Enter menu number (1-7): '))
        match menu_nr:
            case 1: print('1')
            case 2: print('2')
            case 3: print('3')
            case 4: print('4')
            case 5: print('5')
            case 6: print('6')
            case 7: isQuit = True
