# everething were stored at memory
# lost when the program end
# file could be stored longer

# list - eveething will dissapeared when program exit

# collect student name
# name = input("What's your name?: ")
# print(f"Hello, {name}")

# accumulate some amount of information
names = []
for _ in range(3):
    # could be without variable
    name = input("What's your name?: ")
    names.append(name)

# print sorted list
for name in sorted(names):
    print(f"Hello, {name}")

# all information lost after exit()

