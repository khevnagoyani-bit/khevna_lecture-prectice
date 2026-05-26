# Hierarchical Inderitance

# Hierarchical Inderitance mean multiple child classes inherit from one parent class.

class Animal:
    def eat(self):
        print("Animal can eat")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meow")

d = Dog()
c = Cat()

d.eat()
d.bark()
c.eat()
c.meow()

# Hybrid Inheritance

# Hybrid Inheritance is a combination of multiple and diffrent multiplevcl inheritance.

class A:
    def show(self):
        print("class A")

class B(A):
    def show(self):
        print("class B")

class C(A):
    def show(self):
        print("class C")

class D(B,C):
    def display(self):
        super().show()

obj = D()

obj.display()

# super() follow  MRO(method Rsolution order)

# in class D(B,C) , python first check class B

# type() function

# the type() function returns the datatype of a varivable or object.

a = 10
b = 5.5
c = "python"

print(type(a))
print(type(b))
print(type(c))

# dir functions

# the dir() function lists all attributes and methods of class or object.

class student:
    def __init__(self):
        self.name = "Ramesh"

    def show(self):
        print("student Name :" , self.name)

obj = student()

print(dir(obj))
        
# isinstance() fuctions

# The isinstance function checks weather an object belongs to a class.

class person:
    pass

obj = person()

print(isinstance(obj , person))

# help() function

# the help() function display the documentation of a class or function.

class Demo():
    """This is s demo class"""

    def show(self):
        """This is method display message"""

help(Demo)





























