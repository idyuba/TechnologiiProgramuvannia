# write csv

import csv
name = input("Name?: ")
mark = input("MArk?: ")

'''
with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, mark])
'''
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "mark"])
    writer.writerow({"name":name, "mark":mark})