# Python OOP student logic

# class and object.

class car:
    comp_name = None
    model = None
    color = None
    year = None

car1 = car()
car2 = car()

car1.comp_name = "TATA"
car1.model = "Nexon"
car1.color = "pink"
car1.year = 2024

car2.com_name = "Audi"
car2.model = "R8"
car2.color = "Blue"
car2.year = 2026

print("car 1 Details")

print(car1.comp_name)

print(car1.model)

print(car1.color)

print(car1.year)

print("__________________________________")

print("car 2 Details")

print(car2.com_name)

print(car2.model)

print(car2.color)

print(car2.year)

# student

class studentData:
    std_name = None
    std_id = None
    std_age = None
    std_course = None

student1 = studentData()
student2 = studentData()

student1.std_name = "khevna"
student1.std_id = "7045"
student1.std_age = 17
student1.std_course = "AI / ML"

print("student 1 Details:")

print(student1.std_name)

print(student1.std_id)

print(student1.std_age)

print(student1.std_course)

class student:
    def studentData(self):
        name = input("Enter name :")
        age = int(input("Enter Age:"))
        course = input("Enter course:")

        print("\n student Details")

        print("Name :", name)

        print("Age :", age)

        print("course :" , course)

S1 = student()
S2 = student()
S1.studentData()
S2.studentData()

# concept

# class buleprint / template
# object real instance
# student() object creation

# self Keyword

# self refers to corrent object

class student:
    def setData(self , name , marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("name:" , self.name)
        print("marks:" , self.marks)

S1 = student()
S2 = student()

S1.setData ("Rahul" , 45)
S1.display()

S2.setData("ronak" , 26)
S2.display

# Delete Keyword

# Used for:

#delete varible
#delete object
#delete property

class student:
    def show(self):
        print("student object")

S1 = student()
S1show()

del S1 

class student:
    def setData(self):
        self.name = "Rahul"

S1 = student()
S1.setData()

print(S1.name)

del S1.name


# Encapsulation

# Hiding data from direct access.

# Security
# data protection

class student:
    def __init__(self):
     self.__marks = 90

    def showmarks(self):
            print("marks:" , self .__marks)

S1 = student()

S1.showmarks

























