import math

def FindRoots(a, b, c):
    D = b**2 - 4 * a * c
    x1 = (-b + math.sqrt(D)) / 2 * a
    x2 = (-b - math.sqrt(D)) / 2 * a
    return x1, x2


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

result = FindRoots(a, b, c)
print(result)