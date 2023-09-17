# we can try to do something
# in case we will get some exception except will help us

# in case of wrong input - normal mesage 
try:
    x = int(input("What x?: "))
    print(f"x is {x}")
    y = 100/x
    print(f"y is {y}")
except ValueError:
    print("x is not an integer")
except ZeroDivisionError:
    print("x musn't be ZERO")


