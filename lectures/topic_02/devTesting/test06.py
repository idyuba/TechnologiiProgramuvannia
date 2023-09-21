
mark = input("What is your mark?: ")

match mark:
    case "A":
        print("Your score in 90 - 100 ")
    case "B":
        print("Your score in 80 - 89")
    case "C":
        print("Your score in 70 - 79")
    case "D":
        print("Your score in 60 - 69")
    case "F":
        print("Your score under 60")
    case _:
        print("Wrong mark")