# read from file 
# r should be used but could check with w
with open("dump02.txt", "r") as file:
    # read all lines
    lines = file.readlines()

for line in lines:
    print(f"hello, {line.rstrip()}") # always add new line


with open("dump02.txt", "r") as file:
    for line in file:
        print(f"hello, {line.rstrip()}")