def getName():
    name = input("What is your name: ")
    if name != "Ihor":
        raise NameError('Name which was inputed not equal Ihor')
    return name

def main():
    while True:
        try:
            getName()
            break
        except NameError:
            pass
    print("Name has been validated")
    return

main()