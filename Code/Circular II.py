"""circle2"""
import math

_X1 = float(input())
_Y1 = float(input())
_R1 = float(input())
_X2 = float(input())
_Y2 = float(input())
_R2 = float(input())

_CAL = math.sqrt((_X2-_X1)**2+(_Y2-_Y1)**2)

if _CAL < _R1+_R2:
    print("Yes")
else:
    print("No")
