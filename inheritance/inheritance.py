class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def print_name(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduation_year = year


x = Person("John", "Doe")
x.print_name()

y = Student("Alexandra", "Gastani Frinzi", 2019)
y.print_name()
