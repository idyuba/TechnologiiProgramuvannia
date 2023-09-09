'''
def main():
    bark(3) # burk doesnt exist yet

def bark(n):
    for _ in range(n):
        print("bark")
'''

def main():
    number = get_number()
    bark(number) # burk doesnt exist yet

def get_number():
    while True:
        n = int(input("What n? :"))
        if n > 0:
            break
    return n

def bark(n):
    for _ in range(n):
        print("bark")


main()