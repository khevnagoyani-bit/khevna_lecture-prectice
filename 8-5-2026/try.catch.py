# Exception handling in python

# An Exception is an error that occurs during program execution if an exception is not handled the program stop immidiately.

# to avoid program crashes , python provides exception handeling using.

'''
try
catch
else
finally
'''

# 1. try.........except

# used to handle errors sapley

# syntax:
'''
try:
    # code block
except:
    # error handeling code
'''

try:
    num = int(input("Enter number:"))
    print(10 / num)

except ZeroDivisionError:
    print("cannot divide by Zero")

except valueError:
    print("Invalid input")

# try -> contains risky code
# except -> runs if error occurs

# 2. try......except.......else

# syntax
'''
try:
    #code block
except:
    #Error Handeling
else:
    #execcutes if no error
'''
try:
    num = int(input("Enter Number:"))
    result = 10 / num

except ZeroDivisionError:
    print("cannot devide by Zero")

else:
    print("Result :" , result * 10)

# 3. try.......except........finally

# finally block always excutes weather error eccur or not.

# syntax
'''
try:
except:
finally:
'''

try:
    file = open("demo.txt" , "r")

    print(file.read())
    
except FileNoteFoundError:
    print("file not found")

finally:
    print("program finished.")

# 4. try......except......else.....finally

# combination of all blocks.

try:
    num = int(input("Enter number:"))
    result = 10 / num

except ZeroDivisionError:
    print("cannot devided by zero")

else:
    print("result : " , result)

finally:
    print("program finished:")


# Important exception types in python
'''
1. ZeroDivisionError
2. ValueError
3. TypeError
4. IndexError
5. KeyError
6. FileNoteFoundError
'''


# prevent program crash
# Improve program reliability
# make debugging easier
# Handles unexpected error gracefully

try:
    atm_pin = int(input("Enter ATM PIN:"))

except ValueError:
    print("PIN must contain numbers only")

else:
    print("PIN accepted")

# program

# 1. Divide to numbers using try.....except

try:
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Secound Number:"))
    result = num1 / num2
    print("result :" , result)

except ZeroDivisionError:
    print("cannot devided by zero")

# 2. handeling list index error

try:
    numbers = [10,20,30,40,50,60]
    index = int(input("Enter index number:"))
    print("Element :" , numbers[index])

except IndexError:
    print("Index dose not exist")

# 3. Read file using try.....except......else

try:
    filename = input("Enter filename:")
    file = open(filename , "r")

except FileNotFoundError:
    print("file not found")

else:
    print("file content")
    print(file.read())

    file.colse()

# 4. handeling string index error using else

try:
    text = "python"
    
    index = int(input("Enter index number:"))

    result = text[index]

except IndexError:

    print("Index dose not exist")

except IndexError:

    print("Index dose not exist")

else:
    print("character :" , result)

# 5. handling exceptions file dosen't exist

try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("Error: File does not exist.")

finally:
    try:
        file.close()
        print("File closed successfully.")
    except:
        print("No file to close.")

# 6. handling invalid input and ensure

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ValueError:
    print("Invalid input! Please enter numbers only.")

except ZeroDivisionError:
    print("Error! Division by zero is not allowed.")

finally:
    print("Program execution completed.")

# 7. handling input

import math

try:
    num = float(input("Enter a number: "))

    if num < 0:
        raise ValueError("Negative numbers are not allowed.")

except ValueError as e:
    print("Error:", e)

else:
    print("Square root =", math.sqrt(num))

finally:
    print("Execution complete.")
