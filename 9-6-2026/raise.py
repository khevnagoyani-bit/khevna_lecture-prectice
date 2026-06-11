# raise keyword

'''
The raise keyword is used to manually trigger an exception in python.

it allows developers to stop program execution when an error condition occurs.
'''

# syntax

# raise exceptiontype("Error meassage")
'''
age = -5

if age < 0 :
    raise ValueError("Age cannot be nagative")
'''

# assert keyword in python

'''
The assert keyword is used for debugging and testing conditions.

it check weather a condition is True.

if the condition is true -> program continue.

if the condition is false -> AssertionError is raised.
'''

# Syntax

# assert condition , "Error meassage"
'''
num = 10

assert num > 0 , "Number must be Positive."

print("valid number")
'''
# custom exception with try-except
'''
class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1500

try:
    if withdraw > balance:
        raise InsufficientBalanceError("not enough balance")
    print("withdrwal successfull.")

except InsufficientBalanceError as e :
    print("Error :" , e)
'''
# 1. check even number using type error and value Error
'''
def check_even():
    num = int(input("Enter an integer:"))

    if not isinstance(num , int):
        raise TypeError("Input must be an integer")
    if num %2 != 0:
        raise ValueError("Number is odd")
    print("Number is even")

try:
    check_even()

except ValueError:
    print("Enter value must be only numbers")

except Exception as e:
    print("Error :" , e)
'''
# student grade validation
'''
class InvalidGradeError(Exception):
    pass

try:
    grade = int(input("Enter grade:"))

    assert grade != "" , "Grade input cannot be empty."

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be betwon 0 to 100")

    if grade < 40:
        raise InValidGradeError("student has faild")

    print("student passed.")

except AssertionError as e:
    print("AssertionError :" , e)

except ValueError as e:
    print("ValueError :" , e)
except InvalidGradeError as e:
    print("InvalidGradeError :" , e)

'''
# Temperature conversion validation

class HighTemperatureError(Exception):
    pass

try:
    temp = float(input("Enter temperacture in celsius:"))

    if not isinstance(temp , (int , float)):
        raise TypeError("Temperature must be a number")

    assert -273 <=temp <= 10000,"Temperature out of valid range."

    if temp > 1000:
        raise HighTemperatureError("Temperature exceed 1000 C")

    print("Valid Temperature :" , temp , "C")

except TypeError as e:
    print("TypeError : " , e)

except AssertionError as e:
    print("AssertionError : " , e)

except HighTemperatureError as e:
    print("HighTemperatureError : " , e)
    
# try...except handeling

print("Division Program")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# handle exceptions

def check_palindrome(s):
    assert s != "", "Error: Input string cannot be empty."

    if s == s[::-1]:
        print(f'"{s}" is a palindrome.')
    else:
        print(f'"{s}" is not a palindrome.')


check_palindrome("madam")
check_palindrome("hello")

#handle exceptions for invalid input

class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if '@' not in email or not (email.endswith('.com') or email.endswith('.org')):
        raise InvalidEmailError("Invalid email address.")

    print("Valid email address.")

# Valid email
try:
    validate_email("user@gmail.com")
except InvalidEmailError as e:
    print(e)

# Invalid email
try:
    validate_email("usergmail")
except InvalidEmailError as e:
    print("Error:", e)
