# we need soe fuctionalyty with class itself
# no matter what exactly instance variable

import random

'''
class Hat:
    def __init__(self):
        self.houses = ["aaa", "bbb", "ccc"]


    def sort(self, name):
        house = random.choice(self.houses)
        print(name, " in", house )

hat = Hat() # comman syntax of instantiation
hat.sort("Harry")

'''

class Hat:
    # class vaiables exists, one copy for all of the objects
    houses = ["aaa", "bbb", "ccc"]

    @classmethod
    def sort(cls, name): # reference to class itself
        house = random.choice(cls.houses)
        print(name, " in", house )

Hat.sort("qwqwqwwq")