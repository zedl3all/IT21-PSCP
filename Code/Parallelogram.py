"""Parallelogram"""

_X = str(input())
for i in range(1, len(_X) + 1):
    print(" " * (len(_X) - i) + _X[:i])
for i in range(1, len(_X) + 1):
    print(_X[i:])
