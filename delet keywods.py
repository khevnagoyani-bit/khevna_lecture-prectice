# Delete Keyword

print ("\n DELETE EXAMPLE")

list_1 = [10,20,30,40]

print (" before delete:", list_1)

del list_1[1]

print (" after delete:",list_1)

del list_1[2]

print ("after deleting index:", list_1)

# Delete dictionary key

dict_1 ={"a":1 ,"b":2}

del dict_1["a"]

print ("Disctionary aftere delete:", dict_1)

# Small program

print ("\n small program")

students = ["khevna" , "rutva" , "kevanshi" , "vruti" , "krisha" , "grisa" ]

unique_students = list (set(students))

student_data ={name:len(name)for name in unique_students}

print ("student data:" , student_data)

# Create list , tuple,set and dict using user input

user_input = input ("enter element seperated by space:")

user_list = user_input.split()

print("user list", user_list)

user_tuple = tuple(user_list)

print("user tuple ", user_tuple)

user_set = set (user_tuple)

print("user set ", user_set)

user_dict = {i: value for i , value in enmerate ( user_list)}

print ("user set ", user_dict)

dict_input = input ("enter key :value pairs seprated by space:")

pairs = dict_input.split()

for item in pairs:
    key , value + item.split(":")
    my_dict[key] =value

print (" Disctionary : " , my_dict)
