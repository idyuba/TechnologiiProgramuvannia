# dict - two demesion, word and definition

#animals = ["cat", "dog", "goose"]
#paws = ["4", "4", "2"]

# want to asosiate
# using dict {}

# animals = {"dog" : 4, "cat" : 4, "goose": 2}
testDisct = {"a": 1, "b": 2}
print(testDisct.keys())
print(testDisct.values())
print(testDisct.items())


animals = {
    "dog" : 4, 
    "cat" : 4, 
    "goose": 2
}

print("cat" in animals)

print(animals)
print(animals["dog"])

# by design it will be iterated over the keys
for animal in animals:
    print(animal)

for animal in animals:
    print(animal, animals[animal])

# what about one more value for dict element
# animal, paw, is_vactinated
'''
  | type  | paws | is_vactinated
0 | dog   |  4   | True
1 | cat   |  4   | False
2 | goose |  2   | True
'''
# list of the dictionary []
# inside of the list - dict, collection of key value pairs
animals = [
    {"type":"dog", "paws" : 4, "is_vactinated" : True},
    {"type":"cat", "paws" : 4, "is_vactinated" : False},
    {"type":"goose", "paws" : 2, "is_vactinated" : True}
]

print(animals)

for animal in animals:
    print(animal)

for animal in animals:
    print(animal["paws"])
