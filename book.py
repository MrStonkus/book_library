# book class
# ISBN contains simple digits without dashes
# @state could be published, available and borrowed
class Book:
    def __init__(self, isbn_nr, title_tx, author_tx, year_int, state_tx='published'):
        self.isbn = isbn_nr
        self.title = title_tx
        self.author = author_tx
        self.year = year_int
        self.state = state_tx

    def to_string(self):
        return f'ISBN:{self.isbn} title:{self.title} author:{self.author} year:{self.year} state:{self.state}'
