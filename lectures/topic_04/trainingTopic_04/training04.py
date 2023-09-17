'''
try:
    x = int(input("What x?: "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}") # NameError
'''

''' NameError fix
try:
    x = int(input("What x?: "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
'''

while True:
    try:
        x = int(input("What x?: "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")