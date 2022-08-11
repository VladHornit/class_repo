
#Class exercise file
class Book:
    def __init__(self, title, book_id, status):
        self.title = title
        self.book_id = book_id
        self.status = status
book_1 = Book("The Great Gatsby", 1, "avaliable")
book_2 = Book("The Lord of the Rings", 2,"avaliable")



class Library:
    def __init__(self,city, name, book_list, user_list):
        self.city = city
        self.name = name
        self.book_list = book_list
        self.user_list = user_list

    def add_book(self, book):
        self.book_list.append(book)

    def add_users(self, user):
        self.user_list.append(user)

first_library = Library("Brussels", "Uccle libtary",[book_1], [])
first_library.name = "paris"
first_library.add_book(book=book_2)

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
            else:
                print("The book is borrowed")

                #print(book.status)

                #print(book.status)
                for i in library.book_list:
                    print(i.status, i.title)
        else:
            print("Book is not in the library")

    def return_book(self, library, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)

vlad = User("Vlad")
vlad.borrow_book(first_library, book_1)
vlad.return_book(first_library,book_1)
