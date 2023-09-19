name = input("What's your name?: ")
with open("dump02.txt", "a") as file:
    file.write(f"{name}\n")