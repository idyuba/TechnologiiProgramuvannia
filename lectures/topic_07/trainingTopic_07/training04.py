# https://docs.python.org/3/tutorial/classes.html

class Student:
    def __init__(self, name, house): # self using bu design
        # customize object
        if not name:
            # what to do ?
            raise ValueError("Missing name")
        if house not in ["aaa", "bbb", "ccc"]:
            raise ValueError("Wrong house")
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    def house(self):
        self.house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

def main():
    student = get_student()
    student.house = "ZZZ1" # overriding 
    print(student)


main()