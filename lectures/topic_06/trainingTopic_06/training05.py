names = []

# r - default
with open("dump02.txt") as file:
    for line in file:
        names.append(line.rstrip())

# all name are in list
# reverse sorting
# sorted(iterable, /, *, key=None, reverse=False)
for name in sorted(names):
    print(f"Hello, {name}")