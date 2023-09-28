
#animals = ["cat", "dog", "duck"]
#paws = ["4", "4", "2"]
#is_vactinatet = [True, True, False]

# dic
# {key:value}

testDict = {"a": 1, "b":2}
#print(testDict)

animals = {
    "dog" : 4,
    "cat" : 4,
    "duck" : 2
}

#print(animals)

#for elem in animals:
#    print(elem, animals[elem])



'''
  | name  | paws | is_vactinated
0 | dog   |  4   | True
1 | cat   |  4   | False
2 | goose |  2   | True
'''

animals = [
    {"name" : "dog", "paws" : 4, "is_vactinated" : True},
    {"name" : "cat", "paws" : 4, "is_vactinated" : True},
    {"name" : "duck", "paws" : 2, "is_vactinated" : False},
]

for animal in animals:
    print(f" type is {animal['name']} paws cnt {animal['paws']}")