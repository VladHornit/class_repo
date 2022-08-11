
#Class exercise file
class Book:
    def __init__(self, title, book_id):
        self.title = title
        self.book_id = book_id
book_1 = Book("The Great Gatsby", 1)
book_2 = Book("The Lord of the Rings", 2)



class Library:
    def __init__(self,city, name, book_list, user_list):
        self.city = city
        self.name = name
        self.book_list = book_list
        self.user_list = user_list

    def add_book(self, book):
        self.book_list.append(book)

    def add_users(self, users):
        user_list.append(user)

first_library = Library("Brussels", "Uccle libtary",[book_1], [])

first_library.add_book(book_2)

class User:
    def __init__(self, borrowed_books):
        self.borrowed_books = []

    def borrow_book(self, library)
