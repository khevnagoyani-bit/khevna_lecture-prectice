# Set With Delete Keyword

'''
variable
Objected
Entire Set

'''
'''
Colours = {"red", "bule", "pink"}

print (colours)

del colours

print (colours)
'''

numbers = {1,2,3,4}

print (numbers)

# Remove ()

numbers.remove(2)

print (numbers)

# Discard ()

numbers.discard(4)

print (numbers)

# pop ()

numbers.pop()

print(numbers)

# Convert two list into dictonary using zip

keys = ["name" , "age", "city"]

values = [ "alice" , 25 , "Ahemdabad"]

data = dict(zip(keys, values))

print (data)

# Pyton : functions , Recursion , Lambda functions , Global keyword and Multiple returnt value

# Function

# Function are reusable block of code used to perform a specific task.

# Resability , Cleaner code , Better organization , Reduse repetation

def greet ():
    print("welcome pyton students!")

greet()

# function with parameter

def add (a,b):
    print(a+ b)

add(10,20)

add(30,20)

# Recursion

# A Function calling it self.

# Factorial , tree structure , problem solving

# Base case , Recursive cal

# Factorial

def factorial (n):
    if n == 1:
        return 1
    return n*factorial (n-1)

print(factorial(5))

# Sum Of Numbers

def total(n):
    if n == 0:
        return 0
    return n +total (n-1)

print(total(10))

# Anonymous /Lambda function

# Lambda function:

# Small anonymous function

# written in one line

# no function name

# Syntax

# Lambda argument : expression

square = lambda x :x*x

print(square(5))

add = lambda a , b:a + b

print(add(10,20))

# List With lambda & map()

nums = [ 1,2,3,4,5,]

result = list (map(lambda x :x*2,nums))

print (result)

# List With Lambda and Filter ()

nums = [1,2,3,4,5,6]

odd = list (filter(lambda x :x%2!=0,nums))

print(odd)

# Global Keyword

# Variables creates outside function are called global variables

x=10

def show ():
    print(x)

show()

count =0

def increment():
    global count
    count += 1

increment()
increment()
increment()

print(count)

# Return multipale values

# Python function can return : single values, ultiple values

# multiple values are return as tuple

def calc(a , b):
    return a + b , a-b
result = calc(10,5)

print(result)

def students():
    name="Krishna"
    marks = 90
    return name , marks

result1 , result2 = students()

print(result1)
print(result2)

count = 10

def write(str):
    global count
    count+=1
    return str , count

print(write("hello python!!!"))
