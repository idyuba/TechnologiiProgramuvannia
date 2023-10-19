# https://docs.python.org/3/library/functions.html#open

# with
'''
file = open("students.txt", "a")
name = input("What's is name: ")
file.write(f"{name}\n")
file.close()
'''

choise = input("Read(R) or Write(W):")

if choise == 'W':
    with open("students.txt", "a") as file:
        name = input("What's is name: ")
        file.write(f"{name}\n")
else:

    def sort_by_name(elem):
        return elem['name']
    
    def sort_by_mark(elem):
        return elem['mark']

    # names = ['Jon', 'Zak', 'Bob']
    # names = [{'name':Jon, 'mark':60}, {'name':Zak, 'mark':80}] 
    
    names = []
    with open("students.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            #print(line.rstrip().split(","))
            name, mark = line.rstrip().split(",")
            elem = {}
            elem['name'] = name
            elem['mark'] = mark
            names.append(elem)  
            
    for name in sorted(names, key=sort_by_mark):
        print(f"Your name is {name['name']} your mark is {name['mark']}")

        
