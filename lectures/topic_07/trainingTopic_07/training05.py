# https://docs.python.org/3/tutorial/classes.html

# properties

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    # getter - get some atribute
    @property
    def house(self):
        return self._house
    
    # setter - set some value
    @house.setter
    def house(self, house):
        if house not in ["aaa", "bbb", "ccc"]:
            raise ValueError("Wrong house")
        self._house = house

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)

def main():
    student = get_student()
    # but !!!!
    student._house = "qwqwqwqww"
    print(student)


main()