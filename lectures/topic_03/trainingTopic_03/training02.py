# for loop
# before start learn for loop lets talk about list

# list - type of data, containing different values
# for allows to iterate over the list of items

# less work than while
# explicitly specify i
# variable i will be created and will be updated each time
for i in [0, 1, 2]:
    print("bark")

# purly designed and not best case 
# what about a lot of things for i

#better way
# using range

for i in range(3):
    print("bark")

# some pythonik think
# do not need variable itself
for _ in range(3):
    print("bark")

print("bark" * 3) # barkbarkbark
print("bark\n" * 3, end="") # last back slash extra






