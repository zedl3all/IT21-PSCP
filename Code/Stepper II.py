"""Stepper II"""

_X = int(input())
_Y = int(input())

if _X < _Y:
    for _ in range(_X, _Y + 1):
        print(_)
else:
    for _ in range(_X, _Y - 1, -1):
        print(_)
