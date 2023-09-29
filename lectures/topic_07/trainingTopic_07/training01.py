# from procedure way to OOP

# tuple list dictionary for storing information about the student

'''
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
'''

'''
def main():
    name = get_name() # don't care about implementation
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    name = input("Name: ")
    return name

def get_house():
    house = input("House: ")
    return house
'''

'''
# requred one function to get student
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # need to return two value
    # dict could be use to return value
    # return name, house # return tuple could not be changed
    return [name, house] # return value could be changed
    
def main():
    # name, house = get_student()
    # print(f"{name} from {house}")
    student = get_student() # tuple could not be changed
    if student[0] == "qq":
        student[1] = "ss"
    print(f"{student[0]} from {student[1]}")
'''

def get_student():
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

# several data types were used
# but what about one data type wit name Student


def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")

if __name__ == "__main__":
    main()