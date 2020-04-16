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
