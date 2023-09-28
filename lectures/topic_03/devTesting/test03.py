'''
number = int(input("Enter the count: "))
if number < 0: 
    number = int(input("Enter the count: "))
    if number < 0:
        number = int(input("Enter the count: "))
'''

def getNumber():
    while True:
        number = int(input("Enter the count: "))
        if number < 0:
            continue
        else: 
            break
    return number

def dogSay(number):
    for _ in range(number):
        print(f"Woof number")
    return

# ask number of woof
# woof say

def main():
    number = getNumber()
    dogSay(number)



main()



