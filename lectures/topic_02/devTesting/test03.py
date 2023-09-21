'''
    90 - 100 A
    80 - 89  B
    70 - 79  C
    60 - 69  D
        F

'''

score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90: # could be <= 89
    print("Grade B")
elif score >= 70 and score < 80:
    print("Grade C")
elif score >= 60 and score < 70:
    print("Grade D")
else:
    print("Grade F")