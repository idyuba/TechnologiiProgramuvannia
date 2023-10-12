
# https://docs.python.org/3/library/sys.html

import sys

if len(sys.argv) == 2:
    print(f"Hello, {sys.argv[1]}")
else:
    print("Wrong count of parameters")


