students = []

with open("_input06.txt") as file:
    for line in file:
        name, age = line.rstrip().split(",")
        # dict
        student = {} # name and mark
        student["name"] = name
        student["age"] = age
        students.append(student)

print(students)

def get_name(student):
    return student["name"]

def get_age(student):
    return student["age"]

# we can't sort dict
# need to tell sorted function how to sort
# passing function as argument ito function
# https://docs.python.org/3/library/functions.html#sorted
for student in sorted(students, key=get_age):
    print(f"Name is {student['name']} age is {student['age']}") # braces