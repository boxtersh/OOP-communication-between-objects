

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
lib.find_book_by_title('5')
lib.add_book(b1)
lib.add_book(b2)
print(lib.get_books())
b1.bookmark_page(237)
print(b1.get_info())

# ***************** 2. Университет, Факультет и Студент (агрегация) ***************************

def check_id(id):
    if not isinstance(id, str):
        raise TypeError('Данные не соответствуют строке')

    if id.isspace() or id == '':
        raise ValueError('Строка пустая или содержит одни пробелы')

    return id

class University:

    def __init__(self, name, faculties: list = []):

        self.__name = self.__check_name(name)
        self.__faculties = self.__check_faculties(faculties)

    def __check_name(self, name):

        if not isinstance(name, str):
            raise TypeError('Данные не соответствуют строке')

        if name.isspace() or name == '':
            raise ValueError('Строка пустая или содержит одни пробелы')

        return name

    def __check_faculties(self, faculties):

        if not isinstance(faculties, list):
            raise TypeError('Данные не соответствуют списку')

        return faculties

    def __check_object(self, f: 'Faculty'):

        if not isinstance(f, Faculty):
            raise TypeError('Параметр не является объектом класса Faculty')

    def __check_len_list_faculties(self):

        if len(self.get_faculties()) == 0:
            return True

        return False

    def add_faculty(self, f: 'Faculty'):

        self.__check_object(f)
        self.get_faculties().append(f)

    def remove_faculty(self, f: 'Faculty'):

        self.__check_object(f)

        for f_object in self.get_faculties():

            if f_object == f:
                self.get_faculties().remove(f)

    def list_faculties(self):

        if self.__check_len_list_faculties():
            print('В университете нет факультетов')
            return

        for faculties in self.get_faculties():
            print(faculties.get_name_faculty())

    def find_faculty(self, name: str):

        self.__check_name(name)

        if self.__check_len_list_faculties():
            return None

        for faculty in self.get_faculties():

            if faculty.get_name_faculty() == name:
                return faculty

        return None

    def get_faculties(self):

        return self.__faculties


class Faculty:

    def __init__(self, name: str, students: list = []):

        self.__name = self.__check_name(name)
        self.__students = self.__check_students(students)

    def __check_name(self, name):

        if not isinstance(name, str):
            raise TypeError('Данные не соответствуют строке')

        if name.isspace() or name == '':
            raise ValueError('Строка пустая или содержит одни пробелы')

        return name

    def __check_students(self, students):

        if not isinstance(students, list):
            raise TypeError('Данные не соответствуют списку')

        return students

    def __check_len_list_grade(self):

        if len(self.get_students()) == 0:
            return True

        return False

    def __check_object(self, student: 'Student'):

        if not isinstance(student, Student):
            raise TypeError('Параметр не является объектом класса Student')

    def get_name_faculty(self):

        return self.__name

    def get_students(self):

        return self.__students

    def enroll(self, student: 'Student'):

        self.__check_object(student)

        self.get_students().append(student)

    def graduate(self, student: 'Student'):

        for link_stud in self.get_students():
            if student.get_id() == link_stud.get_id():
                self.get_students().remove(student)
                print(f'{student.get_profile()} - выпускник')

    def list_students(self):

        if self.__check_len_list_grade():
            print('На факультете нет студентов')
            return

        for student in self.get_students():
            print(student.get_profile())

    def find_student(self, id: str):

        check_id(id)

        if self.__check_len_list_grade():
            print('На факультете нет студентов')
            return

        for student in self.get_students():

            if student.get_id() == id:
                print(student.get_profile())
                return

            print(f'Студента с зачеткой N{id} в списке студентов нет')

class Student:

    def __init__(self, name: str, id: str, grades: list = []):

        self.__name = self.__check_name(name)
        self.__id = check_id(id)
        self.__grades = self.__check_grades(grades)
        self.__student = f'Студент: {self.__name}, ID: {self.__id}'

    def __check_name(self, name):

        if not isinstance(name, str):
            raise TypeError('Данные не соответствуют строке')

        if name.isspace() or name == '':
            raise ValueError('Строка пустая или содержит одни пробелы')

        return name

    def __check_grades(self, grades):

        if not isinstance(grades, list):
            raise TypeError('Данные не соответствуют списку')

        return grades

    def __check_grade(self, grade):

        if not str(grade).isdigit():
            raise TypeError('Данные не соответствуют числу или отрицательны')

        if not isinstance(grade, int):
            raise TypeError('Данные не соответствуют целому числу')

        if grade < 2 or grade > 5:
            raise ValueError('Значение оценки студента должна быть в интервале'
                             ' от 2 до 5 включая значения интервалов')

        return grade

    def __check_len_list_grade(self):

        if len(self.get_grades()) > 100:
            return True

        return False

    def get_grades(self):

        return self.__grades

    def get_id(self):

        return self.__id

    def get_profile(self):

        return self.__student

    def assign_grade(self, grade: int) -> None:

        self.__check_grade(grade)

        if self.__check_len_list_grade():
            raise ValueError('Список оценок заполнен и равен 100 оценкам')

        self.get_grades().append(grade)

uni = University("МГУ")
math = Faculty("Математический факультет")
stud = Student("Иван Иванов", "A12345")
print(stud.get_profile())