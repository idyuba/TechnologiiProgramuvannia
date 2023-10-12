
def hello(name):
    print(f"Hello, {name}")

def goodBay(name):
    print(f"Good bay, {name}")


def main():
    hello("Ihor")
    hello("Jon")
    hello("Zak")
    goodBay("Zak")
    goodBay("Jon")
    goodBay("Ihor")


if __name__ == "__main__":
    main()