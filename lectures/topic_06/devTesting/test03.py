import csv

def sort_by_name(elem):
    return elem['name']

def sort_by_mark(elem):
    return elem['mark']

names = []

with open("students.txt", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        names.append({'name':row[0], 'mark':row[1]})

# lambda functions    
for name in sorted(names, key=sort_by_mark):
    print(f"Your name is {name['name']} your mark is {name['mark']}")
