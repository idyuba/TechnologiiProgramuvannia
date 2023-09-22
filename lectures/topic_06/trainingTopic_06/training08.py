# lambda functions

students = []

with open("_input06.txt") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        student = {"name":name, "age": age}
        students.append(student)

for student in sorted(students, key=lambda student: student["age"]):
    print(f"Name is {student['name']} age is {student['age']}") # braces