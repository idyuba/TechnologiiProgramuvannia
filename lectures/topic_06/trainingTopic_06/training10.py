# include very first row as name,mark
# dict reader


import csv

students = []

with open("_input06_dict.txt") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        students.append({"name":row["Name"], "age":row["Age"]})
print(students)

def get_name(student):
    return student["name"]

def get_age(student):
    return student["age"]

for student in sorted(students, key=get_age):
    print(f"Name is {student['name']} age is {student['age']}") # braces

