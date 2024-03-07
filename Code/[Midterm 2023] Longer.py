"""[Midterm 2023] Longer"""

import math
_R = float(input())
_A = float(input())
_B = float(input())
_CIRCLE = 2*math.pi*_R
_SQUARE = (2*_A)+(2*_B)

if _CIRCLE > _SQUARE:
    print("Circle is longer")
    print("%.5f" % (_CIRCLE-_SQUARE))
elif _SQUARE > _CIRCLE:
    print("Rectangle is longer")
    print("%.5f" % (_SQUARE - _CIRCLE))
else:
    print("Equal")
    print("%.5f" % (_SQUARE - _CIRCLE))
