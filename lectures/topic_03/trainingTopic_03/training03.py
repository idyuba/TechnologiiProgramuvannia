# get number from user
'''
n = input("What x? :")
if n < 0:
    n = input("What x? :")
    if n < 0:
        n = input("What x? :")
'''

while True:
    n = int(input("What n? :"))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("bark")
