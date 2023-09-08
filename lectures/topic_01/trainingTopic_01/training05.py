import math

# aX**2 + bX + c = 0
# sample  X**2 - 2X -3 = 0, x1 = 3, x2 = -1



a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

# D = b**2 - 4ac
# D = 16

D = b**2 - 4*a*c
print("D = ", D)

# x1 = (-b + sqrt(D))/2*a
# x2 = (-b - sqrt(D))/2*a

x1 = (-b + math.sqrt(D))/2*a
x2 = (-b - math.sqrt(D))/2*a
print("x1 = ", x1)
print("x2 = ", x2)
