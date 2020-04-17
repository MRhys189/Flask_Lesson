import functools


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)


# class Student2:
#     def __init__(self, name):
#         self.name = "Rolf"
#         self.grades = self

#     def __str__(self):
#         return f"{self.name} is the name"

#     def average2(self):
#         return sum(self.grades) / len(self.grades)


student = Student("Bob", (90, 90, 93, 78, 90))
print(student.average())
print(student.grades)
print(student.name)

# class inheritance


class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining) "

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("HP", "USB", 500)
printer.print(20)
print(printer)
printer.disconnect()


# Type hinting

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name: str, book_type: str, weight: int):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    # returns a book object created by "Class Book"
    def hardcover(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> "Book":
        return cls(name, cls.TYPES[1], page_weight)

# errors


def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("The divisor cannot be 0")
    return dividend/divisor


grades = []
print("Welcome to the average grade program")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}")
except ZeroDivisionError as jah:
    print(jah)
    print("There are no grades yet in the system")


def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}")


Students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rhys", "grades": [85, 60]},
    {"name": "James", "grades": [40, 90]}
]


def get_student_name(stud):
    return stud["name"]


print(search(Students, "Rhys", get_student_name))


# decorators
user = {"username": "jose", "access_level": "guest"}


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == "admin":
                return func(*args, **kwargs)
            else:
                return f'No admin permissions for '

        return secure_function

    return decorator


@make_secure("admin")
def get_admin_password():
    return "1234"


@make_secure('guest')
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password.__name__)
# print(secure_get_admin())

# Students = [
#     {"name": "Bob", "grades": [75, 90]},
#     {"name": "Rhys", "grades": [85, 60]},
#     {"name": "James", "grades": [40, 90]}
# ]
# names = {"name": "Rhys Murage", "age": 55}


# def ex_fucn():
#     return "12345"


# def specific_name(func):
#     def specified():
#         if names["name"] == "Bob":
#             return func()
#         else:
#             return f"{names["name"]} is no the one"
#     return specified


# ex_fucn = specific_name(ex_fucn)
# print(ex_fucn())
