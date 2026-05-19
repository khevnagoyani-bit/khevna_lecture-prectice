# Opereator

# python opereator

# Arithmetic Operetors

'''
Addition
Substractiion
Multiplication
Division
Modulus
Expontiations
Floor Division
'''

# Examples

x = 10
y = 20

print(x + y)

print(x - y)

print(x * y)

print(x / y)

print(x ** y)

print(x // y)

# Comparision Operator

x = 20
y = 30

print(x == y)

print(x != y)

print(x < y)

print(x > y)

print(x <= y)

print(x >= y)

# Assignment Operetor

x = 10
y = 2

x = y

print(x)
print(y)

x += y

print(x)
print(y)

x -= y

print(x)
print(y)

x *= y

print(x)
print(y)

y /= x

print(x)
print(y)

x **= y

print(x)
print(y)

x //= y

print(x)
print(y)


# Logical Operator

# and,or,not

# and return true if both statement are true(x<5 and x>2)

# or return true if one of the statement is true.

# not Reverse the result

# chek if a number is even or odd

num = int(input("Enter a num:"))

if num %2 == 0: 
    print(f"{num} is an even num ")

else:
    print(f"{num} is an odd num")

# Find the minimum of two numbers

num1 = int(input("Enter first Number:"))
num2 = int(input("Enter secound Number:"))

if num1<num2:
    print(f"the minimum number is {num1}")
else :
    print(f"the maximum number is {num2}")

# find the largest of three number

num1 = int(input("Enter first number:"))
num2 = int(input("Enter secound number:"))
num3 = int(input("Enter third number:"))

if num >= num2 and num1>num3:
    print(f"the largest number is {num}")
elif num2>= num1 and num2>= num3:
    print(f"the largest number is {num2}")
else:
    print(f"the largest number is {num3}")
    

























