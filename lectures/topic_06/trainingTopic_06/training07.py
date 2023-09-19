students = []

with open("dump02.txt") as file:
    for line in file:
        name, mark = line.rstrip().split(",")
        # dict
        student = {} # name and mark
        student["name"] = name
        student["mark"] = mark
        students.append(student)

print(students)

def get_name(student):
    return student["name"]

def get_mark(student):
    return student["mark"]

# we can't sort dict
# need to tell sorted function how to sort
# passing function as argument ito function
for student in sorted(students, key=get_mark):
    print(f"Name is {student['name']} mark is {student['mark']}") # braces