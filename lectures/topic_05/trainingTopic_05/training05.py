# do we realy need to ask input
# access to command line
# module sys
# https://docs.python.org/3/library/sys.html
# sys.argv - list of all the word at the prompt before Enter

from sys import argv
from sys import exit

print("argv list: ")
print(argv)
print("argv by items: ")
for item in argv[1:]: # slice of the list
    print(item)
print("try block")


try:
    a = int(argv[1])
    b = int(argv[2])
    result = a + b
    print(f"Operation result {result}")
except Exception:
    pass

# or using len function
if len(argv) < 2:
    print("Thare are no input parameters")
elif len(argv) > 2:
    print("There are a lot of parameters")
else:
    print("Correct list of parameters")

# "11 12" - one parameter

# using sys.exit
if len(argv) < 2:
    print("ex. Thare are no input parameters")
    exit("Error")
elif len(argv) > 2:
    print("There are a lot of parameters")

print("Correct list of parameters")



