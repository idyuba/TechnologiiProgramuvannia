# write csv

import csv

Students = [
    {'name': 'Ihor', 'age': '37'}, 
    {'name': 'Jon', 'age': '44'}, 
    {'name': 'Zak', 'age': '27'}, 
    {'name': 'Fink', 'age': '57'}
]

print(Students)
'''
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, mark])
'''
with open("students.csv", "w", newline='') as csvfile:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    writer.writerow({'Name': 'Ihor', 'Age': '37'})
    writer.writerow({'Name': 'Jon', 'Age': '44'})
    writer.writerow({'Name': 'Zak', 'Age': '27'})
