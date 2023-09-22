# using csv modules
#https://docs.python.org/3/library/csv.html

import csv

students = []

with open("_input06.txt") as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        students.append({"name":row[0], "age":row[1]})

def get_name(student):
    return student["name"]

def get_age(student):
    return student["age"]

for student in sorted(students, key=get_age):
    print(f"Name is {student['name']} age is {student['age']}") # braces

