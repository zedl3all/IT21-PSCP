"""inflation"""


_X = float(input())
_Y = int(input())
_Z = _X

for i in range(_Y):
    _Z += (3.81/100)*_Z
    _Z = (int(_Z*100))/100

print("%.2f" % _Z)
