# Default Destructor in Python

# A special method automatically called when an object is destroyed.

# __del__()

# Purpose of Destructor

'''
1. Release memory
2. Close files
3. Disconnect database
4. Clean resources
'''
class Demo:
    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor called")


d = Demo()

del d

class FileManager:

        def __init__(self , filename):
            self.file = open(filename , "w")

        def write_data(self):
            self.file.write("Hello")

        def __del__(self):

            self.file.close()
            print("File closed")

f = FileManager("demo.txt")

f.write_data()

del f
# Constructor vs Destructor
# Method :  __init__()  /  __del__()
# initialize object /  Clenup Object
# During Object creation / During Object destrction

class Bank:

    def __init__(self , name , balance):
        self.__name=  name
        self.__balance = balance

    def deposit(self , amount):
        self.__balance += amount

    def withdraw(self , amount):
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __del__(self):
        print("Account Closed")

b = Bank ("Rahul"  , 10000)

b.deposit(5000)

b.withdraw(10000)

print(b.get_balance())

del b

# Encapsulations =  Data Protection + Controlled Access

# Constructor

# Object creation ->  __init__()

# Destructor

# Object Deletion -> __del__()


# Python Inheritance

# Inheritance allows one class to acquire the properties and methods of another class

# code reusability
# Improve readability
# Supports hierarchical classification

# Single Inheritance

# single inheritance means one child class inherits from one parent class.

# pass

# Null Statement (does nothing)

class Parent:

    def display(self):
        print("This is Parent Class method")

class Child(Parent):

    pass

obj = Child()

obj.display()

# # Multiple Inheritance

# Multiple inheritance means one child class inherits from more than one parent class.

class Teacher:

    def teach(self):
        print("Teaching students")


class Administrator:

    def manage(self):
        print("Managing school")

class Headmaster (Teacher , Administrator):

    pass
h = Headmaster()

h.manage()

# Multilevel Inheritance

# Multiple inheritance means a class inherits from another child class.

class Grandparent:

    def role1(self):
        print("I am Grandparent")

class Parent(Grandparent):

    def role2(self):
        print("I am Parent")

class Child(Parent):

    def role3(self):
        print("I am Child")

c = Child()

c.role1()
c.role2()
c.role3()
