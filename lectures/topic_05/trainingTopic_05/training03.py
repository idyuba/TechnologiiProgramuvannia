
# random.randint(a, b)
# random.shuffle(x)

from random import randint
from random import shuffle

rand_int = randint(1, 10)
print(rand_int)

some_list = ["1", "2", "3", "4", "5", "6"]
print(some_list)
shuffle(some_list)
for elem in some_list:
    print(elem)
