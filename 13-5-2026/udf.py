# All typr of python functions

# T - Take Argument
# N - No Argument
# R - Return Value
# N - No return value

'''
TNRN - take no argument, return no value
TSRS - take some argument, return no value
TNRS - take no argument, return some value
TSRS - take no argument, return some value
'''
# TNRN

def greet():
    print ("welcome python students!!!")

greet()

# TSRS

def add(a , b):
    print("addition = " , a + b)

add(10,20)

# TNRS

def message():
    return"Hello Python!!!"

print(message())

# TSRS
def multiply(x ,y):
    return x*y

print(multiply(5,4))

# Diagram
# Argument :TNRN
# Return : TNRS,TSRN
# both : TSRS
# Rrturn ends functions execution

def cala(a,b):
    return a+b , a-b

x,y = cala(10,5)

print(x)
print(y)

# 1D Arry in python
# in python a list is used to store multiple values in single variable
# Example

marks = [ 78, 52, 82, 24, 100]

print(marks)

# Accessing Elements
# Using Index

numbers = [ 1,2,3,4,5,6]

print(numbers[0])
print(numbers[2])

# Nagative Indexing

numbers = [ 1,2,3,4,5,6]

print(numbers[-1])
print(numbers[-2])

# Changing List Elements

numbers = [ 1,2,3,4,5,6]

numbers[1] = 20

print(numbers)

# List Traversing using loop

numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    print(i)

# Using range() with indexing

numbers = [1,2,3,4,5,6,7,8,9,10]

print("length of list:" , len(numbers))

for i in range(len(numbers)):
    print("index:" , i ,"value:" , numbers[i])

# Add Element at end of the list.

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.append(11)

print(numbers)

# insert() in List

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.insert(3,30)

print(numbers)

# Remove Elements

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.remove(10)

print(numbers)

# Remove Elements at end of the list

numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.pop()

print(numbers)

# Searching in List

numbers = [1,2,3,4,5,6,7,8,9,10]

if 2 in numbers:
    print("found")

# List Slicing

numbers = [1,2,3,4,5,6,7,8,9,10]

print(numbers[3:7])

# Sum of List Elements

numbers = [1,2,3,4,5,6,7,8,9,10]
'''
total = 0

for i in numbers:
    total +=i

print(total)
'''
total = sum(numbers)

print(total)































