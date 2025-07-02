

class Library:

    def __init__(self, name: str, address: str, books: list = []):


        self.__name = self.__check_name(name)
        self.__address = self.__check_address(address)
        self.__books = self.__check_books(books)


    def __check_name(self, name):

        if not isinstance(name, str):
            raise TypeError('Ввод не соответствует строке')

        if name.isspace() or name == '':
            raise TypeError('Ввод состоит из пробелов или пустой строки')

        return name

    def __check_address(self, address):

        if not isinstance(address, str):
            raise TypeError('Ввод не соответствует строке')

        if address.isspace() or address == '':
            raise TypeError('Ввод состоит из пробелов или пустой строки')

        return address

    def __check_books(self, books):

        if not isinstance(books, list):
            raise TypeError('Ввод не соответствует списку')

        return books

    def __check_len_list_books(self, books):

        if len(books) == 0:
            return False

        return True

    def __check_book_in_list(self, book: 'Book'):

        if book.get_book() in self.get_books():
            return True

        return False

    def get_books(self):

        return self.__books

    def add_book(self, book: 'Book'):

        if self.__check_book_in_list(book):
            print('Данная книга уже имеется в библиотеке ')
            return

        self.__books.append(book.get_book())

    def remove_book(self, book: 'Book'):

        if not self.__check_book_in_list(book):
            print('Данной книги в библиотеке нет')
            return

        self.__books.remove(book.get_book())

    def list_books(self):

        return f'{self.__books}'

    def find_book_by_title(self, title: str):

        if not isinstance(title, str):
            raise TypeError('Ввод не соответствует строке')

        if not self.__check_len_list_books(self.get_books()):
            print('В библиотеке нет книг')
            return None

        lst = self.get_books()

        for line in lst:

            if title == line.split(",")[0]:
                return line

            else:
                return None


class Book:

    def __init__(self, title, author, year, total_pages: int):

        self.__title = self.__check_title(title)
        self.__author = self.__check_title(author)
        self.__year = self.__check_year(year)
        self.__total_pages = self.__check_total_pages(total_pages)
        self.__book = ",".join([self.__title, self.__author, str(self.__year)])

    def __check_title(self, title):

        if not isinstance(title, str):
            raise TypeError('Данные не соответствуют строке')

        if title.isspace() or title == '':
            raise ValueError('Строка пустая или содержит одни пробелы')

        return title

    def __check_author(self, author):

        if not isinstance(author, str):
            raise TypeError('Данные не соответствуют строке')

        if author.isspace() or author == '':
            raise ValueError('Строка пустая или содержит одни пробелы')

        return author

    def __check_year(self, year):

        if not str(year).isdigit():
            raise TypeError('Данные не соответствуют числу или отрицательны')

        if not isinstance(year, int):
            raise TypeError('Данные не соответствуют целому числу')

        if len(str(year)) < 4 or len(str(year)) > 4:
            raise ValueError('Год должен состоять из 4х цифр')

        if year < 1000 or year > 2025:
            raise ValueError('Значение года должно быть в интервале'
                             ' 1000 до 2025 включая значения интервалов')

        return year

    def __check_total_pages(self, total_pages):

        if not str(total_pages).isdigit():
            raise TypeError('Данные не соответствуют числу или отрицательны')

        if not isinstance(total_pages, int):
            raise TypeError('Данные не соответствуют целому числу')

        if total_pages < 10 or total_pages > 5000:
            raise ValueError('Значение количества страниц должно быть в интервале'
                             ' от 10 до 5000 включая значения интервалов')

        return total_pages

    def get_info(self):

        return self.__book

    def get_total_pages(self):

        return self.__total_pages

    def get_book(self):
        return self.__book

    def bookmark_page(self, page: int):

        self.__check_total_pages(page)

        if page > self.get_total_pages():
            raise ValueError(f'Значение закладки больше {self.get_total_pages()} '
                             f'страниц в данной книге')

        print(f'Закладка установлена на странице {page}')

    def update_title(self, new_title: str):

        self.__check_title(new_title)
        self.__title = new_title

b1 = Book("Война и мир", "Л. Толстой", 1869, 275)
b2 = Book("Горе от ума", "А. С. Грибоедов", 1824, 275)
lib = Library("Центральная библиотека", "ул. Ленина, 10")
lib.find_book_by_title(5)
lib.add_book(b1)
lib.add_book(b2)
print(lib.get_books())
b1.bookmark_page(237)
print(b1.get_info())