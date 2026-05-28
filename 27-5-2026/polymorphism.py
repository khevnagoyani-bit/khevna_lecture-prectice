# super() function

# super() is used to call method or constructor of the parent class from the child class.

class Employee:

    def __init__(self , name):
        self.name = name
        print("Employee Constructor Called.")

class Manager(Employee):

    def __init__(self , name , department):

        # calling parent constructor

        super().__init__(name)

        self.department = department

        print("Manager constructor called.")

    def display(self):
        print("Name:" , self.name)
        print("Department:" , self.department)

m = Manager("Akhil" , "HR")

m.display()

# Manager inherits from employee

# super class data is reused in child class.'

# polymorphishm in class inheritance.

class shape:
    def area(self):
        print("Area cacluction")

class Circle(shape):
    def __init__(self,redius):
        self.redius = redius

    def area(self):
        print("Area of circle: " , 3.14 * self.redius * self.redius)

class Rectangle(shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        print("Area of Rectangle :", self.length * self.width)

c = Circle(10)
r = Rectangle(5,10)

c.area()
r.area()

# Polymorphism with buli in function len()

# String

text = "python"

# list

numbers = [10 , 20 , 30 , 40 , 50 ,]


# dictionary

student = {"name" : "zeel" , "age" : 20}

print("Length of string:" , len(text))

print("Length of List:" , len(numbers))

print("Length of Disct:" , len(student))

# Polymorphism using transport interface

class Transport:
    def travel(self):
        print("Travel method")

class Train(Transport):
    def travel(self):
        print("Train travel on tracks.")

class plane(Transport):
    def travel(self):
        print("plane travel in air.")


t = Train()
p = plane()

t.travel()
p.travel()













