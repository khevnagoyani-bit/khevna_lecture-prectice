# create a list of dictionaries to store student records

# ======= Initial Data =======

students = [{"id": 101 , "name" : "Alic" , "score" : 85},
    {"id": 102 , "name" : "Bob" , "score" : 78},
    {"id": 103 , "name" : "Charile" , "score" : 92}
            ]

# print the name of each student using a loop

print("Student Names:")

for s in students:
    print(s["name"])

# print the average score of all students

total = 0

for student in students:
    total+= student["score"] # total = total+84 total = 0+85 total =85
                        # total = total+78 total = 85+78 total =163
    avg = total / len(students)   # total = total+92 total = 163+92 total =255/3

print ("\n Average score : " , avg)

# Add a new student record to the list

students.append({"id": 104 , "name" : " jhon" , "score" : 75})


# Update the score of a student with ID 102 to 88

for s in students:
    if s["id"] == 102:
        s["score"] = 88

print ("\n students list :", students)

# Delete the record of the student named "charlie"

new_list = []
for s in students :
    if s ["name"] != " charlie":
        new_list.append(s)

students = new_list

print ("\n students list :" , student)

# print names of students scored more than 80

print ("\n student scoring more than 80:")

for s in students :
    if s ["score"] >80:
        print (s["name"])

# sort the list of students by score (descending)

def get_score (student):
    return student ["score"]

students.sort(key = get_score, reverse = True)

print ("\n sorted by score (dese):")

for s in students:
    print(s)

# find the student with the highest score

max_score = max (student ["score"] for student in students)

top_student = [s for s in students if s ["score"] == max_score]

print ("\n\n top_student :" , top_student)
'''
# Use loop to create a report in this format :
    - name: aice| score:85 | grade :B
        (Add grading logic : A = 90 +, B = 80-89, C=<80)
'''

print ("student Report:")

def get_report(score):

    if score>=90:
        return "A"
    elif score >=80 :
        return "B"
    else:
        return"C"

for s in students:
    grade = get_report (s["score"])
    print ("name:" , s [ "name"] , "| score :" , s [ "score"] , "| grade:" , grade)

# count how many students 90 + each grade

grade_count = { "A":0 ,"B":0 ,"C":0}

for s in students:
    grade = get_report(s["score"])
    grade_count [grade]+=1

print ("\n grade count :" , grade_count)

# convert the list of dictionaries into a pandas dataframe
'''
import pandas as pd

print (pd.__version__)
'''
