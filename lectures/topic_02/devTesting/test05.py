'''
    90 - 100 A
    80 - 89  B
    70 - 79  C
    60 - 69  D
        F

'''

mark = input("What is your mark?: ")

if mark == "A":
    print("Your score in 90 - 100 ")
elif mark == "B":
    print("Your score in 80 - 89")
elif mark == "C":
    print("Your score in 70 - 79")
elif mark == "D":
    print("Your score in 60 - 69")
elif mark == "F":
    print("Your score under 59 ")
else:
    print("Wrong mark")
