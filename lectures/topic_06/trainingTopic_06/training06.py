# csv file
with open("dump02.txt") as file:
    for line in file:
        # what to do in csv situation with line
        # split - remember from Theme 01
        # print(line.rstrip().split(","))
        #row = line.rstrip().split(",")
        name, mark = line.rstrip().split(",")
        #print(f"{row[0]} has mark {row[1]}")
        print(f"{name} has mark {mark}")