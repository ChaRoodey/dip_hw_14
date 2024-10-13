class BookNotFoundError(Exception):
    def __str__(self):
        return 'Книга не найдена'


class Library:
    def __init__(self, books=None):
        if books is None:
            self.books = []
        else:
            self.books = books

    def add_book(self, book: str):
        self.books.append(book)

    def remove_book(self, book: str):
        if book in self.books:
            for i in range(len(self.books)):
                if self.books[i] == book:
                    self.books.pop(i)
                    break
        else:
            raise BookNotFoundError

    def list_books(self):
        return ', '.join(i for i in self.books)


if __name__ == '__main__':
    l1 = Library(['k1', 'k2', 'k3'])
    l1.remove_book('k4')
    print(l1.list_books())
