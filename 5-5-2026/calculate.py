# Write a recursive function to calculate of a give number


# ensure the program handiles edge cases (eg.negative inputs)

def factorial (n) :
    if n<0:
        return "invalid value"
    elif n == 0 or n==1:
        return 1
    else:
        return n* factorial (n-1)

print (factorial (5))
print (factorial (10))


# implement a recursive functionto calculate the fiboncci number.

# test the function with various inputs

def fibonacci(n):
    if n< 1:
        return n
    return fibonacci (n-1) + fibonacci(n-2)

print(fibonacci(6))

# Develop a program using recursion to reverse a string

def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print (reverse_string ("hello"))

# write a recursive function to find the sum of all digits of a given numbers until a single_digit number

def sum_digit(n):
    if n<10:
        return n
    return n%10 + sum_digit (n//10)


print (sum_digit(123456))
