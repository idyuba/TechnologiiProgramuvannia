# packages
# https://pypi.org/
# https://pypi.org/project/cowsay/

# pip install cowsay
# pip show cowsay

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow(f"Hello {sys.argv[1]}")
    cowsay.trex(f"Hello {sys.argv[1]}")


