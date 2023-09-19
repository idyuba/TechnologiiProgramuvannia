# using csv modules
#https://docs.python.org/3/library/csv.html

import csv

students = []

with open("dump02.txt") as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        students.append({"name":row[0], "mark":row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"Name is {student['name']} mark is {student['mark']}") # braces

