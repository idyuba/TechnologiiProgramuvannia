x = int(input("What is x?: "))

# even or odd nomber, cleanly devided by 2

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# sample with function
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

if is_even(x):
    print("Even")
else:
    print("Odd")