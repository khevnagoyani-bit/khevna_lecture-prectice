# Write  a Program to find the Length of a ID array without using buil - in function
'''
arr = []

size = int(input("Enter array size:"))
for i in range(size):
    value = int(input(f"a[{i}] = " ))
    arr.append(value)

count = 0

for i in arr :
    count += 1

print("Lenght of array :" , count)

print("original array :" , arr)
'''
'''
# Write a program to find average of a ID arry without using buil-in functoin

arr = []

size = int(input("Enter array size :"))

for i in range(size):
    value = int(input(f"a[{i}] = "))
    arr.append(value)

sum = 0
count = 0

for i in arr:
    sum += i
    count += 1
average = sum / count

print("Average of array :" , average)
'''
'''
# Write Program to Preform additionoperation of another array and store it in another array

arr1 = []
arr2 = []
result = []

size = int(input("Enter array size :"))

print("Enter arr1 Elements:")

for i in range(size):
    value = int(input(f" a[{i}] = "))
    arr1.append(value)

print("Enter arr2 Elements:")

for i in range(size):
    value = int(input(f" a[{i}] = "))
    arr2.append(value)

for i in range(size):
    result.append(arr1[i] + arr2[i])

print("Array Result = " , result)
'''
'''
# Create an array of numbers from 1 to 10

arr = []

for i in range(1,11):
    arr.append(i)

for i in arr:
    print(i*2)
'''
# Take user input for a number

arr = [ 10 , 20 ,30 ,40 , 50 , 60]

num = int(input("Enter number to search:"))

found = False

for i in range(len(arr)):
    if arr[i] == num :
        print("Element Index : " , i )
        found = True
        break

if found == False:
    print("not found Element.")
