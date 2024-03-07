"""BootSequence"""

_X = int(input())
_Y = ""

for _ in range(_X):
    #print(_ + 1)
    _Y = _Y + "_" + str(_ + 1)

print(_Y[1:])
