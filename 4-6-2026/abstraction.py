# Abstraction in loop

# Abstraction is the process of hiding implemention datails and showing only essential features to the user.

# Reduce complexity
# Increase security
# Improve code reusability

# An abstraction class is a class that cannot be instantied (object cannot be created diretly)

# 1. abc
#Abstraction Base class

# it is built-in python module used to create abstract classes.

'''
class shape(ABC)

ABC is a helper class used to make a class abstract'
'''

from abc import ABC ,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Dog Bow Bow")
        
d = Dog()

# You cannot create an object of an abstract class.

# Abstract class and method

from abc import ABC,abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound (self):
        pass

    def sleep(self):
        print("Animal is sleeping")

# child class

class Dog(Animal):

    def sound(self):
        print("Dog Bow Bow")

class Cat(Animal):

    def sound(self):
        print("Cat Mew")

d = Dog()

d.sound()
d.sleep()

c = Cat()

c.sound()
c.sleep()

# Abstract class shape wuth area()

from abc import ABC , abstractmethod

# Abstract classs

class shape(ABC):

    @abstractmethod

    def area(self):
        pass

class Rectangle(shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

class Circle(shape):

    def __init__(self,radius):
        self.radius = radius

        
    def area(self):
        return 3.14*self.radius*self.radius

r = Rectangle(10,5)
c = Circle(10)

print("Rectangle area:" , r.area())
print("Circle area:" , c.area())

# Add Perimeter() method

from abc import ABC , abstractmethod

class shape():

    @abstractmethod
    def area(self):
        pass

class Rectangle(shape):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length*self.width

    def Perameter(self):
        return 2*(self.length*self.width)

class Circle(shape):

    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

    def Perameter(self):
        return round (2*3.14*self.radius,3)

r = Rectangle(10,5)
c = Circle(10)

print("Rectangle area :" , r.area())
print("Circle area :" , c.area())

# ML Modal Abstract class

from abc import ABC , abstractmethod

class MLModal(ABC):

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

# LinearRegressionModal

class LinearRegressionModal(MLModal):

    def train(self):
        print("Training Linear Regression Modal.")

    def predict(self):
        print("predicting using Linear Regression.")

class DecisionTreeModal(MLModal):

    def train(self):

        print("Training Decision Tree Modal.")

    def predict(self):

        print("Predicting using Decision Tree.")

l = LinearRegressionModal()
d = DecisionTreeModal()

l.train()
l.predict()

d.train()
d.predict()
