'''
# try to do minimal work under try except
try:
    x = int(input("What x?: "))
except ValueError:
    print("x is not an integer")

# Name erro is present
# because of exception present x is undefined
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