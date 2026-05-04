# Pythin collection

print ("=======python collection datatype========")

# ------------List-----------

print ("list example")

my_list = [10,20,30]

print (" original list:", my_list)

# Mutability

my_list[0] = 100

print ("after mutability list :", my_list)

# Append ()

my_list.append(50)

print ("After use buill - in function list :", my_list)

# Max() and min ()

print ("max:", max(my_list))
print ("min:", min(my_list))

# Remove duplicates menually

list1= []
for i in my_list:
    if i not in list1:
        list1.append(i)
print("uniqe list :", list1)

#-------Tuple---------

print(" tuple examples")

my_tuple = (1,2,3,4)

print("tuple :", my_tuple)

# Immutable

# Count occurrence

print ("count of 2:" , my_tuple.count(2))

# Swapping using tuple

a,b = 10,20
a,b =b,a

print ( "Value:" , a,b)

# --------Set--------

print ("set example")

dataset = [ 1,2,3,4,5,6]

setdata = set(dataset)

print("set values:",setdata)

# Set operator

a={1,2,3}
b={3,4,5}

print(" union :", a|b)

# ----------Dictionary example")

student = {
    "name":"khevna",
    "marks":85
    }

print ("student:" , student)

student["marks"] =90

print (" updeted student :", student)

# Throught loop create dictionary

for key,value in student.items():
    print("key:", value)


# Find topper

students = {"A":80, "B":95,"C":70 ,"D":45}

topper = max (students,key = students.get)

print ("topper:",topper)

# ---------List comprehension---------

print("list comprehension examples:")

numbers = [ i for i in range(5)]

print("numbers:", numbers)

even =[i for i in range (10) if i % 2]

print ("even number :", even)

# -------Type casting------

print("type casting examples:")

t = (1,2,3)

list_1 = list (t)

print ("list :", list_1)

l = [1,2,3]

t_1 = tuple(l)

print ("tuple:", t_1)
