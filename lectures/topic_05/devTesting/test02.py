import random
import statistics # https://docs.python.org/3/library/statistics.html

valure = random.randint(1, 100)
print(valure)

lst =[1, 2, 3, 4, 5, 8]
print(lst)
random.shuffle(lst)
print(lst)


mark = [80, 60, 95, 100, 87]
value1 = statistics.mean(mark)
print(value1)
