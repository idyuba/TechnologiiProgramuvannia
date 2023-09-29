# https://docs.python.org/3/tutorial/classes.html

class Student:
    def __init__(self, name, house, phone): # self using bu design
        # customize object
        if not name:
            # what to do ?
            raise ValueError("Missing name")
        if house not in ["aaa", "bbb", "ccc"]:
            raise ValueError("Wrong house")
        self.name = name
        self.house = house
        self.phone = phone
    
    def __str__(self):
        # return ">> a student " 
        return f"{self.name} from {self.house} phone {self.phone}"

    ## need more functionality
    def nameToUpper(self):
        self.name = self.name.upper()


def get_student():
    name = input("Name: ")
    house = input("House: ")
    phone = input("Phone: ")
    # student = Student(name, house) # some check could be perfomed, valid of data
    # return student
    return Student(name, house, phone)

def main():
    student = get_student()
    # print(f"{student.name} from {student.house}")
    print(student)
    student.nameToUpper()
    print(student)



main()