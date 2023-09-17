def get_int_value():
    while True:
        try:
            x = int(input("What x?: "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x # move instead of break

def get_int_value_1():
    while True:
        try:
            return int(input("What x?: "))
        except ValueError:
            print("x is not an integer")

def get_int_value_2():
    while True:
        try:
            return int(input("What x?: "))
        except ValueError:
            pass

def get_int_value_3(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

def main1():
    x = get_int_value_2() # good sample of function using
                        # instead a lot of code only one line   
    print(f"x is {x}")

def main():
    int_value = get_int_value_3("What is x? : ")

main()