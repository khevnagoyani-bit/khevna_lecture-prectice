# Python Mutable and Immutable Data Type

# In Python , every Value is stored as an object.

# Mutable object : Can be change after creation

# concept

'''
1.Momery Mangement
2.Variable behavior
3.Function argument
4.Performance
5.Debugging
6.Learing objectives
'''
# Everyting is python is an object.

x = 10
name = "python"
numbers = [1,2,3,4]

print(x)
print(name)
print(numbers)

# Each object has : value , type , memors address

# We can check memory location using : id() built - in function

x = 10
y = 12

print(id(x))
print(id(y))

# common Immutable Types

'''
int 10
float 10.5
complex 2 + 3 j
bool true
str "Hello"
frozenset frozenset({1,2})
bytes "abcd"
tuple(1,2,3)
'''

# Int

x = 10

print("Before:" , id(x))

x = x +1

print("After:" , id(x))

# string

name = "python"

# name[0] = "j"

# common Mutable Types

'''
list [ 1,2,3]
dict {"a" : 1}
set {1,2,3,}
bytearry bytearry(5)
'''
'''
# Mutable List

numbers = [ 1,2,3,4,5]

print("Before :" , numbers)

print("before Id :" , id(numbers))

# Mutable Dictionary

students = {
    "name" : "khevna",
    "age" : 16
    }

students["age"] = 17

print(students)

# String

a_str = "Hello World"

print(a_str)
print(a_str[4])
print(a_str[0:5])
print(a_str[6:11])

# set dta types

# set - they are mutable and new element can be added once sets are defiend

basket = { 'apple' , 'banana' , 'orange' , 'pear' , 'kiwi' }

print(basket)

a = set('abcdefghijk')
b = set('abchjffuwb')

print(a)
print(b)
'''
'''
# In a user - defiend array (by taking input):

arr = []

size = int(input("Enter array size:"))

for i in range(size):
    value = int(input(f" a [{i}] = "))
    arr.append(value)


print("Even numbers are:")

for i in arr:
    if i % 2 == 0:
        print(i)

print("odd numbers are:")

for i in arr:
    if i % 2 != 0:
        print(i)
'''
'''
# first five elements and alternamte element

arr = []

size = int(input("enter array size:"))

for i in range(size):
    value=int(input("Enter element:"))
    arr.append(value)
for i in range(5):
    print(arr[i])

print("first five elements:")


''''
# first , last and middle element

arr = []

size = int(input("enter array size:"))

for i in range (size):
        value=int(input("Enter Element:"))
        arr.append(value)

print("first element:" , arr[0])

print("last element:" , arr[-1])

middle = size // 2

print("middle element:" , arr[middle])
        















