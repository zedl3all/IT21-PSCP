"""Tuple's Sad life"""

_X = str(input())
_X = tuple(_X.split())
_Y = str(input())

for row in range(_X.count(_Y)):
    for col in range(_X.count(_Y)):
        print(_X.index(_Y), end=' ')
    print()
