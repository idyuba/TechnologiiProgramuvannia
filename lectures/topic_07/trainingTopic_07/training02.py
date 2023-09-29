# https://docs.python.org/3/tutorial/classes.html

class Student:
    ...


def get_student():
    # comman syntax of instantiation
    student = Student() # name could be different
    # student["name"] 
    student.name = input("Name: ")
    student.house = input("House: ")
    return student

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")