try:
    x = int(input("What is x: "))
    print(f"x is {x}")
    y = 100/x
    print(f"y is {y}")
except Exception as ex:
    print(type(ex))
    print(ex.args)
    print(ex)
