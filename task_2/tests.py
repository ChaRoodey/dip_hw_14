import unittest
from task_2.main import Library, BookNotFoundError


class TestLibrary(unittest.TestCase):

    def setUp(self):
        self.library = Library()

    def test_init(self):
        self.assertIs('', self.library.list_books())

    def test_add_book(self):
        self.library.add_book('k1')
        self.assertIn('k1', self.library.list_books())

    def test_remove_book(self):
        self.library.add_book('k1')
        self.library.remove_book('k1')
        self.assertNotIn('k1', self.library.list_books())

    def test_Book_not_found_error(self):
        with self.assertRaises(BookNotFoundError):
            self.library.remove_book('k1')


if __name__ == '__main__':
    unittest.main()