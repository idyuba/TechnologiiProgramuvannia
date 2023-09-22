name = input("What's your name?: ")

# https://docs.python.org/3/library/functions.html#open
# file = open("_output02.txt", "w") # rewrite each time
file = open("_output02.txt", "a") # all in one line
# file.write(name)
file.write(f"{name}\n")
file.close()