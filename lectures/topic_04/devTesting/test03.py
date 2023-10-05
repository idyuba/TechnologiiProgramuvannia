def genIntValue(promt:str):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            print("value is not ineger")


def main():
    xValue = genIntValue("What is x: ")
    print(xValue)

    yValue = genIntValue("What is y: ")
    print(yValue)


main()