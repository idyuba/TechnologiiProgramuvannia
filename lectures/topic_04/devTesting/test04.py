def getName():
    name = input("What is your name: ")
    if name != "Bob":
        raise NameError("Name must be only Bob")
    return name

while True:
    try:
        Name = getName()
        break
    except NameError:
        pass

print(f"was entered {Name}")

