"""Sequence VIII"""

_X = int(input())
#_Z = ""
_Z = []

for i in range(_X):
    _Y = "%02d" % (i+1)
    _Z.append(_Y)
    #_Z = _Z + _Y
    _R = " ".join(_Z)
    #print(" ".join(_Z))
    print(str(_R).rjust((_X*3)-1, " "))
    #print(" ".join(_Z.rjust((_X*3)-1," ")))
