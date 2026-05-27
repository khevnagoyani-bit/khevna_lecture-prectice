# Polymprphism in python

#  Polymprphism mean "many forms" in object - oriented programming(OOP)

#  Polymprphism allows the same method name to perform diffrent task depending on the object or argument used.

# Method Overloading
# Method Overriding

# It also provide built - in functions

# issubclass()
# super()

# 1.  Method Overloading

# method overloading mean creating multiple methods with the same name but with diffrent parameter.

class calculator:
    def multiply(self,a,b,c = 1):
        return a * b *c

# object

calc = calculator()

print("Multiplication of 2 Numbers:" , calc.multiply(2,4))

print("Multiplication of 3 Numbers:" , calc.multiply(2,4,3))

# If only 2 arguments are passed , c takes defaut value 1.

# If 3 arguments are passed , all values are multiplied.

# same method name multiply() perform diffrent operations.

# 2.  Method Overriding

# method overriding occurs when a child class provides a specific implementation of a method already defiend in the parent class.

class Animal:

    def speak(self):
        print("Animal makes a sound")

class Dog (Animal):

    def Speak(self):
        print(" Dog barks")

class Cat(Animal):

    def Speak(self):
        print("cat meow")

# object

a = Animal()
d = Dog()
c = Cat()

c.speak()
d.speak()
c.speak()

# Dog and Cat inherite from animal

# Both child classes override the speak() method.

# issubclass() function

#  issubclass() is a built - in python function used to check weather one class is derived from another class.

# syntax issubclass( child_class) , (parent_class)

# It's return

# True --> if inheritance exists
# False --> otherwise
class person:
    pass

class student(person):
    pass

issubclass(student,person)
# student inerites from person

print(issubclass(student , person))

# polymorphism in function

def add(a,b):
    return a + b

print ("Addition of integers:" , add(10,20))

print("Concatenation of string : " , add (" Hello" , " word"))

