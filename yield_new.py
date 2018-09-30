#from typing import List

nested = [[1, 2], [3, 5], [6]]  # type: List[List[int]]


def flatten(args):
    for sublist in args:
        for element in sublist:
            yield element


for num in flatten(nested):
    print num
