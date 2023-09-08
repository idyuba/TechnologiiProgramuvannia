# 1) compare integers
x = int(input("What is x?: "))
y = int(input("What is y?: "))

# need to make decission
# only two option are valid true or false
if x < y:
    print("x less then y")
if x > y:
    print("x greater then y")
if x == y:
    print("x equal y")

# do not ask a question in case answer has been found
if x < y:
    print("x less then y")
elif x > y:
    print("x greater then y")
elif x == y:
    print("x equal y")

# else
if x < y:
    print("x less then y")
elif x > y:
    print("x greater then y")
else:
    print("x equal y")






