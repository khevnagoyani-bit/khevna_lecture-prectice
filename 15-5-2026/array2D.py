# python lecture topic : 2D array with list

# Array inside another array

# Stoers Data : rows , columns

# It loks like a table or matrix.

# Example.

arr1 = [1,2,3,4,5,6]

arr2 = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]

print(arr1)
print(arr2)

# Accessing Elements in 2D Array

# Syntax : array[row][column]

print(arr1[0])
print(arr2[1][0])
print(arr2[2][2])

# Taking Input in 2D Array

arr = []

rows = int(input("Enter rows:"))
cols = int(input("Enter colums:"))

for i in range(cols):
    row = []
    for j in range(cols):
        value = int(input(f" arr[{i}] [{j}] = "))
        row.append(value)
    arr.append(row)

print(arr)

# Printing 2D Array using Nested Loop

arr = [
    [1,2],
    [3,4]
    ]

for i in arr:
    for j in i:
        print(j , end = " " )
    print()

# Sum Of All Elements in 2D Array

arr = [
    [1,2,3],
    [4,5,6]
    ]

total = 0

for i in arr :
    for j in i:
        total += j

print("total:",total)

# sorting collection datatypes

# sorting mean :arranging data in order

# type : 1.Ascending
#        2.Descending

# syntax = list.sort()

numbers = [5,8,2,7,9,1]

numbers.sort()

print(numbers)

# sorting in string

fruits = ["mango" , "banana" , "apple" , "kiwi"]

fruits.sort()

print(fruits)
