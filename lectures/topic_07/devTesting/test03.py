class Student:
    def __init__(self, name, mark):
        self.name = name 
        self.mark = mark
    
    def __str__(self):
        return f"Student name is {self.name} Mark {self.mark}"
    
    def nameToUpper(self):
        self.name = self.name.upper()
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, mark):
        if mark < 0:
            raise ValueError("Mark should not be less than 0")
        self._mark = mark


def get_student():
    name = input("What's name: ")
    mark = int(input("What's mark: "))
    student = Student(name, mark)
    return student

def main():
    student = get_student()
    student.nameToUpper()
    print(student)

main()