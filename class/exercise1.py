
#Class exercise file
import time

class Book:
    def __init__(self, title, book_id):

        self.title = title
        self.book_id = book_id
        self.status = 'avaliable'
        self.start_time = 0


class Library:
    def __init__(self,city, name, book_list, user_list, money):
        self.city = city
        self.name = name
        self.book_list = book_list
        self.user_list = user_list
        self.money = money

    def add_book(self, book):
        self.book_list.append(book)

    def add_users(self, user):
        self.user_list.append(user)


class User:
    def __init__(self, name_argument):
        self.name = name_argument
        self.borrowed_books = []

    def borrow_book(self, library, book):
        '''for i in library.book_list:
            print(i.status, i.title)'''
        if self in library.user_list:
            if book in library.book_list:
                if book.status == "avaliable":
                    self.borrowed_books.append(book)
                    book.status = "borrowed"
                    book.start_time = time.time()
                    print('book borrwed', book.title)
                else:
                    print('book already borrowed')
            else:
                print("The book is not in lib")

                #print(book.status)

                #print(book.status)
                for i in library.book_list:
                    print(i.status, i.title)
        else:
            print("User is not in the library")

    def return_book(self, library, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            if time.time() - book.start_time < 3:
                book.status = "avaliable"
            else:
                book.status = "avaliable"
        if time.time() - book.start_time > 3:
            library.money = library.money  + (time.time() - book.start_time)



book_1 = Book("The Great Gatsby", 1, "avaliable", time.time())
book_2 = Book("The Lord of the Rings", 2,"avaliable", time.time())


first_library = Library("Brussels", "Uccle libtary",[book_1], [], 100)
first_library.name = "paris"
first_library.add_book(book=book_2)
vlad = User("Vlad")
first_library.add_users(vlad)



vlad.borrow_book(first_library, book_1)
vlad.return_book(first_library,book_1)
