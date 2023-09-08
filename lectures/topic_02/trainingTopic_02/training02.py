x = int(input("What is x?: "))
y = int(input("What is y?: "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# improvement
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# more improvement
if x == y:
    print("x is  equal to y")
else:
    print("x is not equal to y")