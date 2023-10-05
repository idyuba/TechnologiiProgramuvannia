# print("Hello, world")

#a = 3
#b = 0

# c = a / b # ZeroDivisionError
# c = x + 7 # NameError
# c = 'a' + 7 # TypeError
try:
    x = int(input("What is x: "))
    print(f"x is {x}")
    y = 100/x
    print(f"y is {y}")
except ValueError:
    print("Wrong data ")
except ZeroDivisionError:
    print("x must not be ZERO")