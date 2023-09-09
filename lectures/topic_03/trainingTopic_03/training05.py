# list of the student

students = ["Ihor", "Dima", "Serge"]
print(students) 

# want to print in some other way
print(students[0])
print(students[1])
print(students[2])

# use for to iterate over the list
for name in students:
    print(name)

print(len(students))
for i in range(len(students)):
    print(students[i])


# list functions
# extend()
# append()
# insert(id, val)
# remove(val)
# clear()
list_num = ["1", "2", "3"]
print(list_num)
list_str = ["aa", "bb", "cc"]
print(list_str)
list_str.extend(list_num)
print(list_str)

list_str.append("qwqw")
print(list_str)

list_str.insert(1, "cat")
print(list_str)

list_str.remove("cc")
print(list_str)

list_str.pop()
print(list_str)

#is present
print(list_str.index("cat"))
print(list_str.index("bb"))

list_str.sort()
print(list_str)

list_str.reverse()
print(list_str)




