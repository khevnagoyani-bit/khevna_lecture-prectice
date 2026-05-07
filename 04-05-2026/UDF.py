# Built - Inn Function vs User Defined Functions (UDF)

# Bulit - in functions

numbers = [10,20,30,40]

print ("length :", len (numbers))

print ("maximum :", max (numbers))

print ("minimun :", min (numbers))

# These are per-defined inside python you don't need to carate them

# Use - defined functions

def greet (name) :
    return "hello" + name

print ( greet(" khevna"))
print ( greet (" krisha"))

# you define these function using def

# Arbitratry argument

# When number of inputs is unkown

def add_numbers(*args):
    total = 0
    for num in args:
        total = num
    return total

print(add_numbers(1,2,3))

print (add_numbers(1,2,3,4,5))

# keywords arguments (**kwargs)

# when passinf named value

def student_info(**kwargs):
    for key , value in kwargs.items():
        print(key,":", value)


student_info(name = "khevna" , age = 17 , course = "python")
    
# ** kwarge stores data in adictionary

# doc(documentation string)

# used to describe funtions

def multiply(a,b):
    """this function return the multiplication of two numbers"""

print (multiply(5,3))

print (multiply.__doc__)
