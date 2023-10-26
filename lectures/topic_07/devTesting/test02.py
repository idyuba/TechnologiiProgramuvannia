class Student:
    ...

def get_student():
    student = Student()
    student.name = input("What's name: ")
    student.mark = int(input("What's mark: "))
    return student

def main():
    student = get_student()
    print(f"Student name is {student.name} Mark {student.mark}")

main()