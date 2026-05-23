# Encapsulation

# Constructor and destructor

# Encapsuation

# Binding data and methods together inside a class and restricting direct access to data.

# public members

# protected members

# private members


class Student:
    def __init__(self):
        self.__marks = 0

    def set_marks(self , m):
        self.__marks = m

    def get_marks(self):
        return self.__marks

s = Student()

s.set_marks(90)

print("Marks:" , s.get_marks())

# Protected Data
# Prevent Direct Modification
# Improve security and maintainability

# Access Specifiers

# Public

class Student:

    def __init__(self):
        self.name = "Rahul"

s = Student()

print(s.name)

# Protected

class Student:

    def __init__(self):
        self._marks = 85

class Result(Student):

    def show(self):
        print("Marks:" , self._marks)

r = Result()

r.show()

# Private

class BankAccount:

    def __init__(self):
        self.balance = 10000
b = BankAccount()

print(b.balance)

# Real - Life Analogy

# You cannot directly access money inside ATM hardware.

# PIN , withdraw , balance check

# constructor in python

# a special method automatically executed when an object is created.

# initialize variables

# Assign default value

# Execute setup code automatically

class Laptop:

    def __init__(self):
        print("laptop object created")

lap = Laptop()

# parameterized constructor

class Student:

    def __init__(self , name , age):
        self.name = name
        self.age = age

    def display(self):

        print("Name" , self.name)
        print("Age" , self.age)

s1 = Student("Aman" , 21)

s1.display()
