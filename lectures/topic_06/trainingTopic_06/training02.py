name = input("What's your name?: ")

# https://docs.python.org/3/library/functions.html#open
# file = open("dump02.txt", "w") # rewrite each time
file = open("dump02.txt", "a") # all in one line
# file.write(name)
file.write(f"{name}\n")
file.close()