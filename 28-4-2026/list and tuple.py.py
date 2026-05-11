# List and Tuple in python (basic & mutability)

# List - mutable

my_list = [10,20,30,"khevna"]

print ("list : ", my_list)

my_list [1] = 99

print ("list: ", my_list)

my_list [3] = 101

print ("list : " , my_list)

# Tuple - Immutable

my_tuple = (10,20,30)

print ("tuple :", my_tuple)

# String Formatting

# Indexing and Slicing

text = "python"

print ("first letter :", text [5])
print ("first letter :", text [-2])

# Slicing

print("first 3 letter :", text[0:3])
print("first 2 letter :", text[::3])

# Using List With Slicing and Formatting

students = [ "Grisa" , "Isha" , "kevanshi" , "khevna" , "krisha" , "vruti" ]

print ("first two students:", students [::2])

# String Formatting Useing List

for student in students:
    print (f"welcome , (student)")
