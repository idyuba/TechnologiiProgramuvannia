# include very first row as name,mark
# dict reader


import csv

students = []

with open("dump02.txt") as file:
    reader = csv.DictReader(file)
    for row in reader:
        #print(row)
        students.append({"name":row["Name"], "mark":row["Mark"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"Name is {student['name']} mark is {student['mark']}") # braces

