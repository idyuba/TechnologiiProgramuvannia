from random import choice # will load function name choice into current namespace

''' function overloading sample
def choice(lst):
    print("Hello from own choice function")
'''
    
for _ in range(10):
    random_choise = choice(["stone", "scissor", "paper"]) # indead a list
    print(random_choise)

