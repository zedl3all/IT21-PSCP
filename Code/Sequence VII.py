"""Sequence VII"""

_X = int(input())

for _ in range(_X):
    for _ in range(1, _+2):
        print(_, end=" ")
    print("")

for _ in range(_X-1, 0, -1):
    for _ in range(1, _+1):
        print(_, end=" ")
    print("")
