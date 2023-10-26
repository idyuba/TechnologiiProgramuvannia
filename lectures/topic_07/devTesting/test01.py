
def get_student():
    name = input("What's name: ")
    mark = int(input("What's mark: "))
    return {"mark":mark, "name":name}

def main():
    student = get_student()
    print(f"Student name is {student['name']} Mark {student['mark']}")

main()