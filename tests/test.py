import sys

sys.path.insert(0, '../class')

from exercise1 import User, Library, Book
import time
import unittest



class Tests(unittest.TestCase):

    def test_title(self):
        book_1 = Book("The Great Gatsby", 1)
        self.assertEqual(book_1.title, "The Great Gatsby")
        book_2 = Book("The Lord of the Rings", 1)
        self.assertEqual(book_2.title, "The Lord of the Rings")

    def test_book_id(self):
        book_1 = Book("The Great Gatsby", 1)
        self.assertEqual(book_1.book_id, 1)
        book_2 = Book("The Lord of the Rings", 2)
        self.assertEqual(book_2.book_id, 2)

    def test_city(self):
        book_1 = Book("The Great Gatsby", 1)
        first_library = Library("Brussels", "Uccle libtary",[book_1], [], 100)
        self.assertEqual(first_library.city, "Brussels")

    def test_name(self):
        book_1 = Book("The Great Gatsby", 1)
        first_library = Library("Brussels", "Uccle libtary",[book_1], [], 100)
        self.assertEqual(first_library.name, "Uccle libtary")

    def test_book_list(self):
        first_library = Library("Brussels", "Uccle libtary",[book_1], [], 100)
        self.assertEqual(first_library.book_list, ["The Great Gatsby"])

    def test_book_list(self):
        book_1 = Book("The Great Gatsby", 1)
        book_2 = Book("The Lord of the Rings", 2)
        first_library = Library("Brussels", "Uccle libtary",[], [], 100)
        first_library.add_book(book_1)
        first_library.add_book(book_2)
        self.assertEqual(first_library.book_list, [book_1, book_2])

    def test_user_list(self):
        book_1 = Book("The Great Gatsby", 1)
        first_library = Library("Brussels", "Uccle libtary",[book_1], [], 100)
        self.assertEqual(first_library.user_list, [])

    def test_money(self):
        book_1 = Book("The Great Gatsby", 1)
        first_library = Library("Brussels", "Uccle libtary",[book_1], [], 100)
        self.assertEqual(first_library.money, 100)

    def test_add_user(self):
        book_1 = Book("The Great Gatsby", 1)
        first_library = Library("Brussels", "Uccle libtary",[book_1], [], 100)
        vlad = User("Vlad")
        first_library.add_users(vlad)
        self.assertEqual(first_library.user_list, [vlad])

    def test_borrowing(self):
        book_1 = Book("The Great Gatsby", 1)
        first_library = Library("Brussels", "Uccle libtary",[], [], 100)
        vlad = User("Vlad")
        first_library.add_users(vlad)
        vlad.borrow_book(book_1)
        self.assertEqual(vlad.borrowed_books, [])

    def test_borrowing(self):
        book_1 = Book("The Great Gatsby", 1)
        book_2 = Book("The Lord of the Rings", 2)
        first_library = Library("Brussels", "Uccle libtary",[], [], 100)
        first_library.add_book(book_1)
        first_library.add_book(book_2)
        vlad = User("Vlad")
        first_library.add_users(vlad)
        self.assertEqual(first_library.user_list, [vlad])







'''    def test_add_book_to_the_book_list(self):


    def test_expected_empty_result_0(self):



        self.assertEqual(odd_or_even.divisor(0), [ ])

    def test_expected_empty_result_1(self):
        self.assertEqual(odd_or_even.divisor(1), [ ])

    def test_typererror(self):
        with self.assertRaises(TypeError):
            odd_or_even.divisor()("a")
'''
if __name__ == '__main__':
    unittest.main()
# This is the test file
