import csv

def sort_by_name(elem):
    return elem['name']

def sort_by_mark(elem):
    return elem['mark']

names = []

with open("students.txt", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append({"name":row["Name"], "mark":row["Mark"]})

for name in sorted(names, key=sort_by_mark):
    print(f"Your name is {name['name']} your mark is {name['mark']}")