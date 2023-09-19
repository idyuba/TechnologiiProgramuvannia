# lambda functions

students = []

with open("dump02.txt") as file:
    for line in file:
        name, mark = line.rstrip().split(",")
        student = {"name":name, "mark": mark}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"Name is {student['name']} mark is {student['mark']}") # braces